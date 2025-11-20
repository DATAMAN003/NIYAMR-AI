"""Quick test to verify setup before running the main agent"""
import sys
import os

def test_dependencies():
    """Test if all required packages are installed"""
    print("Testing dependencies...")
    try:
        import PyPDF2
        print("  ✓ PyPDF2 installed")
    except ImportError:
        print("  ✗ PyPDF2 not found - run: pip install -r requirements.txt")
        return False
    
    try:
        import groq
        print("  ✓ Groq installed")
    except ImportError:
        print("  ✗ Groq not found - run: pip install -r requirements.txt")
        return False
    
    try:
        import dotenv
        print("  ✓ python-dotenv installed")
    except ImportError:
        print("  ✗ python-dotenv not found - run: pip install -r requirements.txt")
        return False
    
    return True

def test_env_file():
    """Test if .env file exists and has API key"""
    print("\nTesting environment configuration...")
    if not os.path.exists('.env'):
        print("  ✗ .env file not found")
        print("    → Copy .env.example to .env and add your OpenAI API key")
        return False
    
    print("  ✓ .env file exists")
    
    from dotenv import load_dotenv
    load_dotenv()
    
    api_key = os.getenv('GROQ_API_KEY')
    if not api_key or api_key == 'your_groq_api_key_here':
        print("  ✗ GROQ_API_KEY not configured")
        print("    → Edit .env and add your actual Groq API key")
        return False
    
    print("  ✓ GROQ_API_KEY configured")
    return True

def test_pdf_exists():
    """Test if PDF file exists"""
    print("\nTesting PDF file...")
    if not os.path.exists('ukpga_20250022_en.pdf'):
        print("  ✗ ukpga_20250022_en.pdf not found")
        print("    → Make sure the PDF is in the same folder")
        return False
    
    print("  ✓ PDF file found")
    return True

def main():
    print("="*60)
    print("SETUP VERIFICATION TEST")
    print("="*60 + "\n")
    
    deps_ok = test_dependencies()
    env_ok = test_env_file()
    pdf_ok = test_pdf_exists()
    
    print("\n" + "="*60)
    if deps_ok and env_ok and pdf_ok:
        print("✅ ALL TESTS PASSED - Ready to run agent.py!")
        print("="*60)
        print("\nRun: python agent.py")
        return 0
    else:
        print("❌ SOME TESTS FAILED - Fix issues above before running")
        print("="*60)
        return 1

if __name__ == "__main__":
    sys.exit(main())
