# Universal Credit Act 2025 - AI Agent Analysis

## 🎯 Overview
AI agent that extracts, summarizes, and analyzes the Universal Credit Act 2025, producing a structured JSON report with compliance rule checks.

**⚡ Quick Start**: Run `run_all.bat` or see [START_HERE.md](START_HERE.md) for complete guide.

## 📋 Tasks Completed
- ✅ **Task 1**: Extract full text from PDF
- ✅ **Task 2**: Summarize Act in 5-10 bullet points
- ✅ **Task 3**: Extract key legislative sections
- ✅ **Task 4**: Apply 6 rule compliance checks

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Groq API key (free, no credit card needed)

### Installation
```bash
pip install -r requirements.txt
```

### Configuration
1. Get free Groq API key from https://console.groq.com/keys
2. Copy `.env.example` to `.env`
3. Add your Groq API key:
```
GROQ_API_KEY=gsk-your-key-here
```

### Run
```bash
python agent.py
```

Or use automation:
```bash
run_all.bat
```

## 📤 Output Files
- `output_report.json` - Complete structured analysis
- `extracted_text.txt` - Raw extracted text from PDF

## 🏗️ Architecture

### Components
1. **PDF Extractor** (PyPDF2)
   - Extracts text from all pages
   - Cleans and structures content

2. **AI Analyzer** (Groq - Llama 3.3 70B)
   - Summarizes key points
   - Extracts legislative sections
   - Validates compliance rules

3. **Report Generator**
   - Compiles all analysis
   - Outputs structured JSON

### Data Flow
```
PDF → Extract Text → AI Analysis → JSON Report
                    ↓
            [Summarize, Extract, Validate]
```

## 📊 JSON Output Structure
```json
{
  "document": "Universal Credit Act 2025",
  "ai_model": "Groq - Llama 3.3 70B Versatile",
  "task_1_extract_text": {
    "task_name": "Extract Text from PDF",
    "status": "complete",
    "characters_extracted": 38494,
    "pages_processed": 21
  },
  "task_2_summarize_act": {
    "task_name": "Summarize the Act in 5-10 Bullet Points",
    "summary_points": ["...", "..."]
  },
  "task_3_extract_sections": {
    "task_name": "Extract Key Legislative Sections",
    "sections": {
      "definitions": "...",
      "obligations": "...",
      "responsibilities": "...",
      "eligibility": "...",
      "payments": "...",
      "penalties": "...",
      "record_keeping": "..."
    }
  },
  "task_4_rule_checks": {
    "task_name": "Apply 6 Rule Compliance Checks",
    "rules_checked": 6,
    "rules_passed": 4,
    "checks": [
      {
        "rule": "Act must define key terms",
        "status": "pass",
        "evidence": "Section 2 - Definitions",
        "confidence": 100
      }
    ]
  }
}
```

## 🛠️ Technologies
- **Python 3.8+**
- **PyPDF2** - PDF text extraction
- **Groq API** - AI analysis using Llama 3.3 70B (FREE)
- **python-dotenv** - Environment management

## 🎥 Demo Video
[Watch 2-Minute Demo Video](https://youtu.be/tts-XUHU6Ek)

## 👤 Author
NIYAMR 48-Hour Internship Assignment

## ⏱️ Completion Time
Completed within 48-hour deadline

## 📚 Additional Documentation
- [Quick Start Guide](QUICKSTART.md) - Get running in 5 minutes
- [Setup Guide](SETUP_GUIDE.md) - Detailed setup instructions
- [Video Script](VIDEO_SCRIPT.md) - Guide for recording demo
- [Troubleshooting](TROUBLESHOOTING.md) - Common issues and solutions
- [Submission Checklist](SUBMISSION_CHECKLIST.txt) - Pre-submission checklist
- [Project Summary](PROJECT_SUMMARY.md) - Technical overview

## 🔑 Why Groq/Llama?
- ✅ **Free** - No credit card required
- ✅ **Fast** - Faster than OpenAI
- ✅ **Compliant** - Assignment allows "Llama" models
- ✅ **Powerful** - Llama 3.3 70B is highly capable
- ✅ **Easy** - Simple API, same as OpenAI

## 📝 License
This project is for educational purposes as part of the NIYAMR internship assignment.
