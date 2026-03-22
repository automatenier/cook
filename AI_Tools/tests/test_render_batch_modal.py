"""
Tests for render_batch_modal.py — pure Python logic only, no Modal calls.
Run: py -3 24_Tools/tests/test_render_batch_modal.py
"""

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from render_batch_modal import (
    build_props,
    extract_cta_keyword,
    get_composition,
    parse_script,
    strip_emotion_tags,
    _type_from_stem,
    CLIENTS,
    SKIP_STEMS,
)

PASS = "\033[92mPASS\033[0m"
FAIL = "\033[91mFAIL\033[0m"
_errors = []


def check(name: str, got, expected):
    if got == expected:
        print(f"  {PASS}  {name}")
    else:
        print(f"  {FAIL}  {name}")
        print(f"       got:      {got!r}")
        print(f"       expected: {expected!r}")
        _errors.append(name)


# ── strip_emotion_tags ──────────────────────────────────────────────────────────

print("\nstrip_emotion_tags")
check("removes [pensive]",
      strip_emotion_tags("[pensive] Kenapa gagal?"),
      "Kenapa gagal?")
check("removes [energetic] inline",
      strip_emotion_tags("[energetic] Ini tips-nya."),
      "Ini tips-nya.")
check("leaves text without tags",
      strip_emotion_tags("Komen MAKAN ke DM"),
      "Komen MAKAN ke DM")
check("handles multiple tags",
      strip_emotion_tags("[happy] Hook [sad] Body"),
      "Hook  Body")


# ── extract_cta_keyword ────────────────────────────────────────────────────────

print("\nextract_cta_keyword")
check("extracts **MAKAN**",
      extract_cta_keyword('Komen "**MAKAN**" nanti gue kirim.'),
      "MAKAN")
check("extracts **SISTEM**",
      extract_cta_keyword("Comment **SISTEM** for free template"),
      "SISTEM")
check("fallback to DM when no bold keyword",
      extract_cta_keyword("DM me for the template"),
      "DM")


# ── get_composition ────────────────────────────────────────────────────────────

print("\nget_composition")
check("value → ValueCTAReel",     get_composition("value"),       "ValueCTAReel")
check("value-cta → ValueCTAReel", get_composition("value-cta"),   "ValueCTAReel")
check("cta → ValueCTAReel",       get_composition("cta"),         "ValueCTAReel")
check("story → AuthenticityReel", get_composition("story"),       "AuthenticityReel")
check("bts → AuthenticityReel",   get_composition("bts"),         "AuthenticityReel")
check("Value + CTA → ValueCTAReel", get_composition("Value + CTA"), "ValueCTAReel")


# ── _type_from_stem ────────────────────────────────────────────────────────────

print("\n_type_from_stem")
check("date_type_slug",   _type_from_stem("2026-03-03_story_my-journey"), "story")
check("date_type",        _type_from_stem("2026-03-01_value-cta"),        "value-cta")
check("single part stem", _type_from_stem("myscript"),                    "value")


# ── parse_script ───────────────────────────────────────────────────────────────

print("\nparse_script")

SAMPLE_SCRIPT = """\
---
type: Value + CTA
client: Fadli
date: 2026-03-01
slug: diet-consistency
---

#### Hook
[pensive] Kenapa 90% orang gagal diet?

#### Value
[energetic] Motivasi kayak baterai hp, bisa abis.
Tapi sistem kayak charger-nya.

#### CTA
[happy] Komen "**MAKAN**" nanti gue kirim list-nya.
"""

with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as f:
    f.write(SAMPLE_SCRIPT)
    tmp_path = Path(f.name)

fm, sections = parse_script(tmp_path)
tmp_path.unlink()

check("frontmatter type",   fm.get('type'),   "Value + CTA")
check("frontmatter client", fm.get('client'), "Fadli")
check("frontmatter slug",   fm.get('slug'),   "diet-consistency")
check("hook section exists",  'hook' in sections, True)
check("value section exists", 'value' in sections, True)
check("cta section exists",   'cta' in sections, True)
check("hook has text", "Kenapa 90%" in sections['hook'], True)
check("MAKAN in cta",  "MAKAN" in sections['cta'], True)


# ── build_props — ValueCTAReel ─────────────────────────────────────────────────

print("\nbuild_props → ValueCTAReel")
props = build_props(fm, sections, "ValueCTAReel", "#FF6B6B")
check("has hookText",     'hookText'    in props, True)
check("has valueText",    'valueText'   in props, True)
check("has ctaText",      'ctaText'     in props, True)
check("has ctaKeyword",   'ctaKeyword'  in props, True)
check("has brandColor",   'brandColor'  in props, True)
check("emotion tags stripped from hook", '[pensive]' not in props['hookText'], True)
check("ctaKeyword is MAKAN", props['ctaKeyword'], "MAKAN")
check("brandColor passed through", props['brandColor'], "#FF6B6B")
check("hookText not empty", len(props['hookText']) > 0, True)


# ── build_props — AuthenticityReel ─────────────────────────────────────────────

print("\nbuild_props → AuthenticityReel")
STORY_SECTIONS = {
    'hook':  '[pensive] 6 bulan lalu gue nol klien.',
    'value': '[reflective] Gue bukan yang paling pintar.\nTapi gue konsisten setiap hari.\nSistem beats motivasi.',
}
story_props = build_props({}, STORY_SECTIONS, "AuthenticityReel", "#74B9FF")
check("has hookText",   'hookText'   in story_props, True)
check("has storyText",  'storyText'  in story_props, True)
check("has lessonText", 'lessonText' in story_props, True)
check("lessonText is last line", "Sistem beats motivasi" in story_props['lessonText'], True)
check("emotion stripped from hook", '[pensive]' not in story_props['hookText'], True)


# ── CLIENTS config ─────────────────────────────────────────────────────────────

print("\nCLIENTS config")
for key in ['fadli', 'mathew_jordan', 'ruth', 'real_estate']:
    check(f"{key} in CLIENTS", key in CLIENTS, True)
    check(f"{key} has color", 'color' in CLIENTS[key], True)
    check(f"{key} has workspace", 'workspace' in CLIENTS[key], True)
    check(f"{key} has output_dir", 'output_dir' in CLIENTS[key], True)


# ── SKIP_STEMS ─────────────────────────────────────────────────────────────────

print("\nSKIP_STEMS")
check("march sprint skipped", "march_2026_sprint" in SKIP_STEMS, True)


# ── Summary ────────────────────────────────────────────────────────────────────

print()
if _errors:
    print(f"\033[91mFAILED: {len(_errors)} test(s)\033[0m — {_errors}")
    sys.exit(1)
else:
    print(f"\033[92mAll tests passed.\033[0m")
