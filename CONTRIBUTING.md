# Contributing to Video Translator

Thank you for your interest in contributing to the Video Translator project! This document provides guidelines for contributing.

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- A clear, descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Your environment (OS, Python version, etc.)
- Screenshots if applicable

### Suggesting Enhancements

We welcome feature suggestions! Please open an issue with:
- Clear description of the feature
- Use case and benefits
- Any implementation ideas you have

### Pull Requests

1. **Fork the Repository**
   ```bash
   git clone https://github.com/yourusername/video-translator.git
   cd video-translator
   ```

2. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Your Changes**
   - Follow the existing code style
   - Add comments for complex logic
   - Update documentation if needed

4. **Test Your Changes**
   - Test with various video formats
   - Ensure existing functionality still works
   - Test on different operating systems if possible

5. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Add: Brief description of your changes"
   ```

6. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request**
   - Provide a clear description of changes
   - Reference any related issues
   - Wait for review and feedback

## Development Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/video-translator.git
cd video-translator

# Install dependencies
pip install -r requirements.txt

# Run the application
python video_translator.py
```

## Code Style Guidelines

- Follow PEP 8 style guide
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and modular
- Comment complex algorithms

## Testing

Before submitting:
- Test with multiple video formats (MP4, AVI, MOV)
- Test with different video lengths
- Test both audio modes (replace and mix)
- Verify error handling works correctly

## Areas for Contribution

We'd especially welcome contributions in these areas:

### High Priority
- [ ] Subtitle generation (SRT file output)
- [ ] Batch processing multiple videos
- [ ] Progress bar with percentage
- [ ] Cancel/stop functionality during processing
- [ ] Better error messages and recovery

### Medium Priority
- [ ] Support for additional language pairs
- [ ] Custom voice speed controls
- [ ] Audio quality settings
- [ ] Video preview before processing
- [ ] Recent files list

### Low Priority
- [ ] Dark mode theme
- [ ] Keyboard shortcuts
- [ ] Drag-and-drop video files
- [ ] System tray integration
- [ ] Portable executable builds

### Technical Improvements
- [ ] Unit tests
- [ ] Integration tests
- [ ] CI/CD pipeline
- [ ] Code coverage reports
- [ ] Performance optimization
- [ ] Memory usage optimization

## Feature Implementation Guidelines

### Adding New Language Pairs

1. Update the language dropdown in the GUI
2. Verify gTTS supports the target language
3. Test speech recognition for source language
4. Update documentation

### Adding New Features

1. Discuss the feature in an issue first
2. Keep backward compatibility
3. Update README and documentation
4. Add error handling
5. Test thoroughly

## Documentation

When adding features, please update:
- README.md - Main documentation
- QUICKSTART.md - Quick start guide if affected
- Code comments and docstrings
- CHANGELOG.md (if we add one)

## Questions?

Feel free to open an issue with the label "question" if you need clarification on anything.

## Code of Conduct

- Be respectful and constructive
- Welcome newcomers
- Focus on the project's goals
- Help each other learn and grow

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to Video Translator! 🎉
