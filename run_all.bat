@echo off
echo ================================================================
echo    UNIVERSAL CREDIT ACT 2025 - AI AGENT
echo    NIYAMR 48-Hour Internship Assignment
echo ================================================================
echo.

echo [1/3] Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo.

echo [2/3] Testing setup...
python test_setup.py
if errorlevel 1 (
    echo ERROR: Setup test failed. Please fix issues above.
    pause
    exit /b 1
)
echo.

echo [3/3] Running AI Agent...
python agent.py
if errorlevel 1 (
    echo ERROR: Agent execution failed
    pause
    exit /b 1
)
echo.

echo ================================================================
echo    SUCCESS! Check these files:
echo    - output_report.json (complete analysis)
echo    - extracted_text.txt (raw PDF text)
echo ================================================================
echo.
echo.
pause
