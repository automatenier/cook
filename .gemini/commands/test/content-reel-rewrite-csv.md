> **Model: Haiku** — template rewrite from transcription CSV

# Workflow: Reel Rewriting from CSV

When the user asks to `/reel-rewrite-csv [CSV Path] [ClientName]`:

1. **Read CSV**: Parse CSV with columns `Video Reference`, `Transcription`.
2. **Rewrite Script**: Read `VLT_Content/02_HMN_HUMANFLOW/jocons/[ClientName]/client_brief.md` to apply brand tone.
3. **Generate Assets**: Output structured markdown (hook, core message, CTA) to `VLT_Content/02_HMN_HUMANFLOW/jocons/[ClientName]/projects/[YYYY-MM]/scripts/`.
4. **Render (Optional)**: Trigger `/render-simple-reel`.

```bash
/reel-rewrite-csv .tmp/transcriptions.csv fadli
```
