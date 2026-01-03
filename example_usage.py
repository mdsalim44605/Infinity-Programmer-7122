#!/usr/bin/env python3
"""
Example usage of the Video Translator components
This demonstrates how to use the translation functions programmatically
"""

from video_translator import VideoTranslatorApp
import tkinter as tk


def example_gui_launch():
    """
    Example 1: Launch the GUI application
    This is the standard way to use the video translator
    """
    print("Launching Video Translator GUI...")
    root = tk.Tk()
    app = VideoTranslatorApp(root)
    root.mainloop()


def example_programmatic_usage():
    """
    Example 2: Programmatic usage (without GUI)
    Demonstrates how to use individual components
    """
    from googletrans import Translator
    from gtts import gTTS
    
    # Example text translation
    print("\n=== Example: Text Translation ===")
    translator = Translator()
    english_text = "Hello, how are you? Welcome to our video translator."
    
    print(f"English: {english_text}")
    translation = translator.translate(english_text, src='en', dest='bn')
    bengali_text = translation.text
    print(f"Bengali: {bengali_text}")
    
    # Example audio generation
    print("\n=== Example: Audio Generation ===")
    print("Generating Bengali audio...")
    tts = gTTS(text=bengali_text, lang='bn', slow=False)
    output_file = "example_bengali_audio.mp3"
    tts.save(output_file)
    print(f"Audio saved to: {output_file}")
    
    print("\nNote: For video processing, please use the GUI application.")


if __name__ == "__main__":
    # Uncomment the example you want to run:
    
    # Standard GUI launch (recommended)
    example_gui_launch()
    
    # Programmatic usage example (requires internet)
    # example_programmatic_usage()
