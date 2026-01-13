# Project Structure Documentation

## Overview

This document explains the organization and purpose of each directory in the ref-AI-ree project.

## Directory Structure

### `/src/` - Source Code
The main source code directory containing all Python modules.

#### `/src/ai/` - AI Components
Contains AI models and inference code:
- Object detection models
- Classification models
- Tracking algorithms
- Analysis pipelines

**Key files (to be implemented):**
- `detector.py` - Object detection (players, ball, referee)
- `classifier.py` - Action classification
- `tracker.py` - Multi-object tracking
- `analyzer.py` - High-level analysis

#### `/src/utils/` - Utility Functions
Helper functions and common utilities:
- `video_utils.py` - Video processing functions
- `image_utils.py` - Image processing functions
- Additional utilities as needed

#### `/src/config/` - Configuration
Configuration management:
- `settings.py` - Global settings and constants
- Environment-specific configurations

### `/examples/` - Example Media Files
Sample media files for testing and demonstration.

#### `/examples/videos/`
Example video clips:
- Match sequences
- Foul situations
- Decision scenarios

**Note:** Actual video files are not committed to git (see `.gitignore`)

#### `/examples/pictures/`
Example images:
- Match screenshots
- Frame captures
- Annotated images

**Note:** Actual image files are not committed to git (see `.gitignore`)

### `/data/` - Data Storage
All data used by the system.

#### `/data/raw/`
Original, unprocessed data:
- Raw video recordings
- Original images
- Unprocessed sensor data

#### `/data/processed/`
Processed outputs:
- Annotated videos
- Analysis results
- Generated reports

#### `/data/training/`
Training datasets:
- Labeled data
- Ground truth annotations
- Training metadata

#### `/data/validation/`
Validation datasets:
- Test data
- Validation metrics
- Benchmark results

### `/models/` - AI Models
Storage for AI model files.

#### `/models/trained/`
Production-ready models:
- Final model weights (`.onnx`, `.tflite`)
- Model metadata
- Performance metrics

#### `/models/checkpoints/`
Training checkpoints:
- Intermediate weights
- Training snapshots
- Recovery points

### `/docs/` - Documentation
Project documentation:
- `RASPBERRY_PI_SETUP.md` - Raspberry Pi deployment guide
- Additional documentation as needed

### `/tests/` - Test Files
Unit tests and integration tests:
- `test_video_utils.py` - Video utility tests
- `test_image_utils.py` - Image utility tests
- Additional test files

### `/logs/` - Log Files
Application logs (not committed to git)

## File Conventions

### Python Files
- Use snake_case for file names
- Include docstrings for all modules, classes, and functions
- Follow PEP 8 style guidelines

### Data Files
- Use descriptive names with timestamps when appropriate
- Organize by type and date
- Document data sources and formats

### Model Files
- Include version numbers in filenames
- Maintain separate directories for different model types
- Document model architecture and performance

## Development Workflow

1. **Add Examples**: Place media files in `examples/`
2. **Develop AI Components**: Implement in `src/ai/`
3. **Add Utilities**: Create helper functions in `src/utils/`
4. **Test**: Write tests in `tests/`
5. **Process Data**: Run analysis, results go to `data/processed/`
6. **Train Models**: Save to `models/checkpoints/` during training
7. **Deploy**: Move final models to `models/trained/`

## Raspberry Pi Considerations

- Use optimized model formats (ONNX, TensorFlow Lite)
- Minimize memory usage
- Leverage hardware acceleration where available
- See `docs/RASPBERRY_PI_SETUP.md` for deployment details

## Getting Started

See the main [README.md](../README.md) for installation and usage instructions.
