# RE — Follow-Up Scripts
> Use these AFTER initial contact. Track all follow-ups in pipeline tracker.

---

## FOLLOW-UP SEQUENCE — No Response

### Follow-Up #1 (Day 3 — soft nudge)
```
Hei [Nama]! Follow up singkat dari pesan kemarin soal unit di [area].

Unit ini masih available, tapi biasanya tipe kayak gini nggak lama. Kalau mau lihat lebih detail, saya bisa atur viewing minggu ini — fleksibel waktunya.

Gimana?
```

### Follow-Up #2 (Day 7 — urgency + value)
```
Hei [Nama]! Ada update soal unit di [area] yang saya info-kan sebelumnya — sudah ada 1 orang yang minta viewing jadwal minggu ini.

Kalau masih tertarik, saya prioritasin kamu duluan sebelum dipasarkan lebih luas. Kapan bisa 30 menit untuk lihat lokasinya?
```

### Follow-Up #3 (Day 14 — final, no pressure)
```
Hei [Nama], terakhir dari saya soal properti ini.

Kalau memang lagi fokus hal lain dulu, no problem — saya simpan kontaknya. Kalau nanti ada yang pas di [area] atau area lain, saya langsung kabarin.

Semoga semua lancar ya!
```

> Setelah Follow-Up #3 tanpa respons → update status ke `ghost` di tracker. Pindah ke monthly touchpoint (1x/bulan max).

---

## FOLLOW-UP SEQUENCE — Warm Lead (pernah reply, lalu menghilang)

### Re-engage #1 (sudah 1 minggu tidak aktif)
```
Hei [Nama]! Gimana, masih aktif cari properti di [area]?

Ada beberapa listing baru masuk minggu ini yang mungkin lebih cocok dari yang kemarin. Boleh saya share 2-3 pilihan?
```

### Re-engage #2 (setelah 2 minggu)
```
Hei [Nama]! Ada unit baru di [area] yang baru dipasarkan hari ini — harga masih pre-launch. Tipe ini biasanya habis dalam 1-2 minggu.

Masih relevan buat kamu?
```

---

## FOLLOW-UP — Post Qualification (sudah tau budget/kebutuhan, belum booking)

```
Hei [Nama]! Saya udah filter beberapa pilihan sesuai kriteria yang kamu kasih kemarin:
- Budget: [range]
- Area: [lokasi]
- Tipe: [landed/apartemen/dll]

Ada [X] unit yang cukup match. Mau saya kirim summary singkatnya? Bisa lewat WhatsApp atau kita langsung set jadwal viewing kalau ada yang menarik.
```

---

## FOLLOW-UP — Setelah Mengirim Info/Listing

```
Hei [Nama]! Udah sempat lihat info unit [nama/area] yang saya kirim?

Ada pertanyaan atau mau lihat foto/video lebih lengkap? Saya juga bisa arrange virtual tour dulu kalau belum bisa hadir langsung.
```

---

## MONTHLY TOUCHPOINT — Cold Leads (1x/bulan)

```
Hei [Nama]! Jordan di sini.

Pasar properti di [area] lagi interesting bulan ini — ada beberapa listing baru dengan harga yang lebih kompetitif. Kalau kamu atau kenalan masih cari unit, happy to help.

Kabarnya gimana?
```

---

## RULES

- Follow-Up #1: kirim hari ke-3
- Follow-Up #2: kirim hari ke-7
- Follow-Up #3: kirim hari ke-14
- Setelah FU #3 tanpa respons: monthly touchpoint saja
- Selalu update status di tracker setelah setiap follow-up
- Log tiap status change: `py -3 24_Tools/log_lead.py --name "[Name]" --source "[source]" --vertical re --status [new_status]`
