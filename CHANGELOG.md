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

## [1.1.0] - 2024-01-03

### Added
- **Subtitle Translation**: Automatic extraction, translation, and embedding of subtitles
  - Extracts embedded English subtitles from videos
  - Translates all subtitle text to Bengali
  - Embeds Bengali subtitles back into the video
  - Falls back to external SRT file if embedding fails
- **Perfect Audio Dubbing**: Audio is always replaced (no mix mode)
- **Enhanced UI**: Updated interface shows audio replacement and subtitle translation status
- **Comprehensive Subtitle Documentation**: New SUBTITLE_TRANSLATION.md guide

### Changed
- Removed audio mode selection (always replaces with Bengali dubbing)
- Updated UI to show translation features clearly
- Enhanced progress logging for subtitle processing
- Improved error handling for videos without subtitles

### Technical Improvements
- Added FFmpeg-based subtitle extraction
- Implemented SRT parsing and writing
- Added subtitle timing preservation
- Bengali language metadata for subtitles
- Robust fallback for subtitle embedding failures

## [Unreleased]

### Planned Features
- Support for multiple subtitle tracks
- External SRT file input option
- Subtitle timing adjustment
- Batch processing for multiple videos
- Additional language pair support
- Cancel/pause functionality during processing
- Progress percentage indicator
- Video preview before processing
- Custom voice speed controls
- Offline mode support

---

For more details about changes, see the [commit history](https://github.com/yourusername/video-translator/commits).
