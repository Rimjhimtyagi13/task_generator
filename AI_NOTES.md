# AI Usage Notes

This document explains how AI was used during the development of the Tasks Generator app, and what was manually reviewed and implemented by me.

---

##  Where AI Was Used

AI was used as a **development assistant**, not as an autonomous agent.

Specifically, AI helped with:
- Structuring the project folder layout
- Drafting initial prompt templates for task generation
- Suggesting Streamlit UI patterns
- Explaining error messages and debugging issues
- Improving clarity and wording in documentation

All AI-generated suggestions were reviewed, modified, and integrated manually.

---

##  Where AI Was NOT Used

AI was **not** used to:
- Automatically generate the full application
- Blindly copy-paste code without understanding
- Make architectural decisions without validation
- Test or run the application

Final decisions about:
- State management
- Error handling
- Mock mode fallback
- Page navigation
were made manually.

---

##  LLM & Provider Used

- **Provider:** OpenAI  
- **Model (planned):** `gpt-4o-mini`

The model was chosen because:
- It is cost-efficient
- Fast for short structured outputs
- Suitable for generating user stories and task lists

---

##  Mock Mode Design Choice

To ensure the app:
- Always runs for reviewers
- Does not fail without API keys
- Meets assignment constraints

A **mock output mode** was implemented.

If `OPENAI_API_KEY` is not set:
- The app returns a deterministic mock response
- The UI and flow remain fully functional
- System Status page reflects "LLM: Mock mode"

This was a deliberate engineering decision to improve reliability.

---

##  API Key Handling

- API keys are never committed to the repository
- Environment variables are accessed via `os.getenv`
- `.env.example` is provided for configuration reference
- `.gitignore` ensures `.env` is excluded

---

##  What Was Manually Verified

- Input validation logic
- Session state behavior across pages
- Task generation flow
- History storage (last 5 specs)
- Error handling and graceful fallbacks
- App runs without API key

---

##  Summary

AI was used as a **supporting tool**, not a replacement for reasoning or engineering judgment.

The goal was to demonstrate:
- Responsible AI usage
- Understanding of system design
- Clean and explainable implementation
