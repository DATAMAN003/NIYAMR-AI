# Troubleshooting Guide

## Common Issues & Solutions

### 1. Installation Issues

#### "pip: command not found"
**Problem**: Python/pip not installed or not in PATH

**Solution**:
- Download Python from python.org
- During installation, check "Add Python to PATH"
- Restart terminal after installation
- Verify: `python --version` and `pip --version`

#### "No module named 'PyPDF2'"
**Problem**: Dependencies not installed

**Solution**:
```bash
pip install -r requirements.txt
```

If that fails, install individually:
```bash
pip install PyPDF2==3.0.1
pip install openai==1.12.0
pip install python-dotenv==1.0.1
```

### 2. API Key Issues

#### "OpenAI API key not found"
**Problem**: .env file missing or not configured

**Solution**:
1. Copy the example file:
   ```bash
   copy .env.example .env
   ```
2. Edit `.env` with a text editor
3. Replace `your_api_key_here` with your actual key
4. Save the file

#### "Incorrect API key provided"
**Problem**: Invalid or expired API key

**Solution**:
- Get a new key from https://platform.openai.com/api-keys
- Make sure you copied the entire key (starts with `sk-`)
- Check for extra spaces or quotes in .env file
- Format should be: `OPENAI_API_KEY=sk-your-key-here`

#### "You exceeded your current quota"
**Problem**: No credits in OpenAI account

**Solution**:
- Add payment method at https://platform.openai.com/account/billing
- Or use a different API key with available credits
- GPT-4o-mini is very cheap (~$0.01 per run)

### 3. PDF Issues

#### "FileNotFoundError: ukpga_20250022_en.pdf"
**Problem**: PDF not in the correct location

**Solution**:
- Make sure the PDF is in the same folder as agent.py
- Check the filename matches exactly (case-sensitive)
- Verify with: `dir ukpga_20250022_en.pdf` (Windows)

#### "PDF extraction returns empty text"
**Problem**: PDF might be image-based or encrypted

**Solution**:
- Check if PDF opens normally in a PDF reader
- If it's a scanned document, you may need OCR
- Try a different PDF extraction library (pdfplumber, PyMuPDF)

### 4. Runtime Errors

#### "JSONDecodeError"
**Problem**: AI returned invalid JSON

**Solution**:
- This is rare but can happen
- Run the script again (AI responses can vary)
- Check your internet connection
- If persistent, the prompt may need adjustment

#### "Rate limit exceeded"
**Problem**: Too many API requests too quickly

**Solution**:
- Wait 60 seconds and try again
- OpenAI has rate limits for new accounts
- Upgrade your OpenAI account tier if needed

#### Script hangs or takes too long
**Problem**: Large PDF or slow API response

**Solution**:
- Be patient - AI analysis takes 1-2 minutes
- Check your internet connection
- Verify OpenAI API status: https://status.openai.com

### 5. Output Issues

#### "output_report.json not created"
**Problem**: Script failed before completion

**Solution**:
- Check error messages in terminal
- Run with verbose output to see where it fails
- Verify all dependencies are installed
- Check API key is valid

#### JSON output looks incomplete
**Problem**: Partial execution or API limits

**Solution**:
- Check if script completed without errors
- Review terminal output for warnings
- Verify the PDF has sufficient content
- Try running again

### 6. Git/GitHub Issues

#### "git: command not found"
**Problem**: Git not installed

**Solution**:
- Download from https://git-scm.com/
- Install with default options
- Restart terminal
- Verify: `git --version`

#### "Permission denied (publickey)"
**Problem**: SSH key not configured

**Solution**:
- Use HTTPS instead of SSH for GitHub
- Or set up SSH keys: https://docs.github.com/en/authentication

#### ".env file visible in GitHub"
**Problem**: .gitignore not working

**Solution**:
- Make sure .gitignore exists
- If .env already committed, remove it:
  ```bash
  git rm --cached .env
  git commit -m "Remove .env from tracking"
  git push
  ```

### 7. Video Recording Issues

#### "Video too large to upload"
**Problem**: File size exceeds limits

**Solution**:
- Use Loom (free, no size limits)
- Compress video with HandBrake
- Upload to YouTube (unlisted)
- Use Google Drive and share link

#### "Video quality is poor"
**Problem**: Low resolution or bad audio

**Solution**:
- Record at 1080p if possible
- Use a good microphone or headset
- Record in a quiet environment
- Test audio before full recording

### 8. Windows-Specific Issues

#### "python: command not found" (but Python is installed)
**Problem**: Python not in PATH or wrong command

**Solution**:
- Try `py` instead of `python`
- Try `python3` instead of `python`
- Add Python to PATH manually

#### Line ending issues in .env
**Problem**: Windows vs Unix line endings

**Solution**:
- Use a proper text editor (VS Code, Notepad++)
- Avoid Windows Notepad
- Save with UTF-8 encoding

### 9. Testing Issues

#### test_setup.py fails
**Problem**: Setup incomplete

**Solution**:
- Read the error messages carefully
- Fix each issue one by one
- Common fixes:
  - Install dependencies
  - Create .env file
  - Add API key
  - Verify PDF exists

### 10. Performance Issues

#### Script is very slow
**Problem**: Large PDF or slow internet

**Solution**:
- Normal runtime is 1-2 minutes
- Check internet speed
- Try at a different time (less API load)
- Consider using a smaller PDF for testing

## Still Having Issues?

### Debug Mode
Add print statements to see where it fails:
```python
print("Starting Task 1...")
# your code
print("Task 1 complete!")
```

### Check Versions
```bash
python --version  # Should be 3.8+
pip --version
pip list  # See all installed packages
```

### Clean Install
If all else fails:
```bash
# Remove virtual environment if you have one
# Reinstall everything fresh
pip uninstall PyPDF2 openai python-dotenv
pip install -r requirements.txt
```

### Get Help
- Check OpenAI documentation: https://platform.openai.com/docs
- PyPDF2 docs: https://pypdf2.readthedocs.io/
- Python docs: https://docs.python.org/

## Prevention Tips

1. **Test early**: Run test_setup.py before the main script
2. **Check logs**: Read error messages carefully
3. **Verify files**: Make sure all files are in place
4. **Test API**: Verify your OpenAI key works
5. **Backup**: Keep a copy of your .env file (securely)
6. **Version control**: Commit often to Git

## Emergency Contacts

If you're stuck and deadline is approaching:
- Review the SETUP_GUIDE.md step by step
- Try on a different computer if available
- Use a cloud environment (Google Colab, Replit)
- Focus on getting ANY output, then refine

Remember: The goal is to demonstrate understanding and capability, not perfection!
