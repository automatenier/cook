---
tags:
  - consulting
---
# Client Fulfillment Workflow

## Objective
After a fitness coach pays and closes, deliver the full fulfillment experience: onboarding, offer blueprint creation, content audit, and lead activation. This workflow picks up where the Setter DM Outreach workflow ends (Stage 9: Closed → Payment → Onboarding).

## Required Inputs
- Client name and contact info (from Excel CRM, stage: Closed)
- Completed onboarding form (JSON) — collected via intake call or async form
- Access to client's existing content (Instagram, TikTok, etc.)
- Client's existing lead database (if any)

## Tools Used
- `tools/offer_agent.py` — Generate offer blueprint via Claude
- Excel CRM (for tracking fulfillment progress)
- Google Calendar (for milestone check-ins)
- WhatsApp (for async communication)

## The 4-Step Fulfillment Flow

### Step 1: Onboarding (Day 1-2)

**Goal:** Get the new client set up with access and collect their onboarding data.

**Actions:**
1. Create client folder: `Fulfillment/_CLIENT_DELIVERABLES/{client_name}/`
2. Send welcome email (template: `Fulfillment/_ONBOARDING/welcome_email_template.md`)
3. Grant access to training modules and community
4. Collect onboarding form answers — use `Fulfillment/_ONBOARDING/onboarding_form_template.md` as guide
5. Save completed form as `Fulfillment/_ONBOARDING/{client_name}_onboarding.json`

**Expected output:**
- Client has module + community access
- Completed onboarding JSON file ready for Step 2

### Step 2: Offer Blueprint (Day 2-4)

**Goal:** Run the Offer Agent to generate a professional offer sheet from onboarding data.

**Option A: Async processing (from completed form)**
```bash
python tools/offer_agent.py --from-file Fulfillment/_ONBOARDING/{client_name}_onboarding.json
```

**Option B: Live consultation (interactive on call)**
```bash
python tools/offer_agent.py --interactive --client-name "{client_name}"
```

**What happens:**
1. Offer Agent reads onboarding data (or walks through Phase 1-6 questions)
2. Claude processes answers using the High-Ticket Fitness Architect system prompt
3. Generates offer sheet as Markdown + JSON in `.tmp/`
4. Copies final files to `Fulfillment/_OFFER_BLUEPRINT/offer_sheets/{client_name}/`

**Expected output:**
- `{client_name}_offer_sheet.md` — Copy-paste ready for PDF export
- `{client_name}_offer_sheet.json` — Structured data for further automation

**Review:** Walk through the offer sheet with the client on a call. Adjust if needed, then finalize.

### Step 3: Content Audit (Day 5-10)

**Goal:** Analyze the client's existing content and identify gaps, then create a strategic content blueprint.

**Actions:**
1. Review client's last 30 days of content across platforms
2. Use audit template: `Fulfillment/_CONTENT_AUDIT/audit_templates/`
3. Score each content piece: hook quality, CTA presence, niche alignment, engagement rate
4. Identify top 3 content gaps (missing pillars, weak CTAs, no lead magnets)
5. Create content blueprint with weekly posting schedule

**Expected output:**
- Content audit report saved to `Fulfillment/_CONTENT_AUDIT/client_audits/{client_name}/`
- Weekly content calendar (first 4 weeks)
- List of 10 content ideas tailored to their offer

### Step 4: Lead Activation (Day 10-14)

**Goal:** Re-engage the client's existing database (old leads, past inquiries, followers who engaged but never bought).

**Actions:**
1. Export client's existing lead list (DM history, email list, old inquiries)
2. Segment leads by temperature: Hot (engaged recently), Warm (engaged 30-90 days), Cold (90+ days)
3. Use reactivation scripts from `Fulfillment/_LEAD_ACTIVATION/reactivation_scripts/`
4. Customize scripts with the client's new offer (from Step 2)
5. Coach the client through sending the first 10 reactivation messages

**Expected output:**
- Segmented lead list
- Customized reactivation scripts (DM + email + WhatsApp)
- First batch of reactivation messages sent

## Edge Cases
- **Client hasn't closed yet:** Do NOT start fulfillment. Redirect to Setter DM workflow Stage 7-9
- **Client can't fill onboarding form:** Use `--interactive` mode on a call to walk through questions live
- **Client has no existing content:** Skip Step 3, focus on content creation workflow instead (`workflows/content_creation.md`)
- **Client has no existing leads:** Skip Step 4, focus on building lead gen systems from scratch
- **Offer sheet needs major changes:** Re-run offer agent with updated JSON, don't manually edit the markdown
- **Client goes unresponsive:** Follow up at Day 3, Day 7, Day 14. If no response after 14 days, pause fulfillment and flag in CRM

## Timeline Summary

| Step | Name | Days | Deliverable |
|------|------|------|-------------|
| 1 | Onboarding | 1-2 | Access + onboarding JSON |
| 2 | Offer Blueprint | 2-4 | Offer sheet (MD + JSON) |
| 3 | Content Audit | 5-10 | Audit report + content calendar |
| 4 | Lead Activation | 10-14 | Reactivation scripts + first batch sent |

## KPIs (Per Client)

| Metric | Target |
|--------|--------|
| Onboarding completion | Within 48 hours of payment |
| Offer sheet generated | Within 4 days |
| Content audit delivered | Within 10 days |
| First reactivation batch sent | Within 14 days |
| Client satisfaction (post-fulfillment) | 8+/10 |
