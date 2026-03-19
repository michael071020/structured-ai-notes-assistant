# Structured AI Notes Assistant

Structured AI Notes Assistant is a small LLM application that converts long-form text into structured notes with fixed output fields.

## Project Goal
This project is built to practice the foundation of LLM application development by creating a small but complete system.

Given a long piece of text such as an article, transcript, job description, or meeting notes, the application will generate structured notes including:

- summary
- key points
- action items
- tags
- JSON structured output

## Planned Core Features
- Accept one text input at a time
- Process the input with an LLM
- Return structured notes in JSON format
- Provide a readable output version for users

## Example Use Cases
- Summarize meeting notes into actionable items
- Turn a job description into structured key points
- Extract important information from long articles or transcripts

## Project Structure
```text
structured-ai-notes-assistant/
├── README.md
├── .gitignore
├── docs/
│   └── mvp-spec.md
├── examples/
└── src/
```

### MVP Output Format
The target structured output includes:
```json
{
  "title": "Project Sync Meeting",
  "summary": "The meeting reviewed the current project status, blockers, and next steps.",
  "key_points": [
    "The frontend integration is delayed by two days.",
    "The team agreed to finalize the API contract this week."
  ],
  "action_items": [
    "Finalize API contract by Friday.",
    "Prepare updated project timeline."
  ],
  "tags": [
    "meeting",
    "project",
    "planning"
  ]
}
```