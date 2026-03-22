**1. Remotion template development** `remotion/src/` — TypeScript/React video templates that need visual preview. You edit props, the Remotion preview renders in a browser, you iterate. Claude Code is blind to the rendered output. Antigravity could _see_ the preview, adjust values, and verify visually without you relaying screenshots.

**2. Offer sheet website** `Fulfillment/_OFFER_BLUEPRINT/offer_sheets/index.html` — live HTML/CSS page hosted on GitHub Pages. Building and refining this requires visual iteration. An agent that can open the page, inspect layout, edit the file, and verify the result closes the loop without you acting as the eyes.

**3. n8n automation design** Your n8n workflows live in n8n cloud with a visual canvas UI. When designing new automations, an agent with browser control could navigate the n8n interface, wire nodes, and test flows directly — rather than you translating text instructions into UI actions manually.

---

**The pattern:** All three involve a browser-rendered output that Claude Code can't see. That's Antigravity's actual edge over what you have now. Everything else — strategy, scripts, content, CRM — stays here where the WAT execution layer lives.