# System Architecture

## 🏗️ High-Level Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    USER INTERACTION                          │
│                   python agent.py                            │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                  UNIVERSAL CREDIT ACT AGENT                  │
│                    (agent.py - Main Class)                   │
└────────────────────────┬────────────────────────────────────┘
                         │
         ┌───────────────┼───────────────┐
         │               │               │
         ▼               ▼               ▼
    ┌────────┐     ┌─────────┐    ┌──────────┐
    │ Task 1 │     │ Task 2  │    │ Task 3   │
    │Extract │     │Summarize│    │ Extract  │
    │  Text  │     │   Act   │    │ Sections │
    └────┬───┘     └────┬────┘    └────┬─────┘
         │              │              │
         │              │              │
         ▼              ▼              ▼
    ┌────────────────────────────────────┐
    │         Task 4: Rule Checks        │
    │    (Uses extracted sections)       │
    └────────────────┬───────────────────┘
                     │
                     ▼
         ┌───────────────────────┐
         │   JSON Report Output  │
         │  output_report.json   │
         └───────────────────────┘
```

## 🔄 Data Flow Diagram

```
INPUT                PROCESSING              OUTPUT
─────                ──────────              ──────

ukpga_20250022_en.pdf
        │
        │ PyPDF2
        ▼
   [Raw Text]
        │
        ├──────────────────────────────────┐
        │                                   │
        ▼                                   ▼
  extracted_text.txt              [Text Buffer in Memory]
                                           │
                                           │
                    ┌──────────────────────┼──────────────────────┐
                    │                      │                      │
                    ▼                      ▼                      ▼
              ┌──────────┐          ┌──────────┐          ┌──────────┐
              │ OpenAI   │          │ OpenAI   │          │ OpenAI   │
              │ GPT-4o   │          │ GPT-4o   │          │ GPT-4o   │
              │  mini    │          │  mini    │          │  mini    │
              └────┬─────┘          └────┬─────┘          └────┬─────┘
                   │                     │                     │
                   ▼                     ▼                     ▼
              [Summary]            [Sections]            [Rule Checks]
              5-10 points          7 sections            6 validations
                   │                     │                     │
                   └─────────────────────┼─────────────────────┘
                                         │
                                         ▼
                                  ┌─────────────┐
                                  │   Compile   │
                                  │   Report    │
                                  └──────┬──────┘
                                         │
                                         ▼
                                output_report.json
                                {
                                  "task1": {...},
                                  "task2": [...],
                                  "task3": {...},
                                  "task4": [...]
                                }
```

## 🧩 Component Breakdown

### 1. PDF Extractor
```
┌─────────────────────────────────────┐
│      PDF Extraction Layer           │
│                                     │
│  Input: ukpga_20250022_en.pdf      │
│  Tool: PyPDF2.PdfReader            │
│  Process:                           │
│    1. Open PDF file                │
│    2. Iterate through pages        │
│    3. Extract text from each       │
│    4. Join all text                │
│  Output: Clean text string         │
│  Save: extracted_text.txt          │
└─────────────────────────────────────┘
```

### 2. AI Analyzer
```
┌─────────────────────────────────────┐
│       AI Analysis Layer             │
│                                     │
│  Tool: OpenAI GPT-4o-mini          │
│  API: openai.chat.completions      │
│                                     │
│  ┌─────────────────────────────┐   │
│  │  Task 2: Summarization      │   │
│  │  - Input: Full text         │   │
│  │  - Prompt: Summarize in     │   │
│  │    5-10 points              │   │
│  │  - Output: JSON array       │   │
│  └─────────────────────────────┘   │
│                                     │
│  ┌─────────────────────────────┐   │
│  │  Task 3: Section Extract    │   │
│  │  - Input: Full text         │   │
│  │  - Prompt: Extract 7        │   │
│  │    sections                 │   │
│  │  - Output: JSON object      │   │
│  └─────────────────────────────┘   │
│                                     │
│  ┌─────────────────────────────┐   │
│  │  Task 4: Rule Validation    │   │
│  │  - Input: Extracted         │   │
│  │    sections                 │   │
│  │  - Prompt: Check 6 rules    │   │
│  │  - Output: JSON array       │   │
│  └─────────────────────────────┘   │
└─────────────────────────────────────┘
```

### 3. Report Generator
```
┌─────────────────────────────────────┐
│     Report Generation Layer         │
│                                     │
│  Input: All task results           │
│  Process:                           │
│    1. Compile task1 metadata       │
│    2. Add task2 summary            │
│    3. Add task3 sections           │
│    4. Add task4 rule checks        │
│    5. Add metadata (date, etc)     │
│  Output: Structured JSON           │
│  Save: output_report.json          │
└─────────────────────────────────────┘
```

## 🔐 Configuration Layer

```
┌─────────────────────────────────────┐
│      Environment Configuration      │
│                                     │
│  File: .env                         │
│  Loaded by: python-dotenv           │
│                                     │
│  Variables:                         │
│    OPENAI_API_KEY=sk-...           │
│                                     │
│  Security:                          │
│    - Not committed to Git          │
│    - Listed in .gitignore          │
│    - Template in .env.example      │
└─────────────────────────────────────┘
```

## 📊 Class Structure

```python
class UniversalCreditActAgent:
    
    def __init__(self, pdf_path):
        # Initialize OpenAI client
        # Store PDF path
        # Prepare text buffer
    
    def task1_extract_text(self):
        # Use PyPDF2 to extract
        # Return clean text
        # Save to file
    
    def task2_summarize(self):
        # Send text to OpenAI
        # Request 5-10 bullet points
        # Return JSON array
    
    def task3_extract_sections(self):
        # Send text to OpenAI
        # Request 7 sections
        # Return JSON object
    
    def task4_rule_checks(self, sections):
        # For each of 6 rules:
        #   - Send section to OpenAI
        #   - Request validation
        #   - Get pass/fail + confidence
        # Return JSON array
    
    def generate_report(self):
        # Call all tasks in sequence
        # Compile results
        # Save JSON report
        # Return complete report
```

## 🌐 External Dependencies

```
┌─────────────────────────────────────┐
│        External Services            │
│                                     │
│  ┌───────────────────────────────┐ │
│  │  OpenAI API                   │ │
│  │  - Endpoint: api.openai.com   │ │
│  │  - Model: gpt-4o-mini         │ │
│  │  - Auth: API Key              │ │
│  │  - Rate Limit: Varies         │ │
│  └───────────────────────────────┘ │
│                                     │
│  ┌───────────────────────────────┐ │
│  │  Python Packages              │ │
│  │  - PyPDF2: PDF processing     │ │
│  │  - openai: API client         │ │
│  │  - python-dotenv: Config      │ │
│  └───────────────────────────────┘ │
└─────────────────────────────────────┘
```

## ⚡ Execution Flow

```
START
  │
  ├─→ Load environment variables (.env)
  │
  ├─→ Initialize OpenAI client
  │
  ├─→ TASK 1: Extract PDF text
  │     ├─→ Open PDF with PyPDF2
  │     ├─→ Extract from all pages
  │     ├─→ Save to extracted_text.txt
  │     └─→ Store in memory
  │
  ├─→ TASK 2: Summarize
  │     ├─→ Send text to OpenAI
  │     ├─→ Request summary format
  │     ├─→ Parse JSON response
  │     └─→ Store summary
  │
  ├─→ TASK 3: Extract sections
  │     ├─→ Send text to OpenAI
  │     ├─→ Request 7 sections
  │     ├─→ Parse JSON response
  │     └─→ Store sections
  │
  ├─→ TASK 4: Validate rules
  │     ├─→ For each rule (6 total):
  │     │     ├─→ Send relevant section
  │     │     ├─→ Request validation
  │     │     ├─→ Parse response
  │     │     └─→ Store result
  │     └─→ Compile all results
  │
  ├─→ COMPILE REPORT
  │     ├─→ Combine all task results
  │     ├─→ Add metadata
  │     ├─→ Format as JSON
  │     └─→ Save to output_report.json
  │
  └─→ DISPLAY SUMMARY
        ├─→ Print summary points
        ├─→ Print rule check results
        └─→ Show output file paths
END
```

## 🎯 Design Principles

1. **Modularity**: Each task is independent
2. **Sequential Processing**: Tasks run in order (1→2→3→4)
3. **Error Handling**: Graceful failures at each step
4. **Transparency**: Progress printed to console
5. **Persistence**: Results saved to files
6. **Configurability**: API key via environment
7. **Simplicity**: Minimal dependencies

## 📈 Performance Characteristics

```
┌─────────────────────────────────────┐
│         Performance Metrics         │
│                                     │
│  Task 1 (PDF Extract):              │
│    Time: 2-5 seconds                │
│    Depends on: PDF size             │
│                                     │
│  Task 2 (Summarize):                │
│    Time: 10-15 seconds              │
│    Depends on: API response time    │
│                                     │
│  Task 3 (Extract Sections):         │
│    Time: 10-15 seconds              │
│    Depends on: API response time    │
│                                     │
│  Task 4 (Rule Checks):              │
│    Time: 30-60 seconds              │
│    Depends on: 6 API calls          │
│                                     │
│  Total Runtime: 1-2 minutes         │
│  Cost per run: ~$0.01-0.02          │
└─────────────────────────────────────┘
```

## 🔒 Security Architecture

```
┌─────────────────────────────────────┐
│         Security Layers             │
│                                     │
│  1. API Key Protection              │
│     - Stored in .env (not Git)     │
│     - Loaded at runtime            │
│     - Never hardcoded              │
│                                     │
│  2. Input Validation                │
│     - PDF file existence check     │
│     - API response validation      │
│                                     │
│  3. Output Sanitization             │
│     - JSON encoding                │
│     - UTF-8 handling               │
│                                     │
│  4. Error Handling                  │
│     - Try-catch blocks             │
│     - Graceful degradation         │
└─────────────────────────────────────┘
```

## 🎨 Why This Architecture?

**Simplicity**: Easy to understand and modify  
**Reliability**: Each component has one job  
**Testability**: Each task can be tested independently  
**Maintainability**: Clear structure, good documentation  
**Scalability**: Easy to add more tasks or rules  
**Cost-Effective**: Uses efficient GPT-4o-mini model  

This architecture balances simplicity with functionality, making it perfect for a 48-hour assignment while demonstrating professional development practices.
