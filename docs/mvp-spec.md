# MVP Spec - Structured AI Notes Assistant

## Product
Structured AI Notes Assistant

## One-liner
A small LLM application that converts long-form text into structured notes with fixed output fields.

## Goal
This MVP is designed to transform long-form unstructured text into a stable, structured, and reusable note format.

The goal is not to build a chatbot or a full AI assistant.  
The goal is to build a small but complete LLM application with clear input, predictable output, and a usable project structure.

## Core Use Case
A user provides a long piece of text, such as:
- an article
- a transcript
- a job description
- meeting notes

The application sends the text to an LLM and returns:
- a readable summary
- key points
- action items
- tags
- a structured JSON result

## MVP Scope
This MVP includes the following:

- Accept one text input at a time
- Process the input with an LLM
- Generate:
  - summary
  - key_points
  - action_items
  - tags
- Return the result in a fixed JSON structure
- Show a human-readable version of the output

## Input Definition
### Input type
Plain text

### Input source
- pasted text
- txt file

### Expected input
Long-form unstructured text, such as an article, transcript, job description, or meeting notes.

## Output Definition
### Output format
JSON

### Required fields
- title
- summary
- key_points
- action_items
- tags

### Example output
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

## Success Criteria
This MVP is considered successful if:
- the application can process sample long texts end-to-end
- the output is valid JSON
- all required fields are present
- the generated content is relevant to the input text
- the result is readable by humans and parseable by code

## Final Deliverable
The final MVP should be delivered as a GitHub project that includes:
- a runnable Python application
- example input and output files
- a README explaining the project goal, setup, and usage
- a simple demo flow showing text-to-structured-notes generation