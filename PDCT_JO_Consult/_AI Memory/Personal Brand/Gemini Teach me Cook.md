### **Phase 0: Onboarding & Strategy (Week 1)**

This phase is about setting the foundation for success.

**Prompt 1: Onboard New Client & Create Assets** First, you need to officially onboard Alex, gather key data, and create his personalized "AI Swipe File".

- **You would say to Claude:**
    
    ```
    Claude, onboard new client.
    ```
    
- **Claude would then use your pre-defined `[onboard.md](code-assist-path:c:\Workspace\Cook\.claude\commands\onboard.md "c:\Workspace\Cook\.claude\commands\onboard.md")` command to ask for the details:**
    
    > "Okay, Jordan. To onboard the new client, please provide the following information:
    > 
    > - **Client Name:**
    > - **Client Business Name:**
    > - **Niche/Industry:**
    > - **Link to Client's Instagram/Main Platform:**
    > - **Client's Recorded 10-min Voice Sample (link):**
    > 
    > I will use this to create their GDrive, set up the AI Swipe File in Notion, and initiate the ElevenLabs voice cloning process."
    

**Prompt 2: Set Up Client's Sales System** Next, you'll use a Gemini command to create the client's Excel CRM and dashboard.

- **You would say to Gemini:**
    
    ```
    Gemini, execute create_excel_crm for client "Alex".
    ```
    
- **Gemini would then run your Python script (`[create_excel_crm.py](code-assist-path:c:\Workspace\Cook\Tools\create_excel_crm.py "c:\Workspace\Cook\Tools\create_excel_crm.py")`), which would:**
    1. Create a new `Alex_CRM.xlsx` and `Alex_Dashboard.xlsx` from your templates.
    2. Save them into Alex's newly created GDrive folder.
    3. Return a message: "CRM and Dashboard for Alex have been created and are available in their GDrive."

**Prompt 3: Flesh out the AI Swipe File (Offer & Content Strategy)** This is a collaborative session with Alex, facilitated by Claude, to define his brand.

- **You would initiate a meeting with Alex and Claude and prompt Claude:**
    
    ```
    Claude, let's run the "Offer Blueprint" and "Content Strategy" consultation for Alex. Please guide us through the questions.
    ```
    
- **Claude would then act as a consultant, asking Alex questions based on your methodology:**
    
    > "Welcome, Alex. Let's define your unique position in the market.
    > 
    > **Part 1: Your Offer**
    > 
    > - What is the primary result you deliver for your clients?
    > - What are the key deliverables (e.g., weekly check-ins, custom meal plans)?
    > - What is your unique guarantee?
    > 
    > **Part 2: Your Content Persona**
    > 
    > - Who is your Ideal Client Profile (ICP)? Describe them.
    > - What are 3-5 core topics you love talking about?
    > - Are there any topics you want to avoid?
    > - Which of these content styles feels most like you: "Contrarian Expert", "Supportive Guide", or "Aspirational Case Study"?"
    > 
    > _(Claude would record all answers directly into Alex's "AI Swipe File".)_
    

---

### **Phase 1 & 2: Content Production & System Setup (Weeks 2-4)**

Now you turn the strategy into tangible assets. Alex has done his onsite filming.

**Prompt 4: Generate Monthly Content** You use Gemini to generate the entire content plan for the month.

- **You would say to Gemini:**
    
    ```
    Gemini, generate the full 30-day content calendar for client "Alex" for March 2026. Use his AI Swipe File. The output should include:
    - 30 Reel Scripts (15 Authentic, 15 Value/CTA)
    - 30 Story Sequences
    - 30 Threads
    - 4 YouTube Scripts
    ```
    
- **Gemini would then perform the generation, referencing Alex's swipe file to ensure the content is in his voice and targeted to his audience.**

**Prompt 5: Repurpose a Reel** To create even more content, you can use your repurposing tool.

- **You would say to Gemini:**
    
    ```
    Gemini, run repurpose_content on "Alex_Reel_Script_01.txt". Target platforms are Instagram, TikTok, and a newsletter snippet.
    ```
    
- **Gemini would execute your `[repurpose_content.py](code-assist-path:c:\Workspace\Cook\Tools\repurpose_content.py "c:\Workspace\Cook\Tools\repurpose_content.py")` script**, creating multiple content variations from a single script.

**Prompt 6: Handoff the System** At the end of the initial setup, you walk Alex through everything you've built.

- **You would say to Claude:**
    
    ```
    Claude, prepare for the "Content & System Handoff" call with Alex.
    ```
    
- **Claude would use your `[handover.md](code-assist-path:c:\Workspace\Cook\.claude\commands\handover.md "c:\Workspace\Cook\.claude\commands\handover.md")` command to generate a checklist and talking points for the call:**
    
    > "Handoff Agenda for Alex:
    > 
    > 1. **Demo the Live Systems:**
    >     - Walk through the Excel Sales Dashboard.
    >     - Show the 1-Page Funnel.
    >     - Explain the Telegram bot commands.
    > 2. **Review the Content:**
    >     - Present the 30-day content calendar.
    >     - Showcase the edited video drafts.
    > 3. **Explain the Workflow:**
    >     - Daily: Approve content via Telegram.
    >     - Weekly: Attend strategy call.
    > 4. **Q&A.**"
    

---

### **Phase 3 & Ongoing: Scaling & Support (Month 2+)**

The system is running, and now it's about optimization and scaling.

**Prompt 7: Monthly Strategy Session** You meet with Alex and your team to plan the next month.

- **You would say to Claude:**
    
    ```
    Claude, it's time for Alex's monthly strategy call. Pull up his dashboard stats and let's prepare the agenda based on the ``monthly.md`` command.
    ```
    
- **Claude would then analyze the data and create the agenda:**
    
    > "Monthly Strategy for Alex:
    > 
    > - **Performance Review:**
    >     - Top 3 performing reels this month.
    >     - Lead-to-call conversion rate.
    > - **Strategy for Next Month:**
    >     - Based on the data, we should double down on "Hot Take" style content.
    >     - Let's test a new CTA for the VSL.
    > - **Goals for next month.**"
    

This sequence of prompts transforms your detailed offer sheet into a repeatable, scalable, and AI-assisted service delivery process.

Gen