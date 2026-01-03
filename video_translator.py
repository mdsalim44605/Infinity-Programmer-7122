#!/usr/bin/env python3
"""
Video Translator Desktop App
Translates video audio from English to Bengali
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import threading
import os
import sys
from pathlib import Path
import speech_recognition as sr
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip
from googletrans import Translator
from gtts import gTTS
import tempfile
import wave
import contextlib


class VideoTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Translator - English to Bengali")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        self.input_video_path = None
        self.output_video_path = None
        self.is_processing = False
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the user interface"""
        # Configure grid weights
        self.root.grid_rowconfigure(0, weight=0)
        self.root.grid_rowconfigure(1, weight=0)
        self.root.grid_rowconfigure(2, weight=0)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_rowconfigure(4, weight=0)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Title
        title_label = tk.Label(
            self.root,
            text="Video Translator - English to Bengali",
            font=("Arial", 16, "bold"),
            pady=10
        )
        title_label.grid(row=0, column=0, sticky="ew")
        
        # Input section
        input_frame = ttk.LabelFrame(self.root, text="Input Video", padding=10)
        input_frame.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        input_frame.grid_columnconfigure(1, weight=1)
        
        self.input_label = ttk.Label(input_frame, text="No file selected")
        self.input_label.grid(row=0, column=0, columnspan=2, sticky="w", pady=5)
        
        ttk.Button(
            input_frame,
            text="Browse Video",
            command=self.browse_input_video
        ).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        
        # Output section
        output_frame = ttk.LabelFrame(self.root, text="Output Video", padding=10)
        output_frame.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
        output_frame.grid_columnconfigure(1, weight=1)
        
        self.output_label = ttk.Label(output_frame, text="No output path selected")
        self.output_label.grid(row=0, column=0, columnspan=2, sticky="w", pady=5)
        
        ttk.Button(
            output_frame,
            text="Choose Output Location",
            command=self.browse_output_video
        ).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        
        # Options section
        options_frame = ttk.LabelFrame(self.root, text="Options", padding=10)
        options_frame.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")
        options_frame.grid_columnconfigure(0, weight=1)
        options_frame.grid_rowconfigure(1, weight=1)
        
        # Audio mode selection
        mode_frame = ttk.Frame(options_frame)
        mode_frame.grid(row=0, column=0, sticky="ew", pady=5)
        
        ttk.Label(mode_frame, text="Audio Mode:").pack(side=tk.LEFT, padx=5)
        
        self.audio_mode = tk.StringVar(value="replace")
        ttk.Radiobutton(
            mode_frame,
            text="Replace Original Audio",
            variable=self.audio_mode,
            value="replace"
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Radiobutton(
            mode_frame,
            text="Mix with Original",
            variable=self.audio_mode,
            value="mix"
        ).pack(side=tk.LEFT, padx=5)
        
        # Progress/Log section
        ttk.Label(options_frame, text="Progress Log:").grid(row=1, column=0, sticky="w", pady=5)
        
        self.log_text = scrolledtext.ScrolledText(
            options_frame,
            height=10,
            width=70,
            state='disabled',
            wrap=tk.WORD
        )
        self.log_text.grid(row=2, column=0, sticky="nsew", pady=5)
        options_frame.grid_rowconfigure(2, weight=1)
        
        # Progress bar
        self.progress = ttk.Progressbar(
            options_frame,
            mode='indeterminate',
            length=300
        )
        self.progress.grid(row=3, column=0, sticky="ew", pady=5)
        
        # Control buttons
        button_frame = ttk.Frame(self.root)
        button_frame.grid(row=4, column=0, pady=10)
        
        self.translate_button = ttk.Button(
            button_frame,
            text="Translate Video",
            command=self.start_translation,
            style="Accent.TButton"
        )
        self.translate_button.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            button_frame,
            text="Exit",
            command=self.root.quit
        ).pack(side=tk.LEFT, padx=5)
        
    def browse_input_video(self):
        """Browse and select input video file"""
        filepath = filedialog.askopenfilename(
            title="Select Video File",
            filetypes=[
                ("Video Files", "*.mp4 *.avi *.mov *.mkv *.flv *.wmv"),
                ("All Files", "*.*")
            ]
        )
        if filepath:
            self.input_video_path = filepath
            self.input_label.config(text=f"Selected: {os.path.basename(filepath)}")
            self.log_message(f"Input video selected: {filepath}")
            
            # Auto-suggest output path
            if not self.output_video_path:
                output_dir = os.path.dirname(filepath)
                filename = os.path.splitext(os.path.basename(filepath))[0]
                suggested_output = os.path.join(output_dir, f"{filename}_bengali.mp4")
                self.output_video_path = suggested_output
                self.output_label.config(text=f"Output: {os.path.basename(suggested_output)}")
    
    def browse_output_video(self):
        """Browse and select output video file path"""
        filepath = filedialog.asksaveasfilename(
            title="Save Translated Video As",
            defaultextension=".mp4",
            filetypes=[
                ("MP4 Video", "*.mp4"),
                ("All Files", "*.*")
            ]
        )
        if filepath:
            self.output_video_path = filepath
            self.output_label.config(text=f"Output: {os.path.basename(filepath)}")
            self.log_message(f"Output path set: {filepath}")
    
    def log_message(self, message):
        """Add message to log text area"""
        self.log_text.config(state='normal')
        self.log_text.insert(tk.END, f"{message}\n")
        self.log_text.see(tk.END)
        self.log_text.config(state='disabled')
        self.root.update_idletasks()
    
    def start_translation(self):
        """Start the translation process in a separate thread"""
        if self.is_processing:
            messagebox.showwarning("Processing", "Translation is already in progress!")
            return
        
        if not self.input_video_path:
            messagebox.showerror("Error", "Please select an input video file!")
            return
        
        if not self.output_video_path:
            messagebox.showerror("Error", "Please select an output location!")
            return
        
        if not os.path.exists(self.input_video_path):
            messagebox.showerror("Error", "Input video file does not exist!")
            return
        
        # Start processing in a separate thread
        self.is_processing = True
        self.translate_button.config(state='disabled')
        self.progress.start(10)
        
        thread = threading.Thread(target=self.translate_video, daemon=True)
        thread.start()
    
    def translate_video(self):
        """Main translation process"""
        try:
            self.log_message("=" * 60)
            self.log_message("Starting video translation process...")
            self.log_message("=" * 60)
            
            # Step 1: Load video
            self.log_message("Step 1: Loading video file...")
            video = VideoFileClip(self.input_video_path)
            self.log_message(f"Video loaded: Duration={video.duration:.2f}s, FPS={video.fps}")
            
            # Step 2: Extract audio
            self.log_message("\nStep 2: Extracting audio from video...")
            audio = video.audio
            
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_audio_path = os.path.join(temp_dir, "temp_audio.wav")
                audio.write_audiofile(temp_audio_path, logger=None)
                self.log_message(f"Audio extracted to temporary file")
                
                # Step 3: Transcribe audio (English)
                self.log_message("\nStep 3: Transcribing English audio to text...")
                transcribed_text = self.transcribe_audio(temp_audio_path)
                
                if not transcribed_text:
                    raise Exception("Failed to transcribe audio. No speech detected.")
                
                self.log_message(f"Transcribed text: {transcribed_text[:100]}...")
                
                # Step 4: Translate to Bengali
                self.log_message("\nStep 4: Translating text to Bengali...")
                bengali_text = self.translate_text(transcribed_text)
                self.log_message(f"Translated text: {bengali_text[:100]}...")
                
                # Step 5: Generate Bengali audio
                self.log_message("\nStep 5: Generating Bengali audio...")
                bengali_audio_path = os.path.join(temp_dir, "bengali_audio.mp3")
                self.generate_audio(bengali_text, bengali_audio_path)
                self.log_message("Bengali audio generated")
                
                # Step 6: Combine video with new audio
                self.log_message("\nStep 6: Combining video with Bengali audio...")
                bengali_audio_clip = AudioFileClip(bengali_audio_path)
                
                if self.audio_mode.get() == "mix":
                    # Mix with original audio (50% each)
                    original_audio = video.audio.volumex(0.3)
                    bengali_audio_clip = bengali_audio_clip.volumex(0.7)
                    mixed_audio = CompositeAudioClip([original_audio, bengali_audio_clip])
                    final_video = video.set_audio(mixed_audio)
                else:
                    # Replace original audio
                    final_video = video.set_audio(bengali_audio_clip)
                
                # Step 7: Write output video
                self.log_message("\nStep 7: Writing output video file...")
                self.log_message("This may take a while depending on video length...")
                
                final_video.write_videofile(
                    self.output_video_path,
                    codec='libx264',
                    audio_codec='aac',
                    logger=None
                )
                
                # Cleanup
                video.close()
                bengali_audio_clip.close()
                if self.audio_mode.get() == "mix":
                    mixed_audio.close()
                
            self.log_message("\n" + "=" * 60)
            self.log_message("✓ Translation completed successfully!")
            self.log_message(f"Output saved to: {self.output_video_path}")
            self.log_message("=" * 60)
            
            self.root.after(0, lambda: messagebox.showinfo(
                "Success",
                f"Video translation completed!\n\nSaved to:\n{self.output_video_path}"
            ))
            
        except Exception as e:
            error_msg = f"Error during translation: {str(e)}"
            self.log_message(f"\n✗ {error_msg}")
            self.root.after(0, lambda: messagebox.showerror("Error", error_msg))
            
        finally:
            self.is_processing = False
            self.root.after(0, self.progress.stop)
            self.root.after(0, lambda: self.translate_button.config(state='normal'))
    
    def transcribe_audio(self, audio_path):
        """Transcribe audio to text using speech recognition"""
        recognizer = sr.Recognizer()
        
        try:
            with sr.AudioFile(audio_path) as source:
                self.log_message("Processing audio file...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio_data = recognizer.record(source)
                
            self.log_message("Recognizing speech...")
            text = recognizer.recognize_google(audio_data, language='en-US')
            return text
            
        except sr.UnknownValueError:
            self.log_message("Warning: Could not understand audio")
            raise Exception("Could not understand the audio. Please ensure the video has clear English speech.")
        except sr.RequestError as e:
            self.log_message(f"Error with speech recognition service: {e}")
            raise Exception(f"Speech recognition service error: {e}")
    
    def translate_text(self, text):
        """Translate text from English to Bengali"""
        try:
            translator = Translator()
            translation = translator.translate(text, src='en', dest='bn')
            return translation.text
        except Exception as e:
            self.log_message(f"Translation error: {e}")
            raise Exception(f"Translation failed: {e}")
    
    def generate_audio(self, text, output_path):
        """Generate audio from Bengali text using gTTS"""
        try:
            tts = gTTS(text=text, lang='bn', slow=False)
            tts.save(output_path)
        except Exception as e:
            self.log_message(f"Audio generation error: {e}")
            raise Exception(f"Failed to generate Bengali audio: {e}")


def main():
    """Main entry point"""
    root = tk.Tk()
    app = VideoTranslatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
