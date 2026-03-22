---
name: pptx-generator
description: Create and modify PowerPoint (.pptx) presentations. Use when you need to generate professional slides from text, scripts, or project data.
---

# PPTX Generator

This skill enables the creation and modification of PowerPoint presentations using the `python-pptx` library.

## Workflow

1.  **Analyze Content**: Identify the key points, titles, and structure for the slides.
2.  **Format Input**: Create a JSON file with the presentation structure.
3.  **Execute Tool**: Run the `create_pptx.py` script.

### JSON Input Format

```json
{
  "title": "Presentation Title",
  "subtitle": "Optional Subtitle",
  "slides": [
    {
      "title": "Slide 1 Title",
      "content": [
        "Bullet point 1",
        "Bullet point 2"
      ]
    },
    {
      "title": "Slide 2 Title",
      "content": [
        "Important fact",
        "Key takeaway"
      ]
    }
  ]
}
```

## Tools

### Create Presentation

```bash
py -3 skills/pptx-generator/scripts/create_pptx.py <input_json_path> <output_pptx_path>
```

## Guidelines

- **Conciseness**: Keep bullet points brief.
- **Hierarchy**: Use a logical flow from title slide to summary.
- **Validation**: Ensure `python-pptx` is installed (`py -3 -m pip install python-pptx`).
