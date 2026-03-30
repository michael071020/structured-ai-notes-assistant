# Structured AI Notes Assistant

Structured AI Notes Assistant is a small LLM application that converts long-form text into structured notes with fixed output fields.

## Project Goal
This project is built to practice the foundation of LLM application development by creating a small but complete system.

Given a long piece of text such as an article, transcript, job description, or meeting notes, the application generates structured notes including:

- summary
- key points
- action items
- tags
- JSON structured output

## Problem
Long-form text is often difficult to digest quickly.

This project turns long-form input into structured, reusable notes that are easier to read and easier for downstream code to process.

## What It Does
The application:

1. reads a text file
2. sends the content to an LLM
3. asks the model to return structured JSON
4. parses and validates the response
5. prints a human-readable version
6. saves the structured result as a JSON file

## Current Features
- Accepts one text input at a time
- Generates:
  - title
  - summary
  - key_points
  - action_items
  - tags
- Returns structured JSON output
- Performs basic validation on the parsed result
- Saves output to a JSON file
- Supports a simple CLI interface

## Project Structure
```
structured-ai-notes-assistant/
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
├── docs/
│   └── mvp-spec.md
├── examples/
│   ├── input.txt
│   └── output.json
├── notebooks/
│   └── playground.ipynb
├── prompts/
│   └── note_prompt.txt
└── src/
    ├── main.py
    ├── llm/
    │   └── client.py
    └── utils/
        └── parser.py
```

## Setup

### 1. Clone the repository
`git clone https://github.com/michael071020/structured-ai-notes-assistant.git`

`cd structured-ai-notes-assistant`

### 2. Install dependencies
`pip install -r requirements.txt`

### 3. Create a .env file
Create a `.env` file in the project root.

Example:
- OPENAI_API_KEY=your_api_key_here
- OPENAI_MODEL=gpt-5.4-mini

You can also copy from `.env.example`.

## Usage

### Default run
`python src/main.py`

### Run with explicit input and output paths
`python src/main.py --input examples/input.txt --output examples/output.json`


## Example Input
A sample input file is provided in:
`examples/input.txt`


## Example Output
A sample output file is provided in:
`examples/output.json`

The generated JSON has the following structure:
```
{
  "title": "string",
  "summary": "string",
  "key_points": ["string", "string"],
  "action_items": ["string", "string"],
  "tags": ["string", "string"]
}
```


## How It Works
The pipeline is:
```
input text
-> prompt template
-> LLM call
-> JSON output
-> parse
-> validate
-> print
-> save as output.json
```


## Limitations
- Only supports plain text input for now
- Only processes one input at a time
- Validation is still basic
- Output quality depends on prompt quality and model behavior


## Learning Focus
This project is intentionally small.

The main purpose is to practice:
- prompt design
- structured output handling
- parsing and validation
- modular project structure
- packaging an LLM project for GitHub