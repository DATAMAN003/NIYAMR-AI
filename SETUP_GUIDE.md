# Setup & Submission Guide

## 🔧 Setup Steps

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Get FREE Groq API Key
1. Go to https://console.groq.com/
2. Sign up (free, no credit card needed)
3. Go to https://console.groq.com/keys
4. Create API key

### 3. Configure API Key
Create a `.env` file:
```bash
copy .env.example .env
```

Edit `.env` and add your key:
```
GROQ_API_KEY=sk-your-actual-key-here
```

### 3. Run the Agent
```bash
python agent.py
```

Or on Windows:
```bash
run_all.bat
```

## 📦 What Gets Generated

After running, you'll have:
- `extracted_text.txt` - Full text from the PDF
- `output_report.json` - Complete structured analysis
