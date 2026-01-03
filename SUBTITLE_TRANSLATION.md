# Subtitle Translation Feature

## Overview

The Video Translator now supports automatic subtitle extraction, translation, and embedding. This feature works seamlessly with the audio dubbing to provide a complete Bengali translation experience.

## Features

### 🎬 Automatic Subtitle Detection
- Automatically detects embedded subtitles in your video
- Extracts subtitles in SRT format
- Works with videos that have embedded subtitle tracks

### 🌐 Complete Translation
- Translates all subtitle text from English to Bengali
- Preserves timing and formatting
- Maintains subtitle synchronization with video

### 📝 Smart Embedding
- Attempts to embed Bengali subtitles directly into the video
- If embedding fails, saves subtitles as a separate `.srt` file
- Bengali subtitles are marked with proper language metadata

### 🔄 Seamless Integration
- Works automatically during video translation
- No additional steps required
- Processes subtitles while audio is being dubbed

## How It Works

### Step-by-Step Process

1. **Subtitle Extraction**
   ```
   Input Video → FFmpeg → Extract Embedded Subtitles → SRT File
   ```
   - Uses FFmpeg to extract subtitle track
   - Saves as standard SRT format
   - Detects if video has no subtitles

2. **Subtitle Parsing**
   ```
   SRT File → Parse → Subtitle Entries (index, timing, text)
   ```
   - Parses SRT format
   - Extracts:
     - Entry number
     - Start time
     - End time
     - Subtitle text

3. **Translation**
   ```
   English Subtitle Text → Google Translate → Bengali Subtitle Text
   ```
   - Translates each subtitle entry
   - Preserves timing information
   - Maintains subtitle structure

4. **Subtitle Writing**
   ```
   Bengali Subtitle Data → Generate SRT → Bengali SRT File
   ```
   - Creates properly formatted Bengali SRT file
   - Maintains all timing information
   - Uses UTF-8 encoding for Bengali text

5. **Subtitle Embedding**
   ```
   Video + Bengali SRT → FFmpeg → Video with Embedded Subtitles
   ```
   - Embeds subtitles using FFmpeg
   - Sets language metadata to Bengali (ben)
   - Falls back to external SRT if embedding fails

## Supported Formats

### Input Video Formats
- MP4 (with embedded subtitles)
- MKV (with embedded subtitles)
- AVI (with embedded subtitles)
- MOV (with embedded subtitles)
- Any format supported by FFmpeg

### Subtitle Formats
- **Input**: Embedded subtitles or SRT
- **Output**: Embedded Bengali subtitles or separate SRT file

## Usage

### Basic Usage
1. Select your video file (with embedded subtitles)
2. Choose output location
3. Click "Translate Video"
4. Wait for processing to complete
5. Output video will have:
   - Bengali audio (replacing original)
   - Bengali subtitles (embedded or as separate file)

### Videos Without Subtitles
- If video has no embedded subtitles, only audio is dubbed
- Application will note: "No subtitles to process"
- Video processing continues normally

### Videos With Subtitles
- Application extracts subtitles automatically
- Translates all subtitle entries to Bengali
- Embeds translated subtitles back into video
- Shows progress: "Translated X/Y subtitle entries"

## Output

### With Successful Embedding
```
output_video_bengali.mp4
├── Video track (original)
├── Audio track (Bengali dubbing)
└── Subtitle track (Bengali, embedded)
```

### With External Subtitles
```
output_video_bengali.mp4 (Video + Bengali audio)
output_video_bengali.srt (Bengali subtitles)
```

## Technical Details

### Subtitle Extraction Command
```bash
ffmpeg -i input.mp4 -map 0:s:0 output.srt -y
```

### Subtitle Embedding Command
```bash
ffmpeg -i video.mp4 -i subtitles.srt \
  -c copy -c:s mov_text \
  -metadata:s:s:0 language=ben \
  output.mp4 -y
```

### SRT Format Example

**English (Original):**
```
1
00:00:01,000 --> 00:00:03,000
Hello, welcome to our video

2
00:00:03,500 --> 00:00:06,000
Today we will learn about Python
```

**Bengali (Translated):**
```
1
00:00:01,000 --> 00:00:03,000
হ্যালো, আমাদের ভিডিওতে স্বাগতম

2
00:00:03,500 --> 00:00:06,000
আজ আমরা পাইথন সম্পর্কে শিখব
```

## Progress Messages

During subtitle processing, you'll see:

```
Step 6: Processing subtitles...
Attempting to extract embedded subtitles...
✓ Subtitles extracted successfully
Parsing subtitles...
Found 42 subtitle entries
Translating subtitles to Bengali...
Translated 10/42 subtitle entries...
Translated 20/42 subtitle entries...
Translated 30/42 subtitle entries...
Translated 42/42 subtitle entries...
Writing translated subtitles...
✓ Subtitles translated successfully

Step 9: Embedding Bengali subtitles...
Embedding Bengali subtitles into video...
✓ Subtitles embedded successfully
```

## Error Handling

### No Subtitles Found
```
No embedded subtitles found in video
No subtitles to process (video has no embedded subtitles)
```
→ Processing continues with audio dubbing only

### Subtitle Extraction Failed
```
Subtitle extraction failed: [error message]
```
→ Processing continues with audio dubbing only

### Translation Failed
```
Warning: Failed to translate subtitle X: [error]
```
→ Original subtitle text is kept for that entry

### Embedding Failed
```
Note: Could not embed subtitles, but video with audio is ready
Subtitles saved separately as: output_video_bengali.srt
```
→ Subtitles are saved as separate SRT file

## Tips for Best Results

### ✅ For Videos With Subtitles
- Use videos with properly embedded English subtitles
- Ensure subtitles are in SRT format or compatible
- MP4 and MKV formats work best

### ✅ For External Subtitles
- If your video has external `.srt` file, manually embed it first
- Use tools like FFmpeg or video editing software
- Then process with Video Translator

### ✅ Subtitle Quality
- Clear, well-formatted subtitles translate better
- Avoid videos with burned-in (hardcoded) subtitles
- Use videos with properly timed subtitles

## Troubleshooting

### "No embedded subtitles found"
**Problem**: Video doesn't have subtitle track  
**Solution**: 
- Check if video has subtitles in media player
- Try embedding external SRT file first
- Some videos have hardcoded subtitles (can't be extracted)

### "Subtitle extraction timed out"
**Problem**: Extraction taking too long  
**Solution**:
- Check if video file is corrupted
- Try a different video
- Ensure FFmpeg is working properly

### "Could not embed subtitles"
**Problem**: Embedding failed but SRT created  
**Solution**:
- Use the separate SRT file provided
- Load subtitles manually in your media player
- Video and audio are still properly translated

### Subtitles out of sync
**Problem**: Timing doesn't match audio  
**Solution**:
- Original subtitle timing is preserved
- If original was out of sync, translation will be too
- Use subtitle editing tools to adjust timing

## Advanced Usage

### Manual Subtitle Editing
1. Process video with Video Translator
2. If needed, edit the output Bengali SRT file
3. Re-embed using:
   ```bash
   ffmpeg -i video_bengali.mp4 -i edited_bengali.srt \
     -c copy -c:s mov_text output.mp4
   ```

### Batch Processing
- Process videos one at a time
- Each video is checked for subtitles automatically
- Mix of videos with/without subtitles works fine

### Custom Subtitle Formats
- Currently supports SRT format
- Other formats may need conversion first
- Use subtitle conversion tools if needed

## Future Enhancements

Planned improvements:
- [ ] Support for multiple subtitle tracks
- [ ] External SRT file input option
- [ ] Subtitle timing adjustment
- [ ] Support for more subtitle formats (ASS, SSA, VTT)
- [ ] Subtitle style preservation
- [ ] Subtitle position and formatting options

## Examples

### Example 1: Educational Video
**Input**: `lecture.mp4` (30 mins, with English subtitles)  
**Process**: 15-20 minutes  
**Output**: 
- `lecture_bengali.mp4` (Bengali audio + embedded Bengali subtitles)

### Example 2: Movie Clip
**Input**: `movie_clip.mp4` (5 mins, with English subtitles)  
**Process**: 3-5 minutes  
**Output**:
- `movie_clip_bengali.mp4` (Bengali dubbed + Bengali subtitles)

### Example 3: YouTube Video
**Input**: `youtube_download.mp4` (no subtitles)  
**Process**: 2-4 minutes  
**Output**:
- `youtube_download_bengali.mp4` (Bengali audio only)
- Note: "No subtitles to process"

## FAQ

**Q: Do all videos have subtitles?**  
A: No, many videos don't have embedded subtitles. The tool will note this and continue with audio dubbing.

**Q: Can I add my own subtitle file?**  
A: Currently, the tool extracts embedded subtitles. You can embed your SRT file first using FFmpeg, then process.

**Q: What if subtitles are in another language?**  
A: The tool expects English subtitles. Other languages may not translate correctly.

**Q: Can I edit the Bengali subtitles?**  
A: Yes! Edit the output SRT file with any text editor (use UTF-8 encoding).

**Q: Why are subtitles saved separately?**  
A: If embedding fails (codec compatibility), subtitles are saved as `.srt` for manual loading.

---

For more information, see:
- [README.md](README.md) - Main documentation
- [WORKFLOW.md](WORKFLOW.md) - Translation workflow
- [FAQ.md](FAQ.md) - Frequently asked questions
