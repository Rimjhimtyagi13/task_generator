def build_task_prompt(goal, users, constraints, template):
    """
    Builds a structured prompt for task generation.
    """

    prompt = f"""
You are a product manager and a senior software engineer.

Given the following feature details, generate:
1. User stories
2. Engineering tasks grouped into:
   - Frontend
   - Backend
   - QA / Testing

Feature Goal:
{goal}

Target Users:
{users}

Constraints:
{constraints if constraints else "None"}

Template Type:
{template}

Output format (STRICT):
## User Stories
- As a ..., I want to ..., so that ...

## Engineering Tasks

### Frontend
- ...

### Backend
- ...

### QA / Testing
- ...
"""
    return prompt
