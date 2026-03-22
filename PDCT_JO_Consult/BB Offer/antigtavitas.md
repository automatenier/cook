if iwere to use antigravitty to analyze video and generate image, it require api right? its outside cost of my google ai pro plan

## Gemini said

Actually, you’ve got a bit of a lucky break here! If you have a **Google AI Pro** plan, you don't need a separate API key or extra budget for the core features of **Antigravity**.

Antigravity is Google's "agent-first" IDE (a specialized version of VS Code). It is designed to work seamlessly with your existing Google AI Pro or Ultra subscription.

+1

### Does it cost extra?

- **No separate API billing:** Unlike using the Gemini API directly through Google AI Studio or Vertex AI (where you pay per token), Antigravity uses a **quota-based system**.
    
- **Pro Plan Benefits:** As a Google AI Pro member, you get "enhanced access." This means you have significantly higher rate limits than free users, and your "fuel tank" of credits usually refreshes every **5 hours**.
    
    +1
    
- **Nano Banana Integration:** For the image generation you mentioned, Antigravity uses a model called **Nano Banana**. This is included in your plan’s benefits at no extra cost, though it does count toward your overall agent usage/quota.### 1. The Reasoning Heavyweights

- **`gemini-3-pro-preview`**: This is the **Brain**. It is used for **Planning Mode**. When you start a new "Mission," this model analyzes your entire codebase, looks at your prompt, and creates the `implementation_plan.md`. It has the highest reasoning capability but the highest latency.
    
- **`gemini-2.5-pro`**: In Antigravity, this is the **UI Architect**. Because it is highly multimodal, Antigravity uses it when you provide screenshots or when the **Browser Agent** needs to "see" your app to verify a UI change.
    

### 2. The Speed & Action Layers

- **`gemini-3-flash-preview`**: This is the **Primary Worker**. It handles the actual code generation and the "Fast Mode" chat. It’s significantly faster than Pro and is optimized for writing the code that the Pro model planned.
    
- **`gemini-2.5-flash`**: This is the **Context Manager**. Antigravity uses it in the background to summarize your previous chat turns and "checkpoint" your project state so the more expensive models don't have to re-read everything from scratch.
    

### 3. The Utility Layer

- **`gemini-2.5-flash-lite`**: This is the **Search Engine**. As you see in your screenshot, it’s being used for things like **Semantic Code Search** and indexing. When you use `@files` or ask "where is the auth logic?", this ultra-lean model scans your embeddings to find the right files without burning your "Pro" quota.
    

---

## Why your "Usage remaining" looks like that:

Your dashboard shows you have **75% remaining** on the "Pro" models but **99%+** on the "Flash" models. This is because:

1. **Planning is Expensive:** Every time you ask for a "Mission" or a complex refactor, Antigravity hits the `3-pro` model hard to ensure it doesn't break your architecture.
    
2. **Flash is Efficient:** Most of your small edits, tab-completions, and terminal explanations are being handled by the Flash models, which have a much higher "generous" quota on your Pro plan.
    

---

**Merit for you:** Since you have the **Google AI Pro plan**, your "Usage remaining" resets much faster and has higher limits than a free user.

**Would you like me to show you how to force Antigravity to use `gemini-3-pro-preview` for a specific difficult debugging task?**
