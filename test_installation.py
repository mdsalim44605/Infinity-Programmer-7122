#!/usr/bin/env python3
"""
Test script to verify that all dependencies are installed correctly
Run this before using the video translator
"""

import sys

def test_python_version():
    """Check Python version"""
    print("Testing Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 7:
        print(f"✓ Python {version.major}.{version.minor}.{version.micro} - OK")
        return True
    else:
        print(f"✗ Python {version.major}.{version.minor}.{version.micro} - Need 3.7+")
        return False

def test_imports():
    """Test all required imports"""
    print("\nTesting required packages...")
    
    packages = {
        'tkinter': 'tkinter',
        'moviepy': 'moviepy.editor',
        'speech_recognition': 'speech_recognition',
        'googletrans': 'googletrans',
        'gtts': 'gtts',
    }
    
    all_ok = True
    
    for name, module in packages.items():
        try:
            __import__(module)
            print(f"✓ {name} - OK")
        except ImportError as e:
            print(f"✗ {name} - NOT FOUND")
            print(f"  Install with: pip install {name}")
            all_ok = False
    
    return all_ok

def test_ffmpeg():
    """Test if FFmpeg is installed"""
    print("\nTesting FFmpeg...")
    import subprocess
    try:
        result = subprocess.run(
            ['ffmpeg', '-version'],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            version_line = result.stdout.split('\n')[0]
            print(f"✓ FFmpeg - OK ({version_line})")
            return True
        else:
            print("✗ FFmpeg - NOT WORKING")
            return False
    except FileNotFoundError:
        print("✗ FFmpeg - NOT FOUND")
        print("  Please install FFmpeg:")
        print("  - Windows: Download from https://ffmpeg.org/")
        print("  - macOS: brew install ffmpeg")
        print("  - Linux: sudo apt install ffmpeg")
        return False
    except Exception as e:
        print(f"✗ FFmpeg - ERROR: {e}")
        return False

def test_internet():
    """Test internet connection"""
    print("\nTesting internet connection...")
    try:
        import urllib.request
        urllib.request.urlopen('https://www.google.com', timeout=5)
        print("✓ Internet connection - OK")
        return True
    except Exception as e:
        print("✗ Internet connection - FAILED")
        print("  Note: Internet is required for speech recognition and translation")
        return False

def main():
    print("=" * 60)
    print("Video Translator - Installation Test")
    print("=" * 60)
    
    results = []
    
    results.append(("Python Version", test_python_version()))
    results.append(("Required Packages", test_imports()))
    results.append(("FFmpeg", test_ffmpeg()))
    results.append(("Internet Connection", test_internet()))
    
    print("\n" + "=" * 60)
    print("Test Results Summary")
    print("=" * 60)
    
    all_passed = True
    for name, passed in results:
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{name:.<40} {status}")
        if not passed:
            all_passed = False
    
    print("=" * 60)
    
    if all_passed:
        print("\n✓ All tests passed! You're ready to use Video Translator.")
        print("\nRun the application with:")
        print("  python video_translator.py")
    else:
        print("\n✗ Some tests failed. Please fix the issues above before using Video Translator.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
