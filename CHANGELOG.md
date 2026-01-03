# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-01-03

### Added
- Initial release of Video Translator desktop application
- English to Bengali video translation functionality
- Graphical user interface (GUI) using Tkinter
- Speech recognition for English audio
- Google Translate integration for text translation
- Bengali text-to-speech audio generation
- Two audio modes:
  - Replace original audio with Bengali translation
  - Mix Bengali translation with original audio
- Real-time progress logging
- Support for multiple video formats (MP4, AVI, MOV, MKV, FLV, WMV)
- Auto-suggestion for output file paths
- Comprehensive documentation:
  - README.md with full documentation
  - QUICKSTART.md for quick setup
  - CONTRIBUTING.md for contributors
  - Installation test script (test_installation.py)
  - Example usage code (example_usage.py)
- Python package setup (setup.py)
- Dependencies management (requirements.txt)
- MIT License
- .gitignore for Python projects

### Technical Details
- Python 3.7+ support
- MoviePy for video processing
- SpeechRecognition for audio transcription
- googletrans for translation API
- gTTS for Bengali audio synthesis
- FFmpeg integration for video encoding

### Known Limitations
- Requires internet connection for translation services
- Processing time depends on video length
- Best results with clear English speech
- Free API usage limits may apply

## [Unreleased]

### Planned Features
- Subtitle generation (SRT files)
- Batch processing for multiple videos
- Additional language pair support
- Cancel/pause functionality during processing
- Progress percentage indicator
- Video preview before processing
- Custom voice speed controls
- Offline mode support

---

For more details about changes, see the [commit history](https://github.com/yourusername/video-translator/commits).
