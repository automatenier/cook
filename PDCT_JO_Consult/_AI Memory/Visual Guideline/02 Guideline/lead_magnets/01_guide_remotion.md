---
title: "Bikin Reel Otomatis Pakai Remotion — Panduan untuk Online Coach"
type: lead_magnet
status: draft
created: 2026-02-28
---

# Bikin Reel Otomatis Pakai Remotion
### Panduan Lengkap untuk Online Coach yang Mau Scale Konten Tanpa Edit Manual

---

## Apa itu Remotion?

Remotion adalah tool yang bikin lo bisa **render video pakai kode** — bukan edit manual di CapCut atau Premiere. Lo nulis template sekali, lalu sistem yang generate ratusan video dari data yang lo kasih.

Untuk coach, artinya:
- Lo nggak perlu duduk edit tiap reel satu per satu
- Tim lo bisa produce 30 reel sebulan dari 1 template
- Perubahan visual? Ganti di satu file, semua video auto-update

---

## Kenapa Coach Harus Tau Ini?

Kebanyakan coach stuck di sini:
> "Gue mau konsisten posting tapi nggak ada waktu edit, dan kalau hire editor mahal."

Remotion solve masalah itu. Lo build template sekali (atau pakai yang sudah jadi), lalu masukkan script teks → video jadi otomatis.

---

## Yang Lo Butuhkan Sebelum Mulai

- Node.js terinstall di laptop (gratis, download di nodejs.org)
- VS Code atau text editor apapun
- Script reel yang sudah jadi (teks hook + isi + CTA)
- Waktu setup awal: ~2 jam

---

## Step-by-Step: Setup Remotion Pertama Kali

### Step 1 — Install Remotion

Buka terminal / command prompt, ketik:

```bash
npx create-video@latest
```

Pilih template **"Blank"** untuk mulai dari nol, atau minta template yang sudah jadi dari tim lo.

### Step 2 — Pahami Struktur Project

```
remotion-project/
├── src/
│   ├── Root.tsx          ← daftar semua video template
│   ├── Reel.tsx          ← template visual reel lo
│   └── index.ts
├── public/               ← taruh background video / gambar di sini
└── package.json
```

Yang paling penting: **`Reel.tsx`** — ini template visual yang akan dipakai untuk semua reel lo.

### Step 3 — Buat Template Reel Sederhana

Contoh template text-over-video (paling umum untuk coach content):

```tsx
// src/Reel.tsx
import { AbsoluteFill, useCurrentFrame, interpolate } from 'remotion';

export const Reel = ({ hook, body, cta }: {
  hook: string;
  body: string;
  cta: string;
}) => {
  const frame = useCurrentFrame();

  const opacity = interpolate(frame, [0, 20], [0, 1]);

  return (
    <AbsoluteFill style={{ backgroundColor: '#000', padding: 60 }}>
      <p style={{
        color: 'white',
        fontSize: 52,
        fontWeight: 'bold',
        opacity,
        lineHeight: 1.3
      }}>
        {hook}
      </p>
    </AbsoluteFill>
  );
};
```

### Step 4 — Masukkan Script Lo

Di file `Root.tsx`, lo define durasi dan props:

```tsx
<Composition
  id="Reel"
  component={Reel}
  durationInFrames={450}   // 15 detik di 30fps
  fps={30}
  width={1080}
  height={1920}
  defaultProps={{
    hook: "3 kesalahan coach yang bikin klien kabur",
    body: "Lo mungkin lakuin ini tanpa sadar...",
    cta: "Comment 'SCRIPT' untuk template DM gratis"
  }}
/>
```

### Step 5 — Preview di Browser

```bash
npm run preview
```

Buka `localhost:3000` — lo bisa lihat video lo real-time sambil edit teks.

### Step 6 — Render Jadi Video

```bash
npx remotion render Reel out/reel-01.mp4
```

Video MP4 siap upload ke IG/TikTok.

---

## Workflow yang Efisien: Batch Render dari Data

Ini yang bikin Remotion beda dari edit manual. Lo bisa render 30 video sekaligus dari spreadsheet:

**1. Buat file `scripts.json`:**
```json
[
  { "hook": "3 kesalahan coach baru", "body": "...", "cta": "..." },
  { "hook": "Kenapa klien lo ghosting", "body": "...", "cta": "..." },
  { "hook": "Formula DM yang closing", "body": "...", "cta": "..." }
]
```

**2. Loop render dengan script Node.js:**
```bash
node render-batch.js
```

Hasilnya: 30 file MP4 siap upload, dikerjain sistem, bukan lo.

---

## Template yang Sudah Terbukti untuk Coach

| Template | Kapan Dipakai | Durasi |
|----------|--------------|--------|
| **Text Only (Bold)** | Hook kuat, statement | 7–10 detik |
| **Text Over B-Roll** | Tips / value content | 15–30 detik |
| **Split Screen** | Before/after, perbandingan | 15–20 detik |
| **Talking Head + Caption** | Personal / authentic | 30–60 detik |

---

## Batasan yang Perlu Lo Tau

- Remotion butuh sedikit comfort dengan kode — kalau belum pernah coding sama sekali, ada learning curve ~1 minggu
- Render butuh laptop yang cukup kuat (atau pakai cloud rendering)
- Template awal butuh effort setup — tapi setelah jadi, sistem yang kerja

---

## Langkah Selanjutnya

Mau sistem ini jalan fully otomatis — dari script text ke video siap upload, tanpa lo harus render manual?

Itu yang kami bangun untuk klien Bedah Digital: Remotion template + n8n automation + Telegram approval flow.

**DM "SISTEM" ke [Instagram handle] untuk lihat bagaimana sistem ini bekerja.**

---

*Lead Magnet — JO Consult × Mathew Jordan*
