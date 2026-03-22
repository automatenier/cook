# JO Consult — Design System & Brand Guidelines
<!-- Agent reference: read this file before producing any HTML doc for JO Consult / Mathew Jordan -->

---

## Color Palette

| Token | Hex | Usage |
|-------|-----|-------|
| `--navy` | `#1B3A6E` | Primary — covers, headers, step numbers, CTAs, table headers, borders |
| `--navy-dark` | `#111827` | Code block backgrounds |
| `--navy-light` | `#f0f4ff` | Intro boxes, inline code bg, formula blocks |
| `--surface` | `#f8f9ff` | Card backgrounds, even table rows |
| `--page-bg` | `#f5f6fa` | Page background, footer |
| `--border` | `#dde2f5` | Card borders, dividers |
| `--divider` | `#eef0f8` | Subtle HR lines, table row borders |
| `--text-primary` | `#1a1a2e` | Headings, strong labels |
| `--text-body` | `#3a3a5c` | Body paragraphs, list items |
| `--text-muted` | `#6a6a8a` | Subtext, card descriptions |
| `--text-footer` | `#8a8aaa` | Footer text |
| `--white` | `#ffffff` | Page surface, CTA pill, table odd rows |
| `--code-green` | `#86efac` | AI output text in code blocks |
| `--code-blue` | `#93c5fd` | User prompt text in code blocks |
| `--code-label-blue` | `#3b82f6` | System block border + label color |
| `--code-label-green` | `#22c55e` | AI output label color |
| `--warning-bg` | `#fff8e6` | Callout/warning box bg |
| `--warning-border` | `#f5c842` | Callout/warning box border |
| `--warning-text` | `#5a4a00` | Callout/warning box text |

---

## Typography

- **Font**: `Inter` (Google Fonts) — weights 400, 500, 600, 700, 800
- **Monospace**: `'Courier New', monospace` — code blocks only
- **Import**: `@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');`

| Element | Size | Weight | Color |
|---------|------|--------|-------|
| Cover H1 | 34px | 800 | #fff |
| Cover subtitle | 15px | 400 | rgba(255,255,255,0.75) |
| Section label (H2) | 11px | 700 | `--navy`, uppercase, letter-spacing 2.5px |
| Card / step H3 | 18–19px | 700 | `--text-primary` |
| Body paragraph | 15px | 400 | `--text-body` |
| List item | 15px | 400 | `--text-body` |
| Table header | 13px | 600 | #fff |
| Table body | 14px | 400 | `--text-body` |
| Badge | 11px | 700 | #fff, uppercase, letter-spacing 2px |
| Code block | 13px | 400 | varies by type |
| Footer | 12px | 400 | `--text-footer` |

---

## Page Shell

```html
<body style="font-family: Inter; background: #f5f6fa; color: #1a1a2e; line-height: 1.7;">
  <div class="page"> <!-- max-width: 800px; margin: 40px auto; bg: #fff; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 32px rgba(0,0,0,0.10) -->
    <!-- COVER -->
    <!-- BODY -->
    <!-- FOOTER -->
  </div>
</body>
```

---

## Components

### 1. Cover
```css
.cover {
  background: #1B3A6E;
  padding: 56px 56px 48px;
  color: #fff;
}
```
Structure:
- `.badge` — pill with `rgba(255,255,255,0.15)` bg, `rgba(255,255,255,0.3)` border, text: "Lead Magnet · JO Consult"
- `h1` — 34px, weight 800
- `p` — 15px, `rgba(255,255,255,0.75)`, max-width 560px
- `.brand-line` — 12px, `rgba(255,255,255,0.5)`, uppercase, top border `rgba(255,255,255,0.2)`, margin-top 40px

### 2. Body Container
```css
.body { padding: 48px 56px; }
```

### 3. Intro Box (Callout — Branded)
```css
.intro-box {
  background: #f0f4ff;
  border-left: 4px solid #1B3A6E;
  padding: 20px 24px;
  border-radius: 0 8px 8px 0;
  margin-bottom: 40px;
  font-size: 15px;
  color: #2d3a5e;
  font-weight: 500;
}
```

### 4. Section Label (H2)
```css
h2 {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 2.5px;
  text-transform: uppercase;
  color: #1B3A6E;
  margin-top: 48px;
  margin-bottom: 16px;
}
```

### 5. Numbered Steps
```html
<div class="step"> <!-- display: flex; gap: 16px; align-items: flex-start; margin-bottom: 28px -->
  <div class="step-num">1</div> <!-- bg: #1B3A6E; color: #fff; 32x32; border-radius: 50%; font-size: 13px; font-weight: 700 -->
  <div class="step-content">
    <h3>Step Title</h3>
    <p>...</p>
  </div>
</div>
```

### 6. Code Block (Generic — Commands / JSON)
```css
.code-block {
  background: #111827;
  color: #e2e8f0;
  font-family: 'Courier New', monospace;
  font-size: 13px;
  padding: 20px 24px;
  border-radius: 8px;
  margin: 16px 0 24px;
  line-height: 1.6;
  white-space: pre;
  overflow-x: auto;
}
```

### 7. Prompt Blocks (User / AI pair)
```css
/* User prompt — blue left border */
.prompt-block.user-prompt {
  background: #111827;
  color: #93c5fd;
  border-left: 3px solid #3b82f6;
  font-family: 'Courier New', monospace;
  font-size: 13px;
  padding: 20px 24px;
  border-radius: 8px;
  line-height: 1.7;
  white-space: pre-wrap;
}

/* AI output — green left border */
.prompt-block.ai-output {
  background: #111827;
  color: #86efac;
  border-left: 3px solid #22c55e;
  /* same as above */
}

/* Labels above prompt blocks */
.prompt-label.user { color: #3b82f6; font-size: 10px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; font-family: 'Courier New', monospace; }
.prompt-label.ai   { color: #22c55e; /* same */ }
```

### 8. System Briefing Block
```css
.system-block {
  background: #0f1923;
  color: #e2e8f0;
  font-family: 'Courier New', monospace;
  font-size: 13px;
  padding: 24px 28px;
  border-radius: 8px;
  border-left: 3px solid #3b82f6;
  line-height: 1.8;
  white-space: pre-wrap;
}
.system-block .block-label {
  font-size: 10px; font-weight: 700; letter-spacing: 2px;
  text-transform: uppercase; color: #3b82f6;
  margin-bottom: 12px; display: block;
}
```

### 9. Inline Code
```css
.code-inline {
  background: #f0f4ff;
  color: #1B3A6E;
  font-family: 'Courier New', monospace;
  font-size: 13px;
  padding: 2px 7px;
  border-radius: 4px;
}
```

### 10. Formula / Palette Block
```css
.formula-box {
  background: #f0f4ff;
  border: 1px solid #c5d0f0;
  border-radius: 8px;
  padding: 16px 20px;
  font-family: 'Courier New', monospace;
  font-size: 13px;
  color: #1B3A6E;
}
```

### 11. Table
```css
table { width: 100%; border-collapse: collapse; font-size: 14px; margin: 20px 0 28px; }
thead tr { background: #1B3A6E; color: #fff; }
thead th { padding: 12px 16px; text-align: left; font-weight: 600; font-size: 13px; }
tbody tr:nth-child(even) { background: #f8f9ff; }
tbody tr:nth-child(odd)  { background: #fff; }
tbody td { padding: 11px 16px; color: #3a3a5c; border-bottom: 1px solid #eef0f8; }
```

### 12. Use Case / Feature Cards (2-column grid)
```css
.use-case-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin: 20px 0 28px; }
.use-case-card {
  background: #f8f9ff;
  border: 1px solid #dde2f5;
  border-radius: 8px;
  padding: 18px 20px;
}
.use-case-card .num { font-size: 11px; font-weight: 700; letter-spacing: 1.5px; color: #1B3A6E; text-transform: uppercase; margin-bottom: 6px; }
.use-case-card h4 { font-size: 15px; font-weight: 700; color: #1a1a2e; margin-bottom: 4px; }
.use-case-card p  { font-size: 13px; color: #6a6a8a; margin: 0; }
```
Full-width card: `style="grid-column: 1 / -1;"`

### 13. Scenario Card (header + body)
```css
.scenario { border: 1px solid #dde2f5; border-radius: 10px; overflow: hidden; margin-bottom: 32px; }
.scenario-header {
  background: #1B3A6E; color: #fff;
  padding: 14px 20px; font-size: 13px; font-weight: 700;
  display: flex; align-items: center; gap: 10px;
}
.scenario-num {
  background: rgba(255,255,255,0.2); width: 24px; height: 24px;
  border-radius: 50%; display: flex; align-items: center;
  justify-content: center; font-size: 12px; font-weight: 800;
}
.scenario-body { padding: 20px 24px; }
```

### 14. Flow List
```css
.flow { background: #f8f9ff; border: 1px solid #dde2f5; border-radius: 10px; padding: 24px 28px; font-size: 14px; }
.flow-step { display: flex; align-items: flex-start; gap: 12px; margin-bottom: 12px; }
.flow-dot  { width: 8px; height: 8px; background: #1B3A6E; border-radius: 50%; flex-shrink: 0; margin-top: 7px; }
```

### 15. Warning / Callout Box
```css
.callout {
  background: #fff8e6;
  border: 1px solid #f5c842;
  border-radius: 8px;
  padding: 16px 20px;
  font-size: 14px;
  color: #5a4a00;
}
```

### 16. Divider
```css
hr { border: none; border-top: 1px solid #eef0f8; margin: 40px 0; }
```

### 17. CTA Box (Bottom of every doc)
```css
.cta-box {
  background: #1B3A6E;
  color: #fff;
  padding: 36px 40px;
  border-radius: 10px;
  margin-top: 48px;
  text-align: center;
}
.cta-box h3 { color: #fff; font-size: 20px; margin-bottom: 10px; }
.cta-box p  { color: rgba(255,255,255,0.75); font-size: 14px; margin-bottom: 20px; }
.cta-pill {
  display: inline-block;
  background: #fff;
  color: #1B3A6E;
  font-weight: 700;
  font-size: 14px;
  padding: 12px 28px;
  border-radius: 30px;
  letter-spacing: 0.5px;
}
```

### 18. Footer
```css
.footer {
  text-align: center;
  padding: 24px 56px;
  background: #f5f6fa;
  font-size: 12px;
  color: #8a8aaa;
  border-top: 1px solid #eef0f8;
}
```
Content: `JO Consult × Mathew Jordan &nbsp;·&nbsp; Bedah Digital Program &nbsp;·&nbsp; 2026`

---

## Document Structure (Standard Order)

```
1. Cover          — badge, H1, subtitle, brand-line
2. Body
   a. intro-box   — one-liner problem/hook
   b. Section     — H2 label → content
   c. HR          — between major sections
   d. ...repeat
   e. CTA box     — always last inside body
3. Footer
```

---

## Writing Rules (Tone)

- Language: **Bahasa Indonesia informal** (lo/gue)
- No fluff, no "sebagai kesimpulan" closers
- Every section starts with the problem, not the solution
- CTAs always use a keyword in quotes: DM **"KEYWORD"**
- Limitation sections are mandatory — build trust, don't hide weaknesses
- Step numbers are visual (circle) not just text

---

## Naming Convention

| File | Pattern |
|------|---------|
| Lead magnet HTML | `0N_guide_[topic].html` |
| Lead magnet draft | `0N_guide_[topic].md` |
| Brand guidelines | `0_Brand_Guidelines/` |
| Design system (this file) | `design_system.md` |

---

## Quick Reference: When to Use Which Component

| I need to... | Use |
|---|---|
| Show a step-by-step process | Numbered Steps (#5) |
| Show a code command | Code Block (#6) |
| Show a Claude prompt | Prompt Block user-prompt (#7) |
| Show Claude's output | Prompt Block ai-output (#7) |
| Show a system briefing template | System Block (#8) |
| Show a formula or fill-in-the-blank | Formula Box (#10) |
| Compare options | Table (#11) |
| List features in a grid | Use Case Cards (#12) |
| Show a DM scenario with prompt+output | Scenario Card (#13) |
| Show a linear flow / funnel | Flow List (#14) |
| Warn about a limitation | Callout Box (#15) |
| End every document | CTA Box (#17) |
