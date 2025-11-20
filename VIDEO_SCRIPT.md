# 2-Minute Video Script

## Introduction (15 seconds)
"Hi! I'm presenting my solution for the NIYAMR 48-hour AI Agent internship assignment. I built an AI agent that analyzes the Universal Credit Act 2025 and produces a structured JSON report."

## Architecture Overview (30 seconds)
"The architecture has three main components:

1. **PDF Extractor** - Uses PyPDF2 to extract clean text from the Act
2. **AI Analyzer** - Leverages OpenAI's GPT-4 to understand and analyze the content
3. **Report Generator** - Compiles everything into structured JSON

The data flows from PDF extraction, through AI analysis for summarization, section extraction, and rule validation, finally outputting to JSON."

## Task Walkthrough (45 seconds)
"Let me show you the four tasks:

**Task 1** - Extracts all text from the PDF and saves it to a file

**Task 2** - Uses AI to generate 5-10 bullet points summarizing the Act's purpose, definitions, eligibility, obligations, and enforcement

**Task 3** - Extracts seven key sections: definitions, obligations, responsibilities, eligibility, payments, penalties, and record-keeping

**Task 4** - Runs six compliance rule checks, each returning pass/fail status with evidence and confidence scores"

## Demo & Results (20 seconds)
"Running the agent is simple - just `python agent.py`. It processes the PDF, analyzes it with AI, and outputs two files: the extracted text and a complete JSON report with all findings."

## Conclusion (10 seconds)
"The solution is production-ready, well-documented, and completes all four tasks. The code is on GitHub with full setup instructions. Thank you!"

---

## Recording Tips
- Show your face or screen recording
- Display the code structure briefly
- Run the agent live if possible
- Show the JSON output
- Keep energy high and pace quick
