"""
Cook Tools — Modal deployment
Hosts repurpose_content as a 24/7 web UI + API on Modal.

Run locally:   PYTHONIOENCODING=utf-8 py -3 -m modal run AI_Tools/modal_app.py
Deploy:        PYTHONIOENCODING=utf-8 py -3 -m modal deploy AI_Tools/modal_app.py
"""

import json
import modal

app = modal.App("cook-tools")

image = (
    modal.Image.debian_slim()
    .pip_install("anthropic>=0.40.0", "fastapi[standard]", "mcp", "pytz")
)

# ── Prompt ────────────────────────────────────────────────────────────────────

REPURPOSE_PROMPT = """You are a content repurposing engine for JO Consult, an Indonesian online business coaching brand.

Your job is to take FINISHED content (a reel script, storyboard, or transcript) and produce everything needed to publish it across all platforms. You do NOT rewrite the creative. You preserve the voice, hook, and message exactly — then adapt format per platform.

Content type: {content_type}

Original content:
---
{content}
---

Generate ALL of the following. Return as JSON with this exact structure:

{{
  "music": {{
    "vibe": "<1-2 words>",
    "genre": "<genre>",
    "bpm": "<BPM range>",
    "track_suggestions": ["<track 1>", "<track 2>", "<track 3>"],
    "platform_note": "<note>"
  }},
  "pacing": {{
    "total_duration": "<e.g. 30s>",
    "beat_map": ["<0-3s: ...>", "<3-8s: ...>", "<8-15s: ...>", "<15-25s: ...>", "<25-30s: ...>"]
  }},
  "ig_reel": {{
    "caption": "<IG caption>",
    "hashtags": ["<hashtag>"],
    "cover_text": "<3-5 words>"
  }},
  "tiktok": {{
    "caption": "<TikTok caption max 150 chars>",
    "hashtags": ["<hashtag>"],
    "hook_text": "<first 2s text>"
  }},
  "threads_post": {{
    "text": "<300-500 chars>",
    "cta": "<CTA>"
  }},
  "story_sequence": [
    {{"slide": 1, "text": "<hook>", "visual": "<description>"}},
    {{"slide": 2, "text": "<value>", "visual": "<description>"}},
    {{"slide": 3, "text": "<CTA>", "visual": "<description>"}}
  ],
  "newsletter_email": {{
    "subject_line": "<5-8 words>",
    "preview_text": "<1 sentence>",
    "body": "<200-400 words>"
  }},
  "youtube_outline": {{
    "title": "<SEO title>",
    "hook": "<first 30s script>",
    "sections": ["<section 1>", "<section 2>", "<section 3>"],
    "cta": "<end CTA>",
    "description": "<2-3 sentences with keywords>"
  }}
}}

Rules:
- Preserve exact hook wording — don't rephrase it
- Indonesian market context (Bahasa or mixed Bahasa/English is fine)
- Online business coaching niche (helping coaches scale with AI/systems)
- Return ONLY valid JSON"""

# ── Core function ─────────────────────────────────────────────────────────────

@app.function(
    image=image,
    secrets=[modal.Secret.from_name("cook-secrets")],
    timeout=300,
)
def repurpose(content: str, content_type: str = "reel-value") -> dict:
    import os
    import json
    import anthropic

    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    prompt = REPURPOSE_PROMPT.format(content_type=content_type, content=content)

    message = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
    )

    raw = message.content[0].text.strip()
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[1]
        if raw.endswith("```"):
            raw = raw[:-3]

    return json.loads(raw)


# ── Remotion render ───────────────────────────────────────────────────────────
# Node.js + Chromium image — built once, cached by Modal
# Deploy runs from repo root: PYTHONIOENCODING=utf-8 py -3 -m modal deploy AI_Tools/modal_app.py

node_image = (
    modal.Image.from_registry("node:20-bullseye-slim")
    .apt_install(
        "chromium", "fonts-noto", "ca-certificates",
        "libnss3", "libatk1.0-0", "libatk-bridge2.0-0",
        "libcups2", "libxkbcommon0", "libxcomposite1",
        "libxdamage1", "libxfixes3", "libxrandr2",
        "libgbm1", "libpango-1.0-0", "libcairo2", "libasound2",
    )
    .run_commands("mkdir -p /remotion")
    .add_local_file("VLT_Content/AI_ENGINE/remotion/package.json", "/remotion/package.json")
    .add_local_file("VLT_Content/AI_ENGINE/remotion/tsconfig.json", "/remotion/tsconfig.json")
    .run_commands("cd /remotion && npm install 2>&1 | tail -3")
)

src_mount = modal.Mount.from_local_dir(
    "VLT_Content/AI_ENGINE/remotion/src",
    remote_path="/remotion/src",
)
public_mount = modal.Mount.from_local_dir(
    "VLT_Content/AI_ENGINE/remotion/public",
    remote_path="/remotion/public",
)


@app.function(
    image=node_image,
    mounts=[src_mount, public_mount],
    timeout=300,
)
def render_remotion(composition: str, props: dict = None) -> bytes:
    import subprocess, json

    args = [
        "npx", "remotion", "render",
        "src/index.ts",
        composition,
        "--output", f"/tmp/{composition}.mp4",
        "--browser-executable", "/usr/bin/chromium",
        "--gl", "swiftshader",
    ]

    if props:
        props_path = "/tmp/props.json"
        with open(props_path, "w") as f:
            json.dump(props, f)
        args += ["--props", props_path]

    result = subprocess.run(args, cwd="/remotion", capture_output=True, text=True, timeout=240)
    if result.returncode != 0:
        raise RuntimeError(result.stderr[-2000:])

    with open(f"/tmp/{composition}.mp4", "rb") as f:
        return f.read()


# ── Web UI ────────────────────────────────────────────────────────────────────

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cook — Repurpose Content</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
         background: #0f0f0f; color: #e8e8e8; min-height: 100vh; padding: 40px 20px; }
  .container { max-width: 800px; margin: 0 auto; }
  h1 { font-size: 1.5rem; font-weight: 600; margin-bottom: 4px; }
  .subtitle { color: #888; font-size: 0.875rem; margin-bottom: 32px; }
  label { display: block; font-size: 0.8rem; color: #aaa; margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.05em; }
  textarea { width: 100%; background: #1a1a1a; border: 1px solid #2a2a2a; border-radius: 8px;
             color: #e8e8e8; padding: 14px; font-size: 0.95rem; resize: vertical;
             min-height: 180px; font-family: inherit; outline: none; }
  textarea:focus { border-color: #444; }
  select { background: #1a1a1a; border: 1px solid #2a2a2a; border-radius: 8px;
           color: #e8e8e8; padding: 10px 14px; font-size: 0.95rem; outline: none; width: 100%; }
  .row { display: flex; gap: 16px; margin: 16px 0; align-items: flex-end; }
  .row > div { flex: 1; }
  button { background: #fff; color: #0f0f0f; border: none; border-radius: 8px;
           padding: 11px 24px; font-size: 0.95rem; font-weight: 600; cursor: pointer; }
  button:hover { background: #e0e0e0; }
  button:disabled { background: #333; color: #666; cursor: not-allowed; }
  .btn-secondary { background: #1a1a1a; color: #e8e8e8; border: 1px solid #2a2a2a; font-weight: 500; }
  .btn-secondary:hover { background: #222; }
  #status { margin-top: 16px; font-size: 0.875rem; color: #888; min-height: 20px; }
  #results { margin-top: 32px; display: none; }
  .section { background: #1a1a1a; border: 1px solid #222; border-radius: 10px;
             padding: 20px; margin-bottom: 16px; }
  .section-title { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.08em;
                   color: #666; margin-bottom: 12px; }
  .field { margin-bottom: 10px; }
  .field-label { font-size: 0.75rem; color: #666; margin-bottom: 2px; }
  .field-value { font-size: 0.9rem; color: #ccc; line-height: 1.5; white-space: pre-wrap; }
  .tags { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 4px; }
  .tag { background: #222; border: 1px solid #333; border-radius: 4px;
         padding: 3px 8px; font-size: 0.78rem; color: #aaa; }
  .actions { display: flex; gap: 10px; margin-bottom: 24px; }
</style>
</head>
<body>
<div class="container">
  <h1>Cook — Repurpose Content</h1>
  <p class="subtitle">Paste a reel script or transcript. Get 7 platform formats in one shot.</p>

  <label for="content">Script / Transcript</label>
  <textarea id="content" placeholder="Paste your hook, body, and CTA here..."></textarea>

  <div class="row">
    <div>
      <label for="type">Content Type</label>
      <select id="type">
        <option value="reel-value">Reel — Value</option>
        <option value="reel-auth">Reel — Authority</option>
        <option value="youtube">YouTube</option>
        <option value="story">Story</option>
      </select>
    </div>
    <div>
      <button id="submit-btn" onclick="runRepurpose()">Repurpose</button>
    </div>
  </div>

  <div id="status"></div>

  <div id="results">
    <div class="actions">
      <button class="btn-secondary" onclick="downloadJSON()">Download JSON</button>
    </div>

    <div class="section" id="sec-threads">
      <div class="section-title">Threads</div>
      <div class="field"><div class="field-value" id="threads-text"></div></div>
      <div class="field"><div class="field-label">CTA</div><div class="field-value" id="threads-cta"></div></div>
    </div>

    <div class="section" id="sec-ig">
      <div class="section-title">Instagram Reel</div>
      <div class="field"><div class="field-label">Cover Text</div><div class="field-value" id="ig-cover"></div></div>
      <div class="field"><div class="field-label">Caption</div><div class="field-value" id="ig-caption"></div></div>
      <div class="field"><div class="field-label">Hashtags</div><div class="tags" id="ig-hashtags"></div></div>
    </div>

    <div class="section" id="sec-tiktok">
      <div class="section-title">TikTok</div>
      <div class="field"><div class="field-label">Hook Text (0-2s)</div><div class="field-value" id="tiktok-hook"></div></div>
      <div class="field"><div class="field-label">Caption</div><div class="field-value" id="tiktok-caption"></div></div>
      <div class="field"><div class="field-label">Hashtags</div><div class="tags" id="tiktok-hashtags"></div></div>
    </div>

    <div class="section" id="sec-email">
      <div class="section-title">Newsletter Email</div>
      <div class="field"><div class="field-label">Subject</div><div class="field-value" id="email-subject"></div></div>
      <div class="field"><div class="field-label">Preview</div><div class="field-value" id="email-preview"></div></div>
      <div class="field"><div class="field-label">Body</div><div class="field-value" id="email-body"></div></div>
    </div>

    <div class="section" id="sec-youtube">
      <div class="section-title">YouTube</div>
      <div class="field"><div class="field-label">Title</div><div class="field-value" id="yt-title"></div></div>
      <div class="field"><div class="field-label">Hook (30s)</div><div class="field-value" id="yt-hook"></div></div>
      <div class="field"><div class="field-label">Description</div><div class="field-value" id="yt-desc"></div></div>
    </div>

    <div class="section" id="sec-music">
      <div class="section-title">Music</div>
      <div class="field"><div class="field-label">Vibe / Genre / BPM</div>
        <div class="field-value" id="music-info"></div></div>
      <div class="field"><div class="field-label">Track Suggestions</div>
        <div class="tags" id="music-tracks"></div></div>
      <div class="field"><div class="field-label">Platform Note</div>
        <div class="field-value" id="music-note"></div></div>
    </div>

    <div class="section" id="sec-stories">
      <div class="section-title">Story Sequence</div>
      <div id="stories-list"></div>
    </div>

    <div class="section" id="sec-pacing">
      <div class="section-title">Pacing / Beat Map</div>
      <div class="field"><div class="field-label">Duration</div><div class="field-value" id="pacing-duration"></div></div>
      <div id="beat-map"></div>
    </div>
  </div>
</div>

<script>
let lastResult = null;

async function runRepurpose() {
  const content = document.getElementById('content').value.trim();
  if (!content) { alert('Paste your content first.'); return; }

  const btn = document.getElementById('submit-btn');
  const status = document.getElementById('status');
  btn.disabled = true;
  btn.textContent = 'Running...';
  status.textContent = 'Sending to Claude on Modal...';
  document.getElementById('results').style.display = 'none';

  try {
    const res = await fetch('/repurpose', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ content, type: document.getElementById('type').value })
    });
    if (!res.ok) throw new Error(await res.text());
    const data = await res.json();
    lastResult = data;
    renderResults(data);
    status.textContent = 'Done.';
  } catch (e) {
    status.textContent = 'Error: ' + e.message;
  } finally {
    btn.disabled = false;
    btn.textContent = 'Repurpose';
  }
}

function renderResults(d) {
  document.getElementById('threads-text').textContent = d.threads_post?.text || '';
  document.getElementById('threads-cta').textContent = d.threads_post?.cta || '';
  document.getElementById('ig-cover').textContent = d.ig_reel?.cover_text || '';
  document.getElementById('ig-caption').textContent = d.ig_reel?.caption || '';
  renderTags('ig-hashtags', d.ig_reel?.hashtags || []);
  document.getElementById('tiktok-hook').textContent = d.tiktok?.hook_text || '';
  document.getElementById('tiktok-caption').textContent = d.tiktok?.caption || '';
  renderTags('tiktok-hashtags', d.tiktok?.hashtags || []);
  document.getElementById('email-subject').textContent = d.newsletter_email?.subject_line || '';
  document.getElementById('email-preview').textContent = d.newsletter_email?.preview_text || '';
  document.getElementById('email-body').textContent = d.newsletter_email?.body || '';
  document.getElementById('yt-title').textContent = d.youtube_outline?.title || '';
  document.getElementById('yt-hook').textContent = d.youtube_outline?.hook || '';
  document.getElementById('yt-desc').textContent = d.youtube_outline?.description || '';
  const m = d.music || {};
  document.getElementById('music-info').textContent = [m.vibe, m.genre, m.bpm].filter(Boolean).join(' · ');
  renderTags('music-tracks', m.track_suggestions || []);
  document.getElementById('music-note').textContent = m.platform_note || '';
  const storiesList = document.getElementById('stories-list');
  storiesList.innerHTML = (d.story_sequence || []).map(s =>
    `<div class="field"><div class="field-label">Slide ${s.slide} — ${s.visual}</div>
     <div class="field-value">${s.text}</div></div>`
  ).join('');
  document.getElementById('pacing-duration').textContent = d.pacing?.total_duration || '';
  const beatMap = document.getElementById('beat-map');
  beatMap.innerHTML = (d.pacing?.beat_map || []).map(b =>
    `<div class="field"><div class="field-value">${b}</div></div>`
  ).join('');
  document.getElementById('results').style.display = 'block';
}

function renderTags(id, items) {
  document.getElementById(id).innerHTML = items.map(t =>
    `<span class="tag">${t}</span>`).join('');
}

function downloadJSON() {
  if (!lastResult) return;
  const blob = new Blob([JSON.stringify(lastResult, null, 2)], { type: 'application/json' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = 'repurposed_content.json';
  a.click();
}
</script>
</body>
</html>"""


from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse

web_app = FastAPI()


@web_app.get("/", response_class=HTMLResponse)
async def index():
    return HTML


@web_app.post("/repurpose")
async def repurpose_api(request: Request):
    body = await request.json()
    content = body.get("content", "")
    content_type = body.get("type", "reel-value")
    result = repurpose.remote(content, content_type)
    return JSONResponse(result)


@web_app.post("/render")
async def render_api(request: Request):
    from fastapi.responses import Response
    body = await request.json()
    composition = body.get("composition", "PerformaKonten")
    props = body.get("props", None)
    mp4_bytes = render_remotion.remote(composition, props)
    return Response(
        content=mp4_bytes,
        media_type="video/mp4",
        headers={"Content-Disposition": f"attachment; filename={composition}.mp4"},
    )


@app.function(
    image=image,
    secrets=[modal.Secret.from_name("cook-secrets")],
)
@modal.asgi_app()
def frontend():
    from mcp.server.fastmcp import FastMCP
    
    # 1. Initialize FastMCP server
    mcp = FastMCP("cook-mcp-server")

    # 2. Define MCP tools
    @mcp.tool()
    def repurpose_content(content: str, content_type: str = "reel-value") -> dict:
        """
        Repurpose content (script/transcript) for all platforms.
        content_type options: reel-value, reel-auth, youtube, story
        """
        return repurpose.remote(content, content_type)

    @mcp.tool()
    def render_video(composition: str, props: dict = None) -> str:
        """
        Render a Remotion video. Returns a message (actual bytes available via /render endpoint).
        """
        # Note: Since MCP tools usually return text/JSON, we just trigger the remote call
        # or explain how to get the file.
        render_remotion.remote(composition, props)
        return f"Render triggered for {composition}. Download it via the web UI."

    # 3. Create Starlette app with stateless HTTP transport
    starlette_app = mcp.make_app(transport="streamable-http", stateless_http=True)

    # 4. Mount onto existing web_app
    web_app.mount("/mcp", starlette_app)
    
    return web_app


# ── Local test ────────────────────────────────────────────────────────────────

@app.local_entrypoint()
def main():
    from pathlib import Path
    test = """
    Hook: Kenapa coach dengan 1000 follower bisa dapat 50 juta/bulan,
    tapi yang 100rb follower malah struggling?
    Body: Bukan soal jumlah audience. Soal sistem.
    CTA: Comment SISTEM kalau mau template gratisnya.
    """
    print("Running on Modal cloud...")
    result = repurpose.remote(test, "reel-value")
    out = Path(".tmp/repurposed_test.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Saved to {out}")
    print(f"Threads: {result['threads_post']['text'][:100]}...")
    print(f"Email: {result['newsletter_email']['subject_line']}")
    print(f"YouTube: {result['youtube_outline']['title']}")
