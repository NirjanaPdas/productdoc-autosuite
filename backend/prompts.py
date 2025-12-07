# prompts.py
"""
Prompt templates for ProductDoc AutoSuite
"""

PRD_PROMPT = """
You are an AI product manager. Based on the brief below, generate a clean, structured PRD.

BRIEF:
{brief}

Include:
- Problem Statement
- Target Users
- Core Features
- Success Metrics
- Constraints
"""

LANDING_PAGE_PROMPT = """
You are a marketing copywriter. Generate a landing page content for:

BRIEF:
{brief}

Sections:
- Hero Title
- Subtitle
- Key Benefits
- How it Works
- Call to Action
"""

FAQ_PROMPT = """
You are a customer support assistant. Generate top FAQs for:

BRIEF:
{brief}

Output 5–7 question–answer pairs.
"""

VIDEO_SCRIPT_PROMPT = """
You are a scriptwriter. Create a 30-second promotional video script for:

BRIEF:
{brief}

Include:
- Scene-by-scene breakdown
- Voiceover text
- Visual suggestions
"""
