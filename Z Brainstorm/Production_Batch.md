# Content Production Batch
**Goal:** List your raw videos and the hooks you want to test. I will bulk render them using the calibrated safe-zone settings.

| ID  | Video Path                                                | Hook (Title)                                                                                                                                    | Slug                 | Status |
| --- | --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ------ |
| 01  | C:\Users\natha\OneDrive - Bina Nusantara\Cook\test123.mov | CBD Deltamas: harga properti<br>yang belum reflect <br>value sebenernya.                                                                        | cbd-deltamas-value   | Done   |
| 02  | C:\Users\natha\OneDrive - Bina Nusantara\Cook\test123.mov | 300 hektar lahan yang khusus dialokasikan untuk Data Center Park<br>salah satu yang <br>terbesar di Asia Tenggara.                              | data-center-park     | Done   |
| 03  | C:\Users\natha\OneDrive - Bina Nusantara\Cook\test123.mov | Cluster landed 2BR & 3BR dengan Smart Home by Panasonic rancangan Jepang, dibangun untuk profesional yang kerja di GIIC dan kawasan sekitarnya. | smart-home-panasonic | Done   |

---
## 🚀 Reusable Workflow (Preset)
This workflow is calibrated for high-performance A/B testing on Modal Cloud.

### Formatting Rules:
- **No Symbols:** Asterisks, dashes, and special characters are auto-removed.
- **Respect Breaks:** Use `<br>` to force a newline where you want it.
- **True Center:** All lines are perfectly centered line-by-line.
- **Safe Zone:** Text stays in the upper third, matching the "CBD Deltamas" benchmark.

### Run Command:
```powershell
py -3 -m modal run AI_Tools/modal_hook_renderer.py --hooks-file "Z Brainstorm\Production_Batch.md"
```
