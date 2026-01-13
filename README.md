# ref-AI-ree

Small Project to help referees analyze sequences, possible fouls, and make decision confirmations

## Project Overview

This AI-powered system assists referees in analyzing sports sequences, detecting potential fouls, and confirming decision-making in real-time or post-match review. Optimized for deployment on Raspberry Pi 5.

## Folder Structure

```
ref-AI-ree/
├── src/                    # Source code
│   ├── ai/                 # AI models and inference code
│   ├── utils/              # Utility functions
│   └── config/             # Configuration files
├── examples/               # Example media files
│   ├── videos/             # Example video clips
│   └── pictures/           # Example images
├── data/                   # Data storage
│   ├── raw/                # Raw, unprocessed data
│   ├── processed/          # Processed data
│   ├── training/           # Training datasets
│   └── validation/         # Validation datasets
├── models/                 # AI model storage
│   ├── trained/            # Trained model files
│   └── checkpoints/        # Training checkpoints
├── docs/                   # Documentation
├── tests/                  # Test files
├── requirements.txt        # Python dependencies
└── .gitignore             # Git ignore rules
```

## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- (Optional) Raspberry Pi 5 for deployment

### Installation

1. Clone the repository:
```bash
git clone https://github.com/mrkaby90/ref-AI-ree.git
cd ref-AI-ree
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

1. **Add Example Media**: Place your video and image files in the `examples/` directory
   - Videos go in `examples/videos/`
   - Pictures go in `examples/pictures/`

2. **Process Media**: Run the AI analysis (implementation pending)
```bash
python src/main.py --input examples/videos/sample.mp4
```

3. **View Results**: Check the `data/processed/` directory for analysis results

## Raspberry Pi 5 Deployment

For detailed instructions on deploying to Raspberry Pi 5, see [docs/RASPBERRY_PI_SETUP.md](docs/RASPBERRY_PI_SETUP.md)

## Project Goals

- ✅ Analyze referee decisions in sports matches
- ✅ Detect potential fouls and rule violations
- ✅ Provide decision confirmation support
- ✅ Run efficiently on Raspberry Pi 5 hardware
- ✅ Process both live and recorded footage

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## License

See [LICENSE](LICENSE) file for details.

## Future Enhancements

- Real-time video analysis
- Integration with camera modules
- Machine learning model training pipeline
- Web interface for viewing results
- Mobile app integration
