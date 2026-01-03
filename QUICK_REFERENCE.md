# Quick Reference Guide

## 🚀 Quick Start

```bash
# 1. Install FFmpeg
brew install ffmpeg  # macOS
sudo apt install ffmpeg  # Linux

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run application
python video_translator.py
```

## 📹 Video Translation Process

### What Happens:
1. **Audio**: English → Bengali (replaces original)
2. **Subtitles**: English → Bengali (if present)

### Steps:
1. Click **"Browse Video"** → Select video
2. Click **"Translate Video"**
3. Wait for completion
4. Done! ✅

## 🎯 Features

| Feature | Status |
|---------|--------|
| Audio Dubbing | ✅ Always replaced |
| Subtitle Translation | ✅ Automatic |
| Local File Upload | ✅ Browse button |
| Progress Tracking | ✅ Real-time |
| Multiple Formats | ✅ MP4, MKV, AVI, MOV |

## 📝 Subtitle Support

### Videos WITH Subtitles:
- ✅ Subtitles extracted
- ✅ Translated to Bengali
- ✅ Embedded in output video
- ✅ Or saved as `.srt` file

### Videos WITHOUT Subtitles:
- ✅ Audio still dubbed
- ℹ️ Note: "No subtitles to process"
- ✅ Everything else works

## ⏱️ Processing Time

| Video Length | Est. Time |
|-------------|-----------|
| 1 minute | 2-5 min |
| 5 minutes | 10-20 min |
| 10 minutes | 20-40 min |

*Add ~30 sec for subtitle translation*

## 🎬 Output

### You Get:
- `video_bengali.mp4` - Video with Bengali audio
- Bengali subtitles (embedded or as `.srt`)

### Quality:
- ✅ Original video quality maintained
- ✅ Professional Bengali dubbing
- ✅ Perfectly timed subtitles

## 🆘 Common Issues

| Issue | Solution |
|-------|----------|
| FFmpeg not found | Install FFmpeg, restart terminal |
| Could not understand audio | Use video with clear speech |
| Slow processing | Normal! Video processing takes time |
| No subtitles found | Video has no embedded subtitles (OK!) |

## 📖 Full Documentation

- **[README.md](README.md)** - Complete guide
- **[SUBTITLE_TRANSLATION.md](SUBTITLE_TRANSLATION.md)** - Subtitle details
- **[GETTING_STARTED.md](GETTING_STARTED.md)** - Setup guide
- **[FAQ.md](FAQ.md)** - Common questions

## 💡 Tips

### Best Results:
✅ Clear English speech  
✅ Stable internet  
✅ MP4 format  
✅ Videos with embedded subtitles

### Avoid:
❌ Heavy background music  
❌ Very long videos (start small)  
❌ Poor audio quality  
❌ Hardcoded subtitles

## 🎓 Example Workflow

```
Input:
  tutorial.mp4 (5 min, with English subtitles)

Processing:
  [=========>] 10-15 minutes

Output:
  tutorial_bengali.mp4
  - Bengali audio dubbing ✅
  - Bengali subtitles ✅
  - Ready to watch! 🎉
```

## 🔧 Requirements

- Python 3.7+
- FFmpeg
- Internet connection
- 2GB RAM minimum

## ⚡ One-Line Commands

```bash
# Install everything
pip install -r requirements.txt && python video_translator.py

# Test installation
python test_installation.py

# View examples
python example_usage.py
```

## 🌟 Version 1.1 Highlights

- ✅ **Automatic subtitle translation**
- ✅ **Perfect Bengali dubbing**
- ✅ **Simplified UI**
- ✅ **Smart subtitle detection**
- ✅ **Complete Bengali experience**

## 📞 Need Help?

1. Check [FAQ.md](FAQ.md)
2. Run `python test_installation.py`
3. Read full documentation
4. Open GitHub issue

---

**Quick, Easy, Complete Bengali Translation!** 🎬🌐
