# Frequently Asked Questions (FAQ)

## General Questions

### Q: What is Video Translator?
**A:** Video Translator is a free desktop application that translates video audio from English to Bengali. It extracts the audio, transcribes it, translates the text, generates Bengali speech, and creates a new video with the translated audio.

### Q: Is it really free?
**A:** Yes! The application is completely free and open-source. It uses free Google APIs for speech recognition, translation, and text-to-speech.

### Q: What platforms does it support?
**A:** Video Translator works on:
- ✅ Windows (7, 8, 10, 11)
- ✅ macOS (10.12+)
- ✅ Linux (Ubuntu, Debian, Fedora, etc.)

### Q: Do I need an internet connection?
**A:** Yes, an active internet connection is required because the application uses online APIs for:
- Speech recognition (transcription)
- Translation
- Text-to-speech generation

---

## Installation Questions

### Q: What are the system requirements?
**A:**
- Python 3.7 or higher
- 2GB RAM minimum (4GB recommended)
- 500MB free disk space
- Internet connection
- FFmpeg installed

### Q: How do I install Python?
**A:** Download from [python.org](https://www.python.org/downloads/) and follow the installation wizard. Make sure to check "Add Python to PATH" during installation on Windows.

### Q: How do I install FFmpeg?

**Windows:**
1. Download from [ffmpeg.org](https://ffmpeg.org/download.html)
2. Extract to `C:\ffmpeg`
3. Add `C:\ffmpeg\bin` to system PATH

**macOS:**
```bash
brew install ffmpeg
```

**Linux:**
```bash
sudo apt install ffmpeg  # Ubuntu/Debian
sudo yum install ffmpeg  # CentOS/Fedora
```

### Q: I get "ModuleNotFoundError" when running the app
**A:** You need to install the Python dependencies:
```bash
pip install -r requirements.txt
```

### Q: How do I verify my installation?
**A:** Run the test script:
```bash
python test_installation.py
```

---

## Usage Questions

### Q: What video formats are supported?
**A:** Supported formats include:
- MP4 (recommended)
- AVI
- MOV
- MKV
- FLV
- WMV

### Q: How long does translation take?
**A:** Processing time varies:
- 1-minute video: ~2-5 minutes
- 5-minute video: ~10-20 minutes
- 10-minute video: ~20-40 minutes

Factors: video length, internet speed, computer performance

### Q: What's the difference between "Replace" and "Mix" audio modes?

**Replace Original Audio:**
- Completely removes English audio
- Only Bengali audio plays
- Best for full translation

**Mix with Original:**
- Keeps original English at 30% volume
- Bengali audio at 70% volume
- Useful for learning or comparison

### Q: Can I translate long videos (1+ hours)?
**A:** Technically yes, but:
- Processing will take a very long time
- May hit API rate limits
- Consider breaking into smaller segments
- Recommended max: 10-15 minutes per video

### Q: Can I cancel processing once it starts?
**A:** Currently, no. Once translation starts, it must complete or fail. This is a planned feature for future versions.

---

## Troubleshooting

### Q: "Could not understand audio" error
**A:** This means speech recognition failed. Try:
- Ensure video has clear English speech
- Reduce background noise/music
- Check audio volume levels
- Test with a different video
- Verify internet connection

### Q: "FFmpeg not found" error
**A:** 
1. Verify FFmpeg is installed: `ffmpeg -version`
2. Add FFmpeg to system PATH
3. Restart terminal/command prompt
4. Try installation again

### Q: Translation takes forever / hangs
**A:** Possible causes:
- Slow internet connection
- Very long video
- API rate limiting
- Computer performance

**Solutions:**
- Check internet speed
- Try shorter videos first
- Close other applications
- Restart the application

### Q: Poor audio quality in output
**A:** 
- Use higher quality input videos
- Ensure clear source audio
- Check if original audio has issues
- gTTS has limitations on voice quality

### Q: Video and audio out of sync
**A:** This is rare but can happen:
- Use MP4 format for best results
- Ensure input video isn't corrupted
- Check FFmpeg version is up to date
- Report as a bug if persistent

### Q: "Translation failed" error
**A:** Usually means:
- Internet connection lost
- API rate limit reached
- Invalid/corrupted audio
- Service temporarily unavailable

**Solution:** Wait a few minutes and try again

---

## Feature Questions

### Q: Can I translate to languages other than Bengali?
**A:** Not in the current version, but this is a planned feature. You can modify the code to add other languages supported by gTTS.

### Q: Can I translate from languages other than English?
**A:** Not currently. The app is specifically designed for English to Bengali translation.

### Q: Can I add subtitles instead of replacing audio?
**A:** Subtitle generation is not currently available but is a planned feature for future versions.

### Q: Can I batch process multiple videos?
**A:** Not in the current version. You must process videos one at a time. Batch processing is planned for a future release.

### Q: Can I customize the Bengali voice?
**A:** gTTS provides a standard Bengali voice. Custom voice options are not available in the free version.

### Q: Can I adjust translation speed or pitch?
**A:** Not currently. The gTTS API uses standard speed. This could be a future enhancement.

---

## Technical Questions

### Q: Is my data/video uploaded anywhere?
**A:** The video file stays on your computer. Only the audio is:
- Sent to Google Speech Recognition (transcription)
- Sent to Google Translate (translation)
- Used by Google TTS (audio generation)

### Q: How much data does it use?
**A:** Approximate data usage per minute of video:
- Speech recognition: ~2-5 MB
- Translation: <1 MB
- Text-to-speech: ~1-2 MB
- **Total: ~4-8 MB per minute**

### Q: Can I use this offline?
**A:** No, internet is required for the APIs. Offline mode would require local models and is not currently supported.

### Q: What quality is the output video?
**A:** Output video maintains:
- Original video quality
- Original resolution
- Original frame rate
- Audio: AAC codec at standard quality

### Q: Does it preserve video metadata?
**A:** Basic metadata is preserved, but some advanced metadata may be lost during re-encoding.

### Q: Is the translation accurate?
**A:** Translation quality depends on Google Translate:
- Generally good for clear, standard language
- May struggle with idioms or slang
- Best for straightforward speech
- Not professional-grade translation

---

## Licensing & Usage

### Q: Can I use this commercially?
**A:** Yes! The MIT License allows commercial use. However, be aware:
- Google APIs have usage limits
- Consider paid APIs for commercial scale

### Q: Can I modify the code?
**A:** Yes! It's open source under MIT License. You can:
- Modify for personal use
- Add features
- Redistribute (with attribution)

### Q: Can I contribute to the project?
**A:** Absolutely! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Q: Who made this?
**A:** Created by Infinity-Programmer. Contributions welcome!

---

## Performance Questions

### Q: Why is processing so slow?
**A:** Video processing is computationally intensive:
- Audio extraction
- API calls (network latency)
- Video re-encoding
- File I/O operations

### Q: Can I speed it up?
**A:** Some tips:
- Use MP4 format (fastest)
- Use shorter videos
- Ensure fast internet
- Close other applications
- Use SSD instead of HDD

### Q: How much CPU does it use?
**A:** CPU usage varies:
- Light during transcription/translation
- Heavy during video encoding (60-80%)
- Depends on FFmpeg settings

### Q: Does it support GPU acceleration?
**A:** Not currently. FFmpeg can use GPU acceleration, but it's not enabled by default. This could be a future enhancement.

---

## Future Features

### Q: What features are planned?
**A:** Upcoming features include:
- [ ] Multiple language pairs
- [ ] Subtitle generation
- [ ] Batch processing
- [ ] Cancel/pause functionality
- [ ] Progress percentage
- [ ] Custom voice options
- [ ] Offline mode
- [ ] GPU acceleration

### Q: When will [feature] be available?
**A:** The project is open source and community-driven. Feature development depends on:
- Community contributions
- Developer availability
- Technical feasibility

Check [CHANGELOG.md](CHANGELOG.md) for updates.

---

## Getting Help

### Q: I have a problem not listed here
**A:** 
1. Check the [README.md](README.md) troubleshooting section
2. Run `python test_installation.py` to diagnose issues
3. Review [ARCHITECTURE.md](ARCHITECTURE.md) for technical details
4. Open an issue on GitHub with:
   - Your operating system
   - Python version
   - Error message
   - Steps to reproduce

### Q: How can I report a bug?
**A:** Open an issue on GitHub with:
- Clear description of the bug
- Steps to reproduce
- Expected vs actual behavior
- System information
- Error logs if available

### Q: How can I request a feature?
**A:** Open an issue on GitHub labeled "feature request" with:
- Feature description
- Use case
- Why it would be valuable

---

## Additional Resources

- **Quick Start**: [QUICKSTART.md](QUICKSTART.md)
- **Full Documentation**: [README.md](README.md)
- **Architecture**: [ARCHITECTURE.md](ARCHITECTURE.md)
- **Contributing**: [CONTRIBUTING.md](CONTRIBUTING.md)
- **Workflow**: [WORKFLOW.md](WORKFLOW.md)

---

**Still have questions?** Open an issue on GitHub!
