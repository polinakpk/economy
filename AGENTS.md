# AGENTS.md

## Project
Teen financial simulator for a school project.

## Goal
Build a simple educational game where a teenager manages money, mood, skills, monthly income, expenses, and life events.

## Tech stack
- Python
- Flask
- HTML
- CSS
- minimal JavaScript
- no database for MVP

## Architecture
- `player.py` -> player state and player-related logic
- `game.py` -> game rules, month flow, calculations
- `events.py` -> game events and choices
- `app.py` -> Flask routes only
- `templates/` -> HTML templates
- `static/` -> CSS and minimal JavaScript

## Development rules
- Keep code simple and beginner-friendly.
- Prefer clear code over clever code.
- Do not add frameworks or libraries unless explicitly requested.
- Do not add Django, React, PostgreSQL, Redis, Docker, or other infrastructure.
- Do not add a database unless explicitly requested.
- Keep game logic in Python.
- Keep Flask thin: routes should call existing Python logic, not contain game rules.
- Make the smallest possible change for each task.
- Do not refactor unrelated files.
- Do not rewrite the whole project unless explicitly requested.
- Reuse the existing project structure.
- Use descriptive names and small functions.
- Avoid advanced Python patterns unless they are necessary.
- Do not hide logic behind unnecessary abstractions.
- Do not create extra files unless there is a clear reason.

## Learning rules
- This is a student project.
- Generated code must be understandable by a beginner Python student.
- When making changes, briefly explain what was changed and why.
- If a task can be solved simply, choose the simpler solution.
- Do not replace working student code just because another style is cleaner.
- Preserve opportunities for the student to implement core Python logic themselves.

## For every coding task
1. Inspect the existing implementation first.
2. Change only what is required.
3. Do not add unrelated improvements.
4. Run or suggest a simple test for the changed behavior.
5. At the end, list:
   - files changed
   - what changed
   - how to test it
