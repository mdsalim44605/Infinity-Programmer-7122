# Video Translator - English to Bengali

A free desktop application built with Python that translates video audio from English to Bengali. This tool extracts audio from videos, transcribes English speech, translates it to Bengali, generates Bengali audio, and produces a new video with the translated audio.

## 📚 Documentation

- **[Getting Started](GETTING_STARTED.md)** - New users start here!
- **[Quick Start Guide](QUICKSTART.md)** - 5-minute setup
- **[FAQ](FAQ.md)** - Frequently asked questions
- **[Architecture](ARCHITECTURE.md)** - Technical documentation
- **[Workflow](WORKFLOW.md)** - How the translation process works
- **[Contributing](CONTRIBUTING.md)** - Contribution guidelines
- **[Changelog](CHANGELOG.md)** - Version history

## Features

- 🎥 **Video Processing**: Supports multiple video formats (MP4, AVI, MOV, MKV, FLV, WMV)
- 🗣️ **Speech Recognition**: Automatic English speech-to-text transcription
- 🌐 **Translation**: English to Bengali text translation
- 🔊 **Text-to-Speech**: Bengali audio generation
- 🎚️ **Audio Modes**: 
  - Replace original audio completely
  - Mix Bengali audio with original audio
- 🖥️ **User-Friendly GUI**: Easy-to-use desktop interface
- 📝 **Progress Logging**: Real-time progress updates and logs

## Prerequisites

- Python 3.7 or higher
- Internet connection (required for speech recognition and translation services)
- FFmpeg (required for video processing)

## Installation

### 1. Install FFmpeg

**Windows:**
```bash
# Download from https://ffmpeg.org/download.html
# Or use chocolatey:
choco install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install ffmpeg
```

### 2. Clone the Repository

```bash
git clone <repository-url>
cd <repository-name>
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Run the Application

```bash
python video_translator.py
```

### Step-by-Step Guide

1. **Launch the Application**: Run `python video_translator.py`

2. **Select Input Video**:
   - Click "Browse Video" button
   - Choose your English video file

3. **Choose Output Location**:
   - Click "Choose Output Location" button
   - Select where to save the translated video
   - (Optional: Output location is auto-suggested based on input file)

4. **Select Audio Mode**:
   - **Replace Original Audio**: Completely replaces English audio with Bengali
   - **Mix with Original**: Combines both audios (original at 30%, Bengali at 70%)

5. **Start Translation**:
   - Click "Translate Video" button
   - Monitor progress in the log window
   - Wait for completion (time depends on video length)

6. **Done!**: Your translated video will be saved to the output location

## How It Works

1. **Extract Audio**: Extracts audio track from the input video
2. **Transcribe**: Converts English speech to text using Google Speech Recognition
3. **Translate**: Translates English text to Bengali using Google Translate
4. **Generate Audio**: Creates Bengali audio from translated text using gTTS
5. **Combine**: Merges the video with the new Bengali audio track
6. **Export**: Saves the final translated video

## Technical Details

### Architecture

- **GUI Framework**: Tkinter (Python's standard GUI library)
- **Video Processing**: MoviePy
- **Speech Recognition**: Google Speech Recognition API
- **Translation**: Google Translate API (via googletrans)
- **Text-to-Speech**: Google Text-to-Speech (gTTS)

### Supported Video Formats

- MP4 (recommended)
- AVI
- MOV
- MKV
- FLV
- WMV

### Limitations

- Requires internet connection for speech recognition and translation
- Best results with clear English speech
- Processing time depends on video length
- Free API usage limits may apply for very large videos

## Troubleshooting

### "Could not understand audio"
- Ensure the video has clear English speech
- Check that audio quality is good
- Try videos with less background noise

### FFmpeg Not Found
- Make sure FFmpeg is installed and in your system PATH
- Restart terminal/command prompt after installing FFmpeg

### Internet Connection Issues
- Verify you have a stable internet connection
- Some firewalls may block API requests

### Module Import Errors
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Try upgrading pip: `pip install --upgrade pip`

## Dependencies

- **moviepy**: Video editing and processing
- **SpeechRecognition**: Speech-to-text conversion
- **googletrans**: Translation service
- **gTTS**: Text-to-speech for Bengali
- **pydub**: Audio processing utilities
- **numpy**: Numerical operations
- **imageio**: Image and video I/O
- **imageio-ffmpeg**: FFmpeg integration

## Future Enhancements

- [ ] Support for more language pairs
- [ ] Subtitle generation
- [ ] Batch processing multiple videos
- [ ] Advanced audio synchronization
- [ ] Custom voice options
- [ ] Offline mode support
- [ ] GPU acceleration for faster processing

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This project is open-source and available for free use under the MIT License. See [LICENSE](LICENSE) for details.

## Acknowledgments

- Google Speech Recognition API
- Google Translate API
- Google Text-to-Speech (gTTS)
- MoviePy library
- Python community

## Support

For issues, questions, or suggestions, please open an issue in the repository.

---

**Note**: This tool uses free online services for speech recognition and translation. For production use or high-volume processing, consider using paid API services for better reliability and fewer limitations.
