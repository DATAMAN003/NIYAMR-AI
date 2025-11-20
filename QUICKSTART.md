# ⚡ Quick Start - 5 Minutes to Running

## Step 1: Install Dependencies (1 min)
```bash
pip install -r requirements.txt
```

## Step 2: Get FREE Groq API Key (2 min)
1. Go to https://console.groq.com/
2. Sign up (free, no credit card needed!)
3. Go to https://console.groq.com/keys
4. Click "Create API Key"
5. Copy the key (starts with `gsk_`)

## Step 3: Configure API Key (1 min)
```bash
# Copy the template
copy .env.example .env

# Edit .env and add your Groq API key
# GROQ_API_KEY=gsk-your-actual-key-here
```

## Step 4: Test Setup (30 sec)
```bash
python test_setup.py
```

Should see: ✅ ALL TESTS PASSED

## Step 5: Run the Agent (2 min)
```bash
python agent.py
```

Wait 1-2 minutes for AI analysis...

## Step 6: Check Output (30 sec)
```bash
# View the JSON report
type output_report.json

# Or open in your editor
```

## ✅ Done!

You should now have:
- `extracted_text.txt` - Full text from PDF
- `output_report.json` - Complete analysis with all 4 tasks



## One-Liner (if everything is set up)
```bash
run_all.bat
```

That's it! 🚀
