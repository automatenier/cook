import os
import re
import sys
from pathlib import Path

# Use the existing repurpose prompt logic but specialized for Kanban expansion
EXPANSION_PROMPT = """You are a Content Strategist for JO Consult. 
Your task is to take a "Winning Outlier" content idea and expand it into 10 distinct "DRAFT" cards for a Kanban board.

Brand Voice: Authentic, Anak Jaksel (Mixed Indonesian/English), authoritative but conversational.
Target: Business owners/Coaches scaling with AI & Systems.

Original Outlier Idea:
{original_content}

Generate 10 distinct cards. Each card must have a specific format prefix.
Return ONLY a list of 10 markdown task items formatted like this:
- [ ] ### [DRAFT] [Format Name]: [Catchy Hook/Title in Mixed Indo/English]

The 10 Formats to use:
1. Reel (Value-Led): Deep educational value.
2. Reel (Reply-as-Video): Addressing a hypothetical "hater" or "curious" comment.
3. Reel (Contrarian): Flipping a common niche belief.
4. Carousel (Step-by-Step): Visual breakdown of the process.
5. Threads (Hard Truth): Brutal honesty/Call-out post.
6. Threads (Numbers/Results): Social proof/Authority.
7. Threads (Vulnerable): Story about failure to success.
8. Story Sequence: 3-slide engagement loop.
9. Newsletter: Deep-dive email topic.
10. YouTube Short: High-speed, high-retention loop.

Return only the 10 markdown lines."""

def expand_kanban(file_path):
    path = Path(file_path)
    if not path.exists():
        print(f"Error: {file_path} not found.")
        return

    content = path.read_text(encoding="utf-8")
    
    # Identify the sections
    sections = re.split(r"(^## .*$)", content, flags=re.MULTILINE)
    
    qa_lane_idx = -1
    finished_lane_idx = -1
    
    for i, line in enumerate(sections):
        if "Comment-Led Creation" in line:
            qa_lane_idx = i + 1
        if "## Finished" in line:
            finished_lane_idx = i + 1

    if qa_lane_idx == -1:
        print("Error: Could not find Q&A Loop lane.")
        return

    # Find cards to process (those containing [IDENTIFIED])
    qa_lane_content = sections[qa_lane_idx]
    cards_to_process = re.findall(r"- \[ \] ### \[IDENTIFIED\].*", qa_lane_content)

    if not cards_to_process:
        print("No [IDENTIFIED] cards found in the Q&A Loop lane.")
        return

    # Initialize Anthropic/Claude for generation
    # Since I'm the agent, I'll simulate the call or use the available API if this were a standalone tool.
    # For this script's persistence, we assume it's triggered by me.
    
    for card in cards_to_process:
        print(f"Processing card: {card}")
        
        # Here we would call the LLM. For the purpose of this script creation, 
        # I will implement the logic where the Agent (me) calls it.
        # But for the user's workflow, they want ME to do it when I see it.
        
    print("Workflow Tool Ready. I will now execute the first run manually to demonstrate.")

if __name__ == "__main__":
    expand_kanban("VLT_Content/01 HMN_Command/DOUBLE DOWN.md")
