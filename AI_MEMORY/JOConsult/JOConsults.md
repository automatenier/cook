---
tags:
  - memory
---
# JO Consult — Offer, ICP & Active Clients

## Service: Bedah Digital

- Duration: 14-day sprint → ongoing monthly retainer
- Language: Bahasa Indonesia (all client-facing comms) + English (agent internal outputs)
- Geography: Indonesia — onsite filming requires JABODETABEK presence
- Filming: Day 4 onsite session (2 hrs) — Jordan directs talking head, VSL, b-roll, testimonials
- Email: jordanmathew811@gmail.com (all client contracts + comms)

## Offer Tiers

| Tier | Price | Duration | Key Deliverables |
|------|-------|----------|-----------------|
| Bedah Digital | [FILL IN] | 14-day sprint + monthly | Full content system, VSL funnel, offer sheet, lead activation, team SOPs |
| [Mid tier name] | [FILL IN] | [FILL IN] | [FILL IN] |
| [High tier name] | [FILL IN] | [FILL IN] | [FILL IN] |

## ICP (Ideal Customer Profile)

- **Who:** Indonesian online coaches / fitness trainers, 1–3 years in business
- **Situation:** Has clients, getting results, but stuck on inconsistent leads + manual DMs
- **Pain (surface):** No predictable lead flow, spending hours in DMs with no system
- **Pain (deep):** Fear of stagnation, burning out doing everything manually, not scaling
- **Dream outcome:** RM10k+/mo automated pipeline — content attracts, setter closes, AI handles follow-up
- **Objections:** "I'm not tech-savvy", "I've tried content before and it didn't work", "I don't have time"

## Active Clients

| Client | Tier | Phase | Day | Started | Worksheet |
|--------|------|-------|-----|---------|-----------|
| Fadli | Bedah Digital | Onboarding | 0 | 2026-02-21 | `PDCT_JO_Consult/deliverables/Z Products/Client Worksheet/Client_2_Worksheet.md` |

## Key File Paths (per client)

- Worksheet: `PDCT_JO_Consult/deliverables/Z Products/Client Worksheet/Client_X_Worksheet.md`
- Deliverables: `PDCT_JO_Consult/deliverables/Z Products/Fulfillment/_CLIENT_DELIVERABLES/[CLIENT]/`
- Content workspace: `VLT_Content/02_WORKSPACE/[CLIENT]/`
- Onboarding form: `PDCT_JO_Consult/workflows/_JO_CONSULT/Forms/Form-1-Onboarding.md`
- Templates folder: `PDCT_JO_Consult/deliverables/Z Products/Fulfillment/_ONBOARDING/`

## Tools Used Per Phase

| Day | Tool | Command |
|-----|------|---------|
| 2 | Offer agent | `py -3 AI_Tools/offer_agent.py --from-file "_CLIENT_DELIVERABLES/[CLIENT]/onboarding.json"` |
| 9 | Repurpose | `py -3 AI_Tools/repurpose_content.py --batch "[scripts]" --client "[CLIENT]"` |
| 5 | Reel analyzer (content audit support) | `py -3 AI_Tools/analyze_viral_reel.py` |

## Contracts (attach to Day 0 welcome email)

Three documents required — client must sign and return before Onboarding Call:
1. `Perjanjian Legal.pdf` — main legal agreement
2. `Garansi Bersyarat.pdf` — conditional revenue guarantee
3. `Kebijakan Privasi.pdf` — privacy policy

Source: `PDCT_JO_Consult/deliverables/Z Products/Fulfillment/_ONBOARDING/contracts/`
