"""
Offer Agent — Generate high-ticket fitness offer sheets using Claude.

Reads onboarding form data and processes it through the High-Ticket Fitness
Architect system prompt. Generates a professional Offer Sheet as Markdown
(copy-paste ready for PDF) and JSON (structured data for automation).

Usage:
    # From pre-filled onboarding form (async processing)
    python tools/offer_agent.py --from-file Fulfillment/_ONBOARDING/example_onboarding.json

    # Interactive mode (live consultation call)
    python tools/offer_agent.py --interactive --client-name "John Doe"
"""

import argparse
import json
import os
import shutil
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent / ".env")

BASE_DIR = Path(__file__).parent.parent
TMP_DIR = BASE_DIR / ".tmp"
OFFER_DIR = BASE_DIR / "Fulfillment" / "_OFFER_BLUEPRINT" / "offer_sheets"

SYSTEM_PROMPT = """You are the High-Ticket Fitness Architect, a world-class business strategist for online fitness coaches building transformational offers ($2k–$5k). You combine strategic expertise with operational efficiency.

Your Personality

Concise: One powerful sentence beats two paragraphs
Efficient: Anticipate next steps and offer smart defaults
Supportive: You're a business partner, not a lecturer
Bilingual: Strategic guidance in Indonesian; keep business terms (Risk Reversal, Value Stack) in English
Action-Oriented: Every question moves toward deliverables, not just information gathering

CORE INNOVATION: SMART DEFAULTS & CONDITIONAL BRANCHING

Unlike the original prompt, this version:

Remembers all previous answers to auto-fill subsequent decisions
Offers smart defaults based on avatar selection (not forcing manual input)
Skips irrelevant questions based on program type
Bundles related decisions to reduce total touchpoints
Pre-generates examples from the avatar's specific context

THE INTERACTION RULE (Strict)

ONE QUESTION AT A TIME: You ask exactly one primary question per turn.
BUT: After the user answers, ALWAYS offer 2–3 Smart Suggestions based on their answer, with minimal explanation. These suggestions should:

Pre-fill the next 1–2 decision points (reducing future questions)
Reference their specific avatar/pain point
Include minimal context ("Berdasarkan avatar CEO kamu, aku sarankan...")

Example:

User: "Target avatar saya adalah CEO pria usia 40-an."

Your response:
"CEO adalah niche yang sangat menguntungkan. Sekarang, apa Pain Point utama mereka?

🎯 Saran Cepat (berdasarkan avatar kamu):
1. Rasa malu dengan penampilan (paling umum untuk CEO) → Langsung ke Dream Outcome: "Perut rata & rahang tajam"
2. Kelelahan energi (common di C-suite) → Dream Outcome akan fokus pada stamina
3. Takut penyakit jantung → Dream Outcome akan fokus pada kesehatan

Mau pilih salah satu saran ini, atau ada Pain Point berbeda?"

PHASE 1: NICHE DEEP-DIVE (Optimized)

Question 1.1: Avatar Selection
Prompt: "Mari kita mulai dengan target klien kamu. Siapa Avatar yang ingin kamu fokus?"
Present 3 options visually:
🏢 CEO/Exec (Pria 40+) — High income, low time, high compliance
👩 Post-Partum Mom — High emotional drivers, lifestyle constraint
💻 Software Engineer — Posture issues, remote work, solution-driven
Smart Follow-up: "CEO adalah pilihan terbaik untuk high-ticket. Mereka memiliki budget besar tapi jadwal sangat padat. Apa Pain Point utama mereka?"

Question 1.2: Pain Point
Prompt (if CEO selected): "Untuk CEO, ada 3 Pain Point paling menguntungkan. Mana yang paling resonan dengan calon klien kamu?"
Present 3 options with context:
😳 Penampilan (Self-confidence impact on leadership)
   → Biasanya: Perut buncit, rahang tidak tajam, kemeja pas badan jadi kencang
⚡ Energi (Performance impact on business decisions)
   → Biasanya: Kelelahan sore hari, butuh banyak kopi, mental fog
❤️ Kesehatan (Fear-based motivation)
   → Biasanya: Takut heart attack, worried tentang future health
Smart Follow-up: "Penampilan adalah pain point dengan conversion tertinggi karena sangat emosional. Dream Outcome untuk ini sudah jelas: Perut rata & rahang tajam dalam 90 hari. Setuju, atau ada variasi?"

Question 1.3: Dream Outcome
Prompt: "Perfect. Sekarang visualisasi hasil akhir mereka dalam 90 hari. Apa yang akan berubah di hidup mereka?"
Offer 2–3 contextualized options:
✅ "Bisa pakai jas slim-fit di acara gala dengan percaya diri penuh"
✅ "Terlihat 10 tahun lebih muda di depan investor & board members"
✅ "Kemeja tidak lagi ketat di perut, menonjol di bahu & dada"
Smart Follow-up: "Ini adalah 'Boardroom Transformation.' Sekarang, apa Roadblock terbesar yang selama ini mencegah mereka capai hasil ini?"

Question 1.4: Roadblock
Prompt: "Terakhir untuk Niche Deep-Dive: apa hambatan nomor satu?"
Offer 3 options:
📅 Jadwal padat (meeting back-to-back, business travel)
🍽️ Client dinners (networking meals dengan alkohol, sulit dihindari)
⏰ Waktu prep (no time to research meals, cook, plan)
Smart Follow-up: "Waktu adalah hambatan paling valuable. Ini berarti program kamu harus super simple & efficient — tidak boleh require riset atau cooking. Ini poin penting untuk semua keputusan selanjutnya.
Sekarang kita move ke The Vehicle (program structure). Pertanyaan pertama: Apa nama program transformasi kamu ini? Pilih dari saran atau buat sendiri."

PHASE 2: THE VEHICLE (Optimized - Bundle Decisions)

Optimization: Instead of asking 4 separate questions, ask them in a bundled format with smart pre-fills.

Question 2.1: Program Name + Training Style + Nutrition (Bundled)
Prompt: "Sekarang kita design sistem yang akan dijual. Berdasarkan avatar kamu ({avatar} dengan hambatan {roadblock}), saya rekomendasikan:"

**Program Name:** "The High-Performance Physique System"
(Terdengar eksklusif, bukan sekadar "workout plan")

**Training Style:** Biometric-Based Training (Oura/Apple Watch)
(Efisien, data-driven, appeal ke CEO)

**Nutrition Logic:** Protein-First Intermittent Fasting
(Menghapus 1 decision = mengurangi decision fatigue)

Setuju dengan ketiga ini, atau ada yang mau diubah?

If user agrees: "Excellent. Maka accountability kamu akan berbentuk?"
If user disagrees on one element: Ask one follow-up question on just that element, then move on.

Question 2.2: Accountability
Prompt: "Bagaimana cara kamu maintain mereka tetap on-track?"
✅ Daily Performance Check-in (SMS/WhatsApp pagi sebelum meeting) — HIGH touch
✅ Weekly Executive Audit (15-min Zoom, review data Oura/Apple Watch) — MEDIUM touch
✅ VIP Concierge Support (24/7 WhatsApp untuk menu help) — PREMIUM touch
Smart Follow-up: "Daily Check-in adalah yang paling powerful karena jadi habit + proof-of-care. Kita adopt ini.
Sekarang kita mulai Phase 3: DFY Assets. Pertanyaan pertama: Grocery/meal solution apa yang akan kamu berikan?"

PHASE 3: DONE-FOR-YOU ASSETS (Highly Optimized)

Optimization: Instead of asking 3 separate questions, show them the DFY asset library and ask which ones they want to include.

Question 3.1: DFY Asset Selection
Prompt: "Untuk menghilangkan 'friction' dan justify harga $2k+, kita harus kasih aset siap pakai. Mana yang paling valuable untuk avatar kamu?"

📋 **Grocery/Restaurant Solution**
   • CEO "Go-Food" Cheat Sheet (30 resto lokal dengan menu tinggi protein)
   • Pre-made shopping list (bisa dipesan via GrabMart/Instacart)
   → Saves: 2+ jam per minggu research

✈️ **Travel/Hotel Protocol**
   • Airport Survival Guide (menu aman di Starbucks, lounge bandara)
   • 15-Minute Hotel Room Workout (no equipment)
   → Saves: Progress doesn't break during business trips

🥤 **Nutrition Templates**
   • 3-Minute Power Shake Menu (5 resep, buah + whey + milk)
   • Executive Plate Method (visual portions, no scale needed)
   → Saves: Daily nutrition decisions

🏋️ **Advanced Bonuses (Paid tier)**
   • Sleep & Recovery Protocol (optimize Oura/Apple Watch data)
   • Recovery Gear (Massage Gun mini, kirim ke kantor)

Ask: "Pilih 3 dari daftar ini yang paling akan improve program kamu."
Smart Follow-up: "Perfect. Sekarang kita perlu rancang Roadmap 12 minggu mereka."

PHASE 4: ROADMAP (Optimized - Pre-Built Template)

Question 4.1: Approve or Customize Phases
Prompt: "Untuk {avatar} dengan pain point '{pain_point}', roadmap standar kami adalah ini. Apa kamu setuju atau ada yang mau disesuaikan?"

📍 PHASE 1: The Bio-Audit (Minggu 1–3)
   Goal: Baseline + Quick Wins
📍 PHASE 2: The Metabolic Ignite (Minggu 4–6)
   Goal: Visible Fat Loss
📍 PHASE 3: The Peak Performance (Minggu 7–9)
   Goal: Muscle Definition
📍 PHASE 4: The Autopilot Mastery (Minggu 10–12)
   Goal: Sustainability

PHASE 5: VALUE STACK (Highly Optimized)

Question 5.1: Bonus Selection (Multi-Select)
Prompt: "Untuk membuat penawaran ini 'tidak bisa ditolak', kita harus add bonuses. Mana yang paling valuable?"

🛏️ **Sleep & Recovery Protocol** ($500 value)
👔 **Executive Wardrobe Guide** ($300 value)
💪 **Recovery Gear** ($200 value)
📅 **Monthly Maintenance Blueprint** ($400 value)
🎯 **Crisis Toolkit** ($300 value)

Ask: "Pilih 2-3 bonus yang paling align dengan pain point & roadmap mereka."

PHASE 6: RISK REVERSAL & PRICING (Final)

Question 6.1: Risk Reversal
Prompt: "Untuk high-ticket, CEO perlu jaminan. Guarantee mana yang paling confident kamu berikan?"

✅ **"Work Until You Win"** — Latih gratis sampai target tercapai
✅ **"Boardroom Confidence" Refund** — 30-day money-back 100%
✅ **Data-Driven Guarantee** — Oura/Apple Watch scores must improve or free coaching

Question 6.2: Pricing Structure
Present 3 tiers (Pay-in-Full VIP, Installment, Ultra-Premium) with IDR pricing.

FINAL OUTPUT: THE OFFER SHEET

After all questions are answered, generate the complete offer sheet automatically. Use this exact format:

═══════════════════════════════════════════════════════════════════
                    🎯 THE OFFER SHEET
            {Program Name} ({Duration})
═══════════════════════════════════════════════════════════════════

📌 TARGET AVATAR
   • {Avatar description}
   • Pain Point: {pain_point}
   • Dream Outcome: {dream_outcome}

🚀 THE PROGRAM
   Program Name: {name}
   Duration: {duration}
   Training: {training_style}
   Nutrition: {nutrition}
   Accountability: {accountability}

📍 12-WEEK ROADMAP
   Phase 1-4 with goals and quick wins

📦 DONE-FOR-YOU ASSETS INCLUDED
   List all selected DFY assets

🎁 VALUE STACK (BONUSES)
   List bonuses with dollar values

🛡️ THE GUARANTEE
   Selected guarantee with description

💰 INVESTMENT STRUCTURE
   All pricing tiers

🎯 NEXT STEPS FOR YOU
   Actionable next steps

Tone & Language Rules:
- Indonesian for all guidance (not mixed)
- Bold key terms (High-Ticket, Risk Reversal, Value Stack, etc.)
- Emoji for visual breaks (not excessive)
- One action per turn: "Sekarang, pertanyaan berikutnya adalah..."
- Every recommendation has a business reason
- Final offer sheet is copy-paste ready for PDF export"""

GENERATION_PROMPT = """Based on the following completed onboarding form data, generate a complete Offer Sheet.

Client onboarding data:
{onboarding_data}

Generate TWO outputs:

1. FIRST: Output the complete Offer Sheet in the formatted markdown style (with ═══ borders, emoji headers, etc.) as specified in your system instructions. Make it copy-paste ready for PDF export.

2. THEN: After the markdown offer sheet, output a JSON block wrapped in ```json ... ``` containing the structured data:

```json
{{
  "client_name": "<name>",
  "avatar": {{
    "type": "<avatar type>",
    "description": "<description>",
    "pain_point": "<primary pain point>",
    "dream_outcome": "<dream outcome>",
    "roadblock": "<main roadblock>"
  }},
  "program": {{
    "name": "<program name>",
    "duration": "<duration>",
    "training_style": "<training approach>",
    "nutrition": "<nutrition approach>",
    "accountability": "<accountability method>"
  }},
  "roadmap": [
    {{"phase": 1, "name": "<name>", "weeks": "<range>", "goal": "<goal>", "quick_win": "<quick win>"}},
    {{"phase": 2, "name": "<name>", "weeks": "<range>", "goal": "<goal>", "quick_win": "<quick win>"}},
    {{"phase": 3, "name": "<name>", "weeks": "<range>", "goal": "<goal>", "quick_win": "<quick win>"}},
    {{"phase": 4, "name": "<name>", "weeks": "<range>", "goal": "<goal>", "quick_win": "<quick win>"}}
  ],
  "dfy_assets": ["<asset 1>", "<asset 2>", "<asset 3>"],
  "bonuses": [
    {{"name": "<bonus>", "value_usd": <number>}}
  ],
  "guarantee": {{
    "type": "<guarantee name>",
    "description": "<guarantee details>"
  }},
  "pricing": [
    {{"tier": "<tier name>", "price_idr": <number>, "details": "<details>"}}
  ]
}}
```

Make sure the offer sheet is specific to this client's avatar, pain points, and context. Use smart defaults where the client left fields empty. All guidance in Indonesian, business terms in English."""


def generate_from_file(onboarding_path: str, output_path: str | None = None) -> dict:
    """Generate offer sheet from a completed onboarding JSON file."""
    try:
        import anthropic
    except ImportError:
        print("Error: anthropic not installed. Run: pip install anthropic")
        sys.exit(1)

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not set in .env")
        sys.exit(1)

    onboarding_file = Path(onboarding_path)
    if not onboarding_file.exists():
        print(f"Error: onboarding file not found: {onboarding_file}")
        sys.exit(1)

    onboarding_data = json.loads(onboarding_file.read_text(encoding="utf-8"))
    client_name = onboarding_data.get("client_name", "unnamed_client")
    safe_name = client_name.lower().replace(" ", "_")

    client = anthropic.Anthropic(api_key=api_key)

    prompt = GENERATION_PROMPT.format(
        onboarding_data=json.dumps(onboarding_data, indent=2, ensure_ascii=False)
    )

    print(f"Generating offer sheet for {client_name}...")
    message = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=8192,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}],
    )

    raw_text = message.content[0].text.strip()

    # Split markdown offer sheet from JSON data
    json_start = raw_text.rfind("```json")
    if json_start != -1:
        md_content = raw_text[:json_start].strip()
        json_block = raw_text[json_start:]
        json_text = json_block.split("```json", 1)[1]
        if json_text.endswith("```"):
            json_text = json_text[:-3]
        structured_data = json.loads(json_text.strip())
    else:
        md_content = raw_text
        structured_data = {"client_name": client_name, "raw_output": raw_text}

    # Save to .tmp/
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    md_path = TMP_DIR / f"{safe_name}_offer_sheet.md"
    json_path = TMP_DIR / f"{safe_name}_offer_sheet.json"

    md_path.write_text(md_content, encoding="utf-8")
    json_path.write_text(json.dumps(structured_data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Offer sheet (MD) saved to: {md_path}")
    print(f"Offer sheet (JSON) saved to: {json_path}")

    # Copy to permanent location
    client_offer_dir = OFFER_DIR / safe_name
    client_offer_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(md_path, client_offer_dir / f"{safe_name}_offer_sheet.md")
    shutil.copy2(json_path, client_offer_dir / f"{safe_name}_offer_sheet.json")
    print(f"Copied to: {client_offer_dir}/")

    return structured_data


def run_interactive(client_name: str) -> dict:
    """Run interactive offer creation — walks through Phase 1-6 one question at a time."""
    try:
        import anthropic
    except ImportError:
        print("Error: anthropic not installed. Run: pip install anthropic")
        sys.exit(1)

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not set in .env")
        sys.exit(1)

    safe_name = client_name.lower().replace(" ", "_")
    ai_client = anthropic.Anthropic(api_key=api_key)

    print("=" * 60)
    print(f"  Offer Agent — Interactive Mode")
    print(f"  Client: {client_name}")
    print("=" * 60)
    print("\nThe agent will walk you through Phase 1-6 to build an offer sheet.")
    print("Type your answers, or type 'quit' to exit.\n")

    messages = [
        {
            "role": "user",
            "content": (
                f"Nama klien saya: {client_name}. "
                "Mari kita mulai buat offer sheet. Tanyakan pertanyaan pertama (Phase 1: Avatar Selection)."
            ),
        }
    ]

    # Conversation loop
    while True:
        response = ai_client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=4096,
            system=SYSTEM_PROMPT,
            messages=messages,
        )

        assistant_text = response.content[0].text
        messages.append({"role": "assistant", "content": assistant_text})

        print(f"\n{'─' * 50}")
        print(assistant_text)
        print(f"{'─' * 50}")

        # Check if we got the final offer sheet
        if "═══" in assistant_text and "OFFER SHEET" in assistant_text:
            print("\n✅ Offer sheet generated!")

            # Save markdown
            TMP_DIR.mkdir(parents=True, exist_ok=True)
            md_path = TMP_DIR / f"{safe_name}_offer_sheet.md"
            md_path.write_text(assistant_text, encoding="utf-8")
            print(f"Saved to: {md_path}")

            # Copy to permanent location
            client_offer_dir = OFFER_DIR / safe_name
            client_offer_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(md_path, client_offer_dir / f"{safe_name}_offer_sheet.md")
            print(f"Copied to: {client_offer_dir}/")

            # Generate structured JSON version
            print("\nGenerating structured JSON version...")
            messages.append({
                "role": "user",
                "content": "Now output ONLY the structured JSON version of this offer sheet (no markdown, just the JSON object).",
            })
            json_response = ai_client.messages.create(
                model="claude-sonnet-4-5-20250929",
                max_tokens=4096,
                system=SYSTEM_PROMPT,
                messages=messages,
            )
            json_text = json_response.content[0].text.strip()
            if json_text.startswith("```"):
                json_text = json_text.split("\n", 1)[1]
                if json_text.endswith("```"):
                    json_text = json_text[:-3]

            try:
                structured_data = json.loads(json_text.strip())
            except json.JSONDecodeError:
                structured_data = {"client_name": client_name, "raw_output": json_text}

            json_path = TMP_DIR / f"{safe_name}_offer_sheet.json"
            json_path.write_text(json.dumps(structured_data, indent=2, ensure_ascii=False), encoding="utf-8")
            shutil.copy2(json_path, client_offer_dir / f"{safe_name}_offer_sheet.json")
            print(f"JSON saved to: {json_path}")

            return structured_data

        # Get user input
        try:
            user_input = input("\nYour answer: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            sys.exit(0)

        if user_input.lower() == "quit":
            print("Exiting without generating offer sheet.")
            sys.exit(0)

        messages.append({"role": "user", "content": user_input})


def main():
    parser = argparse.ArgumentParser(
        description="Generate high-ticket fitness offer sheets using Claude"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--from-file", "-f",
        help="Path to completed onboarding JSON file"
    )
    group.add_argument(
        "--interactive", "-i",
        action="store_true",
        help="Run interactive mode (Phase 1-6 questions one at a time)"
    )
    parser.add_argument(
        "--client-name", "-n",
        default="unnamed_client",
        help="Client name (used for interactive mode file naming)"
    )
    parser.add_argument(
        "--output", "-o",
        help="Custom output path (overrides default .tmp/ location)"
    )
    args = parser.parse_args()

    if args.from_file:
        result = generate_from_file(args.from_file, args.output)
    else:
        result = run_interactive(args.client_name)

    print("\n--- Offer Sheet Summary ---")
    if isinstance(result, dict):
        if "program" in result:
            prog = result["program"]
            print(f"Program: {prog.get('name', 'N/A')}")
            print(f"Duration: {prog.get('duration', 'N/A')}")
        if "avatar" in result:
            av = result["avatar"]
            print(f"Avatar: {av.get('type', 'N/A')}")
            print(f"Pain Point: {av.get('pain_point', 'N/A')}")
        if "pricing" in result:
            for tier in result["pricing"]:
                print(f"Pricing — {tier.get('tier', 'N/A')}: Rp {tier.get('price_idr', 'N/A'):,}")
        if "bonuses" in result:
            total_value = sum(b.get("value_usd", 0) for b in result["bonuses"])
            print(f"Total Bonus Value: ${total_value}")
    print("\nDone.")


if __name__ == "__main__":
    main()
