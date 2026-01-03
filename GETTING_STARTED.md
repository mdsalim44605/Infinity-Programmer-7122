# Getting Started with Video Translator

Welcome to Video Translator! This guide will help you get up and running in just a few minutes.

## 📋 Table of Contents

1. [Quick Start](#quick-start)
2. [Installation](#installation)
3. [First Translation](#first-translation)
4. [Understanding the Interface](#understanding-the-interface)
5. [Tips & Best Practices](#tips--best-practices)
6. [Next Steps](#next-steps)

---

## 🚀 Quick Start

**5-Minute Setup:**

```bash
# 1. Install FFmpeg (choose your OS)
# Windows: Download from https://ffmpeg.org/
# macOS:
brew install ffmpeg
# Linux:
sudo apt install ffmpeg

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Verify installation
python test_installation.py

# 4. Run the application
python video_translator.py
```

**That's it!** 🎉

---

## 💾 Installation

### Prerequisites

Before you begin, ensure you have:

- [x] **Python 3.7+** - [Download here](https://www.python.org/downloads/)
- [x] **FFmpeg** - Video processing tool
- [x] **Internet connection** - Required for translation APIs
- [x] **2GB RAM** minimum (4GB recommended)

### Step-by-Step Installation

#### Step 1: Install Python

1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. ✅ **Important**: Check "Add Python to PATH"
4. Verify installation:
   ```bash
   python --version
   # Should show Python 3.7 or higher
   ```

#### Step 2: Install FFmpeg

<details>
<summary><b>Windows</b></summary>

1. Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html)
2. Extract to `C:\ffmpeg`
3. Add to PATH:
   - Open "Environment Variables"
   - Edit "Path" variable
   - Add `C:\ffmpeg\bin`
4. Restart Command Prompt
5. Verify: `ffmpeg -version`

</details>

<details>
<summary><b>macOS</b></summary>

```bash
# Using Homebrew (recommended)
brew install ffmpeg

# Verify
ffmpeg -version
```

</details>

<details>
<summary><b>Linux</b></summary>

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install ffmpeg

# Fedora/CentOS
sudo yum install ffmpeg

# Verify
ffmpeg -version
```

</details>

#### Step 3: Clone/Download the Project

```bash
# Clone with git
git clone <repository-url>
cd video-translator

# Or download ZIP and extract
```

#### Step 4: Install Python Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- moviepy (video processing)
- SpeechRecognition (speech-to-text)
- googletrans (translation)
- gTTS (text-to-speech)
- And supporting libraries

#### Step 5: Verify Installation

```bash
python test_installation.py
```

You should see:
```
✓ Python Version - OK
✓ Required Packages - OK
✓ FFmpeg - OK
✓ Internet Connection - OK
```

If any tests fail, follow the instructions provided.

---

## 🎬 First Translation

Let's translate your first video!

### 1. Launch the Application

```bash
python video_translator.py
```

A window will open with the Video Translator interface.

### 2. Select Your Video

1. Click **"Browse Video"** button
2. Navigate to your English video file
3. Select it and click Open

**Supported formats:** MP4, AVI, MOV, MKV, FLV, WMV

### 3. Choose Output Location

- The app auto-suggests: `original_name_bengali.mp4`
- Click **"Choose Output Location"** to change it (optional)

### 4. Select Audio Mode

**Replace Original Audio** (Recommended for first try)
- Completely replaces English with Bengali
- Best for full translation

**Mix with Original**
- English at 30% + Bengali at 70%
- Useful for learning or comparison

### 5. Start Translation

1. Click **"Translate Video"**
2. Watch the progress log for updates:
   ```
   Step 1: Loading video file...
   Step 2: Extracting audio...
   Step 3: Transcribing English audio...
   Step 4: Translating to Bengali...
   Step 5: Generating Bengali audio...
   Step 6: Combining video with audio...
   Step 7: Writing output video...
   ✓ Translation completed!
   ```

### 6. Done!

A success dialog will appear. Your translated video is ready!

---

## 🖥️ Understanding the Interface

```
┌─────────────────────────────────────────────┐
│    Video Translator - English to Bengali    │
├─────────────────────────────────────────────┤
│                                             │
│  ┌─ Input Video ──────────────────────┐   │
│  │ No file selected                    │   │
│  │ [Browse Video]                      │   │
│  └─────────────────────────────────────┘   │
│                                             │
│  ┌─ Output Video ─────────────────────┐   │
│  │ No output path selected             │   │
│  │ [Choose Output Location]            │   │
│  └─────────────────────────────────────┘   │
│                                             │
│  ┌─ Options ──────────────────────────┐   │
│  │ Audio Mode:                         │   │
│  │ ● Replace Original Audio            │   │
│  │ ○ Mix with Original                 │   │
│  │                                     │   │
│  │ Progress Log:                       │   │
│  │ ┌───────────────────────────────┐  │   │
│  │ │ Log messages appear here...   │  │   │
│  │ │                               │  │   │
│  │ └───────────────────────────────┘  │   │
│  │ [========Progress Bar=========]     │   │
│  └─────────────────────────────────────┘   │
│                                             │
│       [Translate Video]    [Exit]          │
└─────────────────────────────────────────────┘
```

### Interface Elements

| Element | Purpose |
|---------|---------|
| **Browse Video** | Select input video file |
| **Choose Output Location** | Set where to save translated video |
| **Audio Mode** | Choose Replace or Mix |
| **Progress Log** | See real-time updates |
| **Progress Bar** | Visual indication of processing |
| **Translate Video** | Start the translation |

---

## 💡 Tips & Best Practices

### For Best Results

✅ **DO:**
- Start with short videos (1-2 minutes) to test
- Use videos with clear, slow English speech
- Ensure stable internet connection
- Use MP4 format when possible
- Check audio quality before processing
- Close other heavy applications

❌ **DON'T:**
- Don't use videos with heavy background music
- Don't translate very long videos on first try
- Don't use videos with poor audio quality
- Don't interrupt the process (can't cancel yet)
- Don't expect instant results (it takes time!)

### Choosing the Right Audio Mode

**Use "Replace Original Audio" when:**
- You want pure Bengali audio
- Original audio isn't important
- Creating content for Bengali speakers
- Dubbing movies or tutorials

**Use "Mix with Original" when:**
- Learning Bengali
- Need to hear both languages
- Comparing translations
- Original audio provides context (music, effects)

### Expected Processing Times

| Video Length | Approximate Time |
|--------------|-----------------|
| 30 seconds   | 1-2 minutes     |
| 1 minute     | 2-5 minutes     |
| 5 minutes    | 10-20 minutes   |
| 10 minutes   | 20-40 minutes   |

*Times vary based on video quality, internet speed, and computer performance*

---

## 🎯 Next Steps

Now that you've completed your first translation, explore more:

### Learn More

- 📖 **[README.md](README.md)** - Complete documentation
- 🏗️ **[ARCHITECTURE.md](ARCHITECTURE.md)** - Technical details
- 🔄 **[WORKFLOW.md](WORKFLOW.md)** - How it works
- ❓ **[FAQ.md](FAQ.md)** - Common questions
- 🤝 **[CONTRIBUTING.md](CONTRIBUTING.md)** - Contribute to the project

### Try Advanced Features

1. **Mix Audio Mode** - Combine English and Bengali
2. **Different Video Formats** - Test with AVI, MOV, etc.
3. **Longer Videos** - Gradually increase video length
4. **Batch Processing** - Translate multiple videos (one at a time)

### Troubleshooting

Having issues? Check these resources:

1. **[FAQ.md](FAQ.md)** - Answers to common problems
2. **[README.md](README.md)** - Troubleshooting section
3. **Run diagnostic**: `python test_installation.py`
4. **Open an issue** on GitHub

### Share Your Experience

- ⭐ Star the project on GitHub
- 🐛 Report bugs or issues
- 💡 Suggest new features
- 🤝 Contribute code or documentation
- 📢 Share with others who might benefit

---

## 📚 Quick Reference

### Common Commands

```bash
# Run the application
python video_translator.py

# Test installation
python test_installation.py

# View examples
python example_usage.py

# Install dependencies
pip install -r requirements.txt

# Update dependencies
pip install -r requirements.txt --upgrade
```

### File Locations

```
video-translator/
├── video_translator.py      # Main application
├── test_installation.py     # Diagnostic tool
├── example_usage.py         # Usage examples
├── requirements.txt         # Dependencies
└── *.md                     # Documentation
```

### Getting Help

1. **Read the docs**: Start with [README.md](README.md)
2. **Check FAQ**: See [FAQ.md](FAQ.md)
3. **Run diagnostics**: `python test_installation.py`
4. **Open an issue**: Report problems on GitHub
5. **Join discussions**: Participate in community discussions

---

## 🎉 You're Ready!

Congratulations! You now know how to:
- ✅ Install and set up Video Translator
- ✅ Translate your first video
- ✅ Use the interface effectively
- ✅ Apply best practices
- ✅ Find help when needed

**Happy translating!** 🌐🎥

---

**Need help?** Check [FAQ.md](FAQ.md) or open an issue on GitHub.
