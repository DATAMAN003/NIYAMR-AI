# Setup & Submission Guide

## 🔧 Setup Steps

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure OpenAI API Key
Create a `.env` file:
```bash
copy .env.example .env
```

Edit `.env` and add your key:
```
OPENAI_API_KEY=sk-your-actual-key-here
```

### 3. Run the Agent
```bash
python agent.py
```

Or on Windows:
```bash
run.bat
```

## 📦 What Gets Generated

After running, you'll have:
- `extracted_text.txt` - Full text from the PDF
- `output_report.json` - Complete structured analysis

## 🎥 Recording Your Video

Use the `VIDEO_SCRIPT.md` as your guide. Record:
1. Introduction to the project
2. Architecture explanation
3. Quick code walkthrough
4. Live demo or results showcase
5. Conclusion

Tools you can use:
- Loom (free, easy)
- OBS Studio (free, professional)
- Zoom (record yourself)
- Windows Game Bar (Win+G)

## 📤 GitHub Submission Checklist

### Files to Include:
- ✅ `agent.py` - Main code
- ✅ `requirements.txt` - Dependencies
- ✅ `README.md` - Documentation
- ✅ `.env.example` - Config template
- ✅ `.gitignore` - Ignore sensitive files
- ✅ `ukpga_20250022_en.pdf` - Source document
- ✅ `output_report.json` - Sample output

### Files to Exclude (in .gitignore):
- ❌ `.env` - Contains your API key
- ❌ `__pycache__/` - Python cache

### Git Commands:
```bash
git init
git add .
git commit -m "Complete Universal Credit Act 2025 AI Agent"
git branch -M main
git remote add origin https://github.com/yourusername/universal-credit-act-agent.git
git push -u origin main
```

## 🎯 Final Deliverables

1. **GitHub Repository URL**
   - Include in your submission email
   - Make sure it's public

2. **JSON Output**
   - Include `output_report.json` in the repo
   - Or attach to submission email

3. **2-Minute Video**
   - Upload to YouTube/Loom/Drive
   - Include link in README or submission

## ⚡ Quick Test

Before submitting, verify:
```bash
# Test installation
pip install -r requirements.txt

# Test run (make sure .env is configured)
python agent.py

# Check outputs exist
dir output_report.json
dir extracted_text.txt
```

## 🆘 Troubleshooting

**"No module named PyPDF2"**
→ Run: `pip install -r requirements.txt`

**"OpenAI API key not found"**
→ Check your `.env` file exists and has the correct key

**"PDF not found"**
→ Make sure `ukpga_20250022_en.pdf` is in the same folder

**Rate limit errors**
→ The code uses gpt-4o-mini which is cost-effective. If you hit limits, wait a minute and retry.

## 💡 Tips

- Test everything before recording your video
- Keep your API key private (never commit .env)
- The agent takes 1-2 minutes to run (AI processing time)
- Review the JSON output to understand what it found

Good luck! 🚀
