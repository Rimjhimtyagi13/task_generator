import os
#rom openai import OpenAI
from utils.prompts import build_task_prompt


def generate_tasks(goal, users, constraints, template):
    #api_key = os.getenv("OPENAI_API_KEY")

    # ---------- MOCK MODE ----------
    #if not api_key:
    mock_output = f"""
### 🧑‍💻 User Stories
- As a user, I want to {goal.lower()} so that my problem is solved.

### 🛠️ Engineering Tasks
- Clarify requirements and edge cases
- Design UI components
- Implement backend logic
- Add validation and error handling
- Write basic tests
- Prepare documentation
"""
    return mock_output, None# "Running in mock mode (no API key configured)."

  
