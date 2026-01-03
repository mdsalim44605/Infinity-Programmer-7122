# Architecture Documentation

## Overview

Video Translator is a desktop application that translates video audio from English to Bengali. This document describes the system architecture, components, and data flow.

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                       User Interface (Tkinter)               │
│  - File selection dialogs                                    │
│  - Progress display                                          │
│  - Audio mode selection                                      │
│  - Log viewer                                                │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│              VideoTranslatorApp (Main Controller)            │
│  - Event handling                                            │
│  - Thread management                                         │
│  - Workflow orchestration                                    │
└─────────────────────┬───────────────────────────────────────┘
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
┌──────────────────┐    ┌──────────────────┐
│  Video Processing│    │  Audio Processing│
│    (MoviePy)     │    │  (SpeechRec/gTTS)│
└──────────────────┘    └──────────────────┘
          │                       │
          ▼                       ▼
┌──────────────────┐    ┌──────────────────┐
│   FFmpeg         │    │  Google APIs     │
│   (External)     │    │  (External)      │
└──────────────────┘    └──────────────────┘
```

## Component Breakdown

### 1. User Interface Layer

**File**: `video_translator.py` (class `VideoTranslatorApp.__init__` and `setup_ui`)

**Responsibilities**:
- Display application window
- Handle user input (file selection, buttons)
- Show progress and logs
- Manage UI state (enable/disable buttons)

**Key UI Components**:
- Input video browser
- Output location selector
- Audio mode radio buttons (Replace/Mix)
- Progress log (ScrolledText)
- Progress bar (indeterminate)
- Translate button
- Exit button

### 2. Controller Layer

**File**: `video_translator.py` (class `VideoTranslatorApp`)

**Responsibilities**:
- Coordinate between UI and processing layers
- Manage application state
- Handle threading for non-blocking operations
- Error handling and user notifications

**Key Methods**:
- `start_translation()` - Initiates translation workflow
- `translate_video()` - Main translation orchestrator
- `log_message()` - Updates UI with progress

### 3. Video Processing Layer

**Technologies**: MoviePy, FFmpeg

**Workflow**:
```
Video File → Load Video → Extract Audio → Process → Combine with New Audio → Export
```

**Key Operations**:
- Load video with `VideoFileClip()`
- Extract audio track
- Create new audio track
- Mix or replace audio
- Export final video with `write_videofile()`

### 4. Audio Processing Layer

**Components**:

#### a. Speech-to-Text (Transcription)
- **Library**: SpeechRecognition
- **API**: Google Speech Recognition
- **Input**: WAV audio file
- **Output**: English text transcript

#### b. Translation
- **Library**: googletrans
- **API**: Google Translate
- **Input**: English text
- **Output**: Bengali text

#### c. Text-to-Speech (Synthesis)
- **Library**: gTTS (Google Text-to-Speech)
- **Input**: Bengali text
- **Output**: MP3 audio file

## Data Flow

### Complete Translation Pipeline

```
1. User selects video
   ↓
2. Extract audio from video
   ↓
3. Convert audio to WAV format
   ↓
4. Transcribe audio to English text
   (Google Speech Recognition API)
   ↓
5. Translate English text to Bengali
   (Google Translate API)
   ↓
6. Generate Bengali audio from text
   (Google TTS API)
   ↓
7. Combine video with Bengali audio
   (Mix or Replace based on user choice)
   ↓
8. Export final video with new audio
   ↓
9. Save to user-specified location
```

## Threading Model

**Main Thread**:
- Runs Tkinter event loop
- Handles UI updates
- Responds to user interactions

**Worker Thread**:
- Executes `translate_video()` method
- Performs all heavy processing
- Communicates with main thread via `root.after()`

**Benefits**:
- Non-blocking UI during processing
- Responsive interface
- Progress updates in real-time

## File Management

### Temporary Files

The application uses Python's `tempfile.TemporaryDirectory()` for intermediate files:

```python
temp_dir/
├── temp_audio.wav      # Extracted audio from video
└── bengali_audio.mp3   # Generated Bengali audio
```

**Cleanup**: Temporary directory is automatically deleted after processing.

### Output Files

- Format: MP4 (H.264 video codec, AAC audio codec)
- Naming: User-specified or auto-suggested (`<original>_bengali.mp4`)

## Dependencies

### Core Dependencies

```
moviepy==1.0.3          # Video processing
SpeechRecognition==3.10.1  # Speech-to-text
googletrans==4.0.0rc1    # Translation
gTTS==2.5.0             # Text-to-speech
```

### Supporting Libraries

```
pydub==0.25.1           # Audio utilities
numpy==1.24.3           # Numerical operations
imageio==2.33.1         # Image/video I/O
imageio-ffmpeg==0.4.9   # FFmpeg wrapper
```

### External Dependencies

- **FFmpeg**: Required for video encoding/decoding
- **Internet**: Required for Google APIs

## Error Handling

### Error Categories

1. **User Input Errors**
   - Missing input/output files
   - Invalid file paths
   - Handled with: `messagebox.showerror()`

2. **Processing Errors**
   - Audio transcription failures
   - Translation API errors
   - Audio generation errors
   - Handled with: Try-except blocks, logged to UI

3. **System Errors**
   - FFmpeg not found
   - Network issues
   - Disk space issues
   - Handled with: Exception catching, user notifications

## Performance Considerations

### Processing Time

Typical processing time for a 1-minute video:
- Extract audio: ~5 seconds
- Transcribe: ~10-20 seconds
- Translate: ~1-2 seconds
- Generate audio: ~3-5 seconds
- Combine & export: ~30-60 seconds
- **Total**: ~2-5 minutes

Factors affecting performance:
- Video length and resolution
- Internet speed (for APIs)
- CPU performance
- Disk I/O speed

### Memory Usage

- Video loaded fully into memory
- Temporary audio files on disk
- Peak memory usage: ~2-4x video file size

## Security Considerations

### API Keys
- Currently uses free APIs (no key required)
- Future: May need API key management for rate limits

### File Handling
- Validates file paths before processing
- Uses temporary directories for intermediate files
- Cleans up temporary files after processing

### Network
- All API calls use HTTPS
- No local storage of API responses
- Requires internet connection

## Extensibility

### Adding New Languages

1. Update UI to include language selection
2. Modify `translate_text()` to accept source/target languages
3. Verify gTTS supports the target language
4. Update documentation

### Adding Features

**Example: Subtitle Generation**

```python
def generate_subtitles(self, transcribed_text, output_path):
    """Generate SRT subtitle file"""
    # Implementation here
    pass
```

Integration point: After step 4 (transcription) in `translate_video()`

## Testing Strategy

### Unit Tests (Future)
- Test each processing function independently
- Mock external API calls
- Test error handling

### Integration Tests (Future)
- Test full pipeline with sample videos
- Test different video formats
- Test different audio modes

### Manual Testing (Current)
- Test with various video formats
- Test with different video lengths
- Test error scenarios
- Test UI responsiveness

## Deployment

### Standalone Executable (Future)

Using PyInstaller:
```bash
pyinstaller --onefile --windowed video_translator.py
```

### Installation Package

Using setup.py:
```bash
pip install -e .
```

## Monitoring and Logging

### Current Logging
- Real-time progress in UI log viewer
- User-friendly status messages

### Future Enhancements
- File-based logging
- Error log files
- Performance metrics
- Usage statistics

## References

- [MoviePy Documentation](https://zulko.github.io/moviepy/)
- [SpeechRecognition Documentation](https://github.com/Uberi/speech_recognition)
- [googletrans Documentation](https://py-googletrans.readthedocs.io/)
- [gTTS Documentation](https://gtts.readthedocs.io/)
- [FFmpeg Documentation](https://ffmpeg.org/documentation.html)

---

Last Updated: 2024-01-03
