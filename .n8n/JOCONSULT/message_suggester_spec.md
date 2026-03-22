---
tags:
  - automation
---
# Message Suggester — n8n Workflow Spec

> **What it does:** Setter pastes a DM conversation into Telegram → Claude reads context + CRM stage → suggests 2-3 reply options → setter picks one and sends manually.
> **Model:** claude-haiku-4-5-20251001 (upgrade to Sonnet if quality needs improving)
> **Estimated cost:** ~$4.20/month at 20 uses/day (Haiku, full sequences)

---

## Flow Diagram

```
Setter pastes convo into Telegram bot
        ↓
n8n Telegram Trigger (receives /suggest command)
        ↓
Parse Node — extract lead username, stage, conversation
        ↓
Google Sheets Node — pull lead's CRM row (stage, pain, notes)
        ↓
Anthropic API Node — Claude reads all context → generates reply options
        ↓
Format Node — clean up Claude output into readable Telegram message
        ↓
Telegram Send — reply to setter with 3 options + recommendation
```

---

## n8n Node Breakdown

### Node 1 — Telegram Trigger
- **Type:** Telegram Trigger
- **Bot:** Your existing setter bot (or create `@HTSSetterBot`)
- **Listen for:** Messages starting with `/suggest`
- **Output:** `{{ $json.message.text }}`

---

### Node 2 — Parse Input
- **Type:** Code (JavaScript)
- **Purpose:** Extract structured data from setter's message

```javascript
const raw = $input.first().json.message.text;

// Remove the /suggest command
const body = raw.replace('/suggest', '').trim();

// Try to extract structured fields
const leadMatch = body.match(/LEAD:\s*@?(\S+)/i);
const stageMatch = body.match(/STAGE:\s*(.+)/i);
const painMatch = body.match(/PAIN:\s*"?(.+?)"?\n/i);
const convoMatch = body.match(/CONVO:\n([\s\S]+)/i);

return [{
  json: {
    lead_username: leadMatch ? leadMatch[1] : 'unknown',
    stage: stageMatch ? stageMatch[1].trim() : 'unknown',
    pain: painMatch ? painMatch[1].trim() : '',
    conversation: convoMatch ? convoMatch[1].trim() : body,
    raw_input: body,
    chat_id: $input.first().json.message.chat.id,
    setter_name: $input.first().json.message.from.first_name
  }
}];
```

---

### Node 3 — Get CRM Data (Google Sheets)
- **Type:** Google Sheets
- **Operation:** Get Row(s)
- **Authentication:** **Service Account** (NOT OAuth2 — never expires, no weekly re-auth)
- **Sheet:** Your CRM Google Sheet
- **Lookup column:** `Username`
- **Lookup value:** `{{ $json.lead_username }}`
- **Returns:** Full CRM row for this lead (stage, ICP type, notes, last contact)
- **On not found:** Continue with empty CRM data (new lead)

> **Why Service Account?** OAuth2 re-auth expires every ~7 days. Service Account uses a permanent JSON key — set once, runs forever. Setup: `n8n/SOP.md`

---

### Node 4 — Build Claude Prompt
- **Type:** Code (JavaScript)
- **Purpose:** Assemble final prompt with all context

```javascript
const parsed = $('Parse Input').first().json;
const crm = $('Get CRM Data').first().json || {};

const crmContext = crm.Username ? `
CRM DATA FOR THIS LEAD:
- Username: @${crm.Username}
- Lead Type: ${crm.LeadType || 'Unknown'}
- Current Stage: ${crm.Status || parsed.stage}
- Pain Point: ${crm.Objections || parsed.pain || 'Not recorded yet'}
- Last Contact: ${crm.Date || 'Unknown'}
- Notes: ${crm['Mindmap'] || 'None'}
` : `CRM DATA: New lead — not yet in CRM. Stage provided by setter: ${parsed.stage}`;

const userMessage = `
${crmContext}

CURRENT CONVERSATION:
${parsed.conversation}

SETTER NAME: ${parsed.setter_name}
LEAD USERNAME: @${parsed.lead_username}
`;

return [{ json: { ...parsed, claude_user_message: userMessage } }];
```

---

### Node 5 — Claude API (Anthropic)
- **Type:** HTTP Request
- **Method:** POST
- **URL:** `https://api.anthropic.com/v1/messages`
- **Headers:**
  ```
  x-api-key: {{ $env.ANTHROPIC_API_KEY }}
  anthropic-version: 2023-06-01
  content-type: application/json
  ```
- **Body:** (see `claude_prompt.md` for full system prompt)
  ```json
  {
    "model": "claude-haiku-4-5-20251001",
    "max_tokens": 1500,
    "system": "<paste full system prompt from claude_prompt.md>",
    "messages": [
      {
        "role": "user",
        "content": "{{ $json.claude_user_message }}"
      }
    ]
  }
  ```

---

### Node 6 — Format Response
- **Type:** Code (JavaScript)
- **Purpose:** Pull Claude's text output, format for Telegram

```javascript
const claudeOutput = $input.first().json.content[0].text;
const lead = $('Parse Input').first().json.lead_username;

const formatted = `🎯 *Reply Suggestions for @${lead}*\n\n${claudeOutput}`;

return [{ json: {
  message: formatted,
  chat_id: $('Parse Input').first().json.chat_id
}}];
```

---

### Node 7 — Telegram Send Reply
- **Type:** Telegram
- **Operation:** Send Message
- **Chat ID:** `{{ $json.chat_id }}`
- **Text:** `{{ $json.message }}`
- **Parse Mode:** Markdown

---

### Node 8 — Update CRM Stage (Optional)
- **Type:** Google Sheets
- **Operation:** Update row
- **Trigger:** Only if Claude detected a stage change
- **Updates:** Status column, last contact date

---

## Telegram Usage Format

Setter types this into the bot:

```
/suggest
LEAD: @fitnesscoachahmad
STAGE: Problem Aware
PAIN: "can't get consistent leads"

CONVO:
Them: Eh iya bro, udah nyoba posting tiap hari tapi DM nya sepi banget
Me: Wah iya, emang susah kalau cuma ngandalin konten doang. Udah berapa lama online coaching nya?
Them: Sekitar 8 bulan, tapi klien nya masi 2-3 orang aja
Me: Nah itu wajar banget sebenarnya. Yang biasanya jadi masalah di stage itu apa?
Them: Kayaknya di conversion sih, orang tau gue tapi ga ada yang DM
```

---

## Cost Per Use

| Model | Input tokens | Output tokens | Cost per call |
|---|---|---|---|
| Haiku (default) | ~2,500 | ~1,200 | **$0.007** |
| Sonnet (upgrade) | ~2,500 | ~1,200 | **$0.057** |

At 20 uses/day:
- Haiku: **$4.20/month**
- Sonnet: **$34/month**

**Recommendation:** Start with Haiku. Output is now a full sequence (3-4 messages with branching) so quality difference from Sonnet is smaller than you'd think. Switch to Sonnet only if sequence logic feels off.

---

## Setup Checklist

- [ ] Create Telegram bot via @BotFather → save token
- [ ] Add `ANTHROPIC_API_KEY` to n8n credentials
- [ ] Add `TELEGRAM_BOT_TOKEN` to n8n credentials
- [ ] Connect Google Sheets node to CRM spreadsheet
- [ ] Test with 1 real conversation before going live
- [ ] Share bot link with setter team
