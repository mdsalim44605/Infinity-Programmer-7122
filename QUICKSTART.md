# Quick Start Guide

Get started with Video Translator in just 5 minutes!

## Step 1: Install Python

Make sure you have Python 3.7 or higher installed:

```bash
python --version
# or
python3 --version
```

If not installed, download from [python.org](https://www.python.org/downloads/)

## Step 2: Install FFmpeg

### Windows
Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH

### macOS
```bash
brew install ffmpeg
```

### Linux
```bash
sudo apt install ffmpeg
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 4: Run the Application

```bash
python video_translator.py
```

## Step 5: Translate Your First Video

1. Click **"Browse Video"** and select your English video
2. Click **"Choose Output Location"** (or use the auto-suggested path)
3. Choose audio mode:
   - **Replace Original Audio**: For complete translation
   - **Mix with Original**: To hear both languages
4. Click **"Translate Video"**
5. Wait for the process to complete
6. Find your translated video at the output location!

## Tips for Best Results

✅ **DO:**
- Use videos with clear English speech
- Ensure stable internet connection
- Start with shorter videos (under 5 minutes) for testing
- Use MP4 format when possible

❌ **DON'T:**
- Use videos with heavy background music/noise
- Translate very long videos without testing first
- Expect real-time processing (it takes time!)

## Common Issues

### "FFmpeg not found"
- Make sure FFmpeg is installed and in your system PATH
- Restart your terminal after installation

### "Could not understand audio"
- Check that the video has clear speech
- Reduce background noise
- Try a different video

### Slow Processing
- Normal! Video processing is time-consuming
- Time varies based on video length
- A 1-minute video might take 2-5 minutes to process

## Need Help?

Check the full [README.md](README.md) for detailed documentation.

---

**Enjoy translating! 🎥🌐**
