# Examples Directory

This directory contains example media files (videos and pictures) for testing and demonstrating the referee AI system.

## Structure

### `videos/`
Contains example video clips of:
- Football/soccer match sequences
- Potential foul situations
- Goal-line decisions
- Offside scenarios
- VAR review situations

**Supported formats:** `.mp4`, `.avi`, `.mov`, `.mkv`

### `pictures/`
Contains example images of:
- Match screenshots
- Frame captures from video analysis
- Reference images for training/testing
- Annotated images showing AI detections

**Supported formats:** `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`

## Usage

Place your example media files in the respective subdirectories:

```bash
# Add a video example
cp /path/to/your/video.mp4 examples/videos/

# Add a picture example
cp /path/to/your/image.jpg examples/pictures/
```

## Note

Due to file size limitations, actual media files are not committed to the repository (see `.gitignore`). 

To use this project:
1. Add your own example files to these directories
2. Use the AI models in `src/ai/` to process these examples
3. Results will be saved to the `data/processed/` directory

## Sample Data Sources

You can obtain sample sports footage from:
- Public domain sports videos
- Creative Commons licensed content
- Your own recorded footage
- Generated test data
