# Tasks Generator – Mini Planning Tool

A simple web application that helps convert a high-level feature idea into
structured user stories and engineering tasks.

This project was built as part of a time-boxed technical assignment to
demonstrate product thinking, clean implementation, and sensible AI usage.

---

##  Features

- Simple home page with clear navigation
- Form-based input for:
  - Feature goal
  - Target users
  - Constraints
  - App template (Web / Mobile / Internal tool)
- Generate:
  - User stories
  - Engineering tasks (LLM or mock mode)
- Edit generated tasks directly in the UI
- View last 5 generated specs
- Status page showing:
  - Frontend health
  - Backend health
  - LLM mode (mock / configured)
- Basic validation for empty or invalid input
- Export-ready output (copyable Markdown/text)

---

##  Project Structure

tasks-generator/

├── app.py # Main entry point & navigation

├── pages/

 ├── Home.py # Home page
 
 ├── Generator.py # Task generation UI
 
 ├── Status.py # System status page

├── utils/

 ├── prompts.py # Prompt templates
 
 ├── generator.py # Task generation logic (LLM / mock)
 
 ├── storage.py # Session-based storage helpers

├── README.md

├── AI_NOTES.md

├── PROMPTS_USED.md

├── ABOUTME.md

├── requirements.txt

├── .env.example


---

##  How to Run Locally

### 1️ Clone the repository

git clone <repo-url>
cd tasks-generator
---
## Install dependencies
pip install -r requirements.txt

## Run the app
streamlit run app.py

## Known Limitations
- Task reordering and grouping are manual (via editing text)
- No persistent database (session-based storage only)
- Minimal styling (focus on functionality and clarity)

## What Is Not Done (Yet)
- Authentication
- Multi-user persistence
- Advanced task management UI (drag & drop)
- Rich analytics or metrics



