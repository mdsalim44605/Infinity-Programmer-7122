# Video Translator Workflow

This document provides a visual guide to how the Video Translator application works.

## 🎯 High-Level Workflow

```
┌──────────────┐
│  Input Video │ (English Audio)
└──────┬───────┘
       │
       ▼
┌──────────────────────────────┐
│   Extract Audio from Video   │
│  (MoviePy + FFmpeg)          │
└──────┬───────────────────────┘
       │
       ▼
┌──────────────────────────────┐
│  Transcribe Audio to Text    │
│  (Google Speech Recognition) │
│  Output: English Text        │
└──────┬───────────────────────┘
       │
       ▼
┌──────────────────────────────┐
│   Translate English → Bengali│
│   (Google Translate API)     │
│   Output: Bengali Text       │
└──────┬───────────────────────┘
       │
       ▼
┌──────────────────────────────┐
│  Generate Audio from Text    │
│  (Google Text-to-Speech)     │
│  Output: Bengali Audio       │
└──────┬───────────────────────┘
       │
       ▼
┌──────────────────────────────┐
│  Combine Video + New Audio   │
│  (MoviePy + FFmpeg)          │
│  Mode: Replace or Mix        │
└──────┬───────────────────────┘
       │
       ▼
┌──────────────┐
│ Output Video │ (Bengali Audio)
└──────────────┘
```

## 🖥️ User Interaction Flow

```
START
  │
  ▼
┌─────────────────────┐
│  Launch Application │
│  python video_translator.py │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│  GUI Window Opens   │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐      ┌──────────────┐
│ Click "Browse Video"│ ───► │ Select File  │
└──────┬──────────────┘      └──────┬───────┘
       │                             │
       │◄────────────────────────────┘
       │
       ▼
┌─────────────────────┐
│ Choose Output Path  │ (Optional - Auto-suggested)
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Select Audio Mode   │
│ ○ Replace Original  │
│ ○ Mix with Original │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│Click "Translate"    │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│   Processing...     │
│   (Shows Progress)  │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│   Success Dialog    │
│   "Translation      │
│    Complete!"       │
└──────┬──────────────┘
       │
       ▼
      END
```

## 🔄 Processing Pipeline Details

### Step 1: Video Loading
```
Input: video.mp4
  │
  ├─ Load video metadata
  │  - Duration
  │  - FPS
  │  - Resolution
  │
  └─ Load audio track
     └─ Output: AudioClip object
```

### Step 2: Audio Extraction
```
AudioClip
  │
  ├─ Convert to WAV format
  │  - Sample rate: 44100 Hz
  │  - Channels: Mono/Stereo
  │
  └─ Save to temporary file
     └─ Output: temp_audio.wav
```

### Step 3: Speech Recognition
```
temp_audio.wav
  │
  ├─ Load audio file
  │
  ├─ Adjust for ambient noise
  │
  ├─ Send to Google API
  │  - Language: en-US
  │  - Format: FLAC
  │
  └─ Receive transcription
     └─ Output: "Hello, how are you..."
```

### Step 4: Translation
```
English Text: "Hello, how are you..."
  │
  ├─ Send to Google Translate
  │  - Source: en (English)
  │  - Target: bn (Bengali)
  │
  └─ Receive translation
     └─ Output: "হ্যালো, তুমি কেমন আছো..."
```

### Step 5: Audio Generation
```
Bengali Text: "হ্যালো, তুমি কেমন আছো..."
  │
  ├─ Send to Google TTS
  │  - Language: bn (Bengali)
  │  - Speed: Normal
  │
  ├─ Generate audio
  │
  └─ Save to temporary file
     └─ Output: bengali_audio.mp3
```

### Step 6: Audio Combination

#### Mode A: Replace Original Audio
```
Video (no audio) + Bengali Audio
  │
  ├─ Remove original audio track
  │
  ├─ Attach Bengali audio
  │
  └─ Output: video_bengali.mp4
```

#### Mode B: Mix with Original
```
Original Audio (30%) + Bengali Audio (70%)
  │
  ├─ Adjust volume levels
  │  - Original: volumex(0.3)
  │  - Bengali: volumex(0.7)
  │
  ├─ Create CompositeAudioClip
  │
  ├─ Attach to video
  │
  └─ Output: video_bengali.mp4
```

## ⚙️ Threading Architecture

```
┌────────────────────────────────────────┐
│           Main Thread                   │
│                                         │
│  ┌──────────────────────────────┐     │
│  │     Tkinter Event Loop       │     │
│  │  - Handle UI events          │     │
│  │  - Update UI elements        │     │
│  │  - Display progress          │     │
│  └──────────────────────────────┘     │
│                                         │
└─────────────┬──────────────────────────┘
              │
              │ start_translation()
              │ creates Worker Thread
              │
              ▼
┌────────────────────────────────────────┐
│          Worker Thread                  │
│                                         │
│  ┌──────────────────────────────┐     │
│  │   translate_video()          │     │
│  │  - Extract audio             │     │
│  │  - Transcribe                │     │
│  │  - Translate                 │     │
│  │  - Generate audio            │     │
│  │  - Combine video             │     │
│  │  - Export result             │     │
│  └──────────────────────────────┘     │
│              │                          │
│              │ Progress updates via     │
│              │ root.after()             │
│              ▼                          │
│         Update UI                       │
└────────────────────────────────────────┘
```

## 📊 Data Transformations

```
MP4 Video → VideoClip → AudioClip → WAV
                                      │
                                      ▼
WAV → Speech Recognition → English Text
                                      │
                                      ▼
English Text → Translation → Bengali Text
                                      │
                                      ▼
Bengali Text → TTS → MP3 Audio
                                      │
                                      ▼
MP3 + Original Video → New MP4 Video
```

## 🕒 Time Estimates

For a typical 1-minute video:

```
┌────────────────────────┬──────────────┐
│ Operation              │ Est. Time    │
├────────────────────────┼──────────────┤
│ Load Video             │ 2-5 sec      │
│ Extract Audio          │ 3-5 sec      │
│ Transcribe Audio       │ 10-20 sec    │
│ Translate Text         │ 1-2 sec      │
│ Generate Bengali Audio │ 3-5 sec      │
│ Combine & Export       │ 30-60 sec    │
├────────────────────────┼──────────────┤
│ TOTAL                  │ 2-5 minutes  │
└────────────────────────┴──────────────┘

Note: Times vary based on:
- Video length and resolution
- Internet speed
- Computer performance
- FFmpeg encoding speed
```

## 🚀 Performance Tips

### For Faster Processing:
```
✓ Use shorter videos for testing
✓ Use MP4 format (fastest)
✓ Ensure fast internet connection
✓ Close other applications
✓ Use videos with clear audio
```

### For Better Results:
```
✓ Use videos with clear English speech
✓ Minimize background noise
✓ Use videos with consistent audio levels
✓ Avoid videos with music overlays
✓ Test with 30-second clips first
```

## 🔧 Error Handling Flow

```
Operation
  │
  ├─ Try Execute
  │
  ├─ Success? ──Yes──► Continue
  │
  └─ No
      │
      ▼
   Catch Exception
      │
      ├─ Log Error Message
      │
      ├─ Show User Dialog
      │
      ├─ Clean Up Resources
      │
      └─ Reset UI State
```

## 📁 File Operations

### Temporary Files Lifecycle
```
START
  │
  ▼
Create temp directory: /tmp/tmpXXXXXX/
  │
  ├─ Extract: temp_audio.wav
  │
  ├─ Generate: bengali_audio.mp3
  │
  ├─ Process video...
  │
  ▼
Delete temp directory (automatic)
  │
  ▼
END
```

### Output File Creation
```
Input: video.mp4
  │
  ├─ Suggest: video_bengali.mp4
  │
  ├─ User confirms/changes location
  │
  ├─ Process video
  │
  └─ Write: video_bengali.mp4
             - Codec: H.264
             - Audio: AAC
             - Container: MP4
```

## 🌐 API Interactions

### Google Speech Recognition
```
Request:
  - Audio: FLAC format
  - Language: en-US
  - Encoding: LINEAR16

Response:
  - Transcription: String
  - Confidence: Float
```

### Google Translate
```
Request:
  - Text: String
  - Source: 'en'
  - Target: 'bn'

Response:
  - Translation: String
  - Source detected: String
```

### Google Text-to-Speech
```
Request:
  - Text: String
  - Language: 'bn'
  - Speed: Normal

Response:
  - Audio: MP3 file
  - Duration: Auto
```

## 🎨 UI State Management

```
Initial State:
  - Translate Button: Enabled
  - Progress Bar: Hidden
  - Log: Empty

During Processing:
  - Translate Button: Disabled
  - Progress Bar: Animating
  - Log: Showing updates

After Completion:
  - Translate Button: Enabled
  - Progress Bar: Stopped
  - Log: Shows success/error

On Error:
  - Translate Button: Enabled
  - Progress Bar: Stopped
  - Log: Shows error details
  - Error Dialog: Displayed
```

---

For technical details, see [ARCHITECTURE.md](ARCHITECTURE.md)  
For usage instructions, see [README.md](README.md)
