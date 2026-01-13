"""
Configuration settings for the referee AI system
"""

import os
from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).parent.parent.parent

# Directory paths
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
TRAINING_DATA_DIR = DATA_DIR / "training"
VALIDATION_DATA_DIR = DATA_DIR / "validation"

MODELS_DIR = PROJECT_ROOT / "models"
TRAINED_MODELS_DIR = MODELS_DIR / "trained"
CHECKPOINTS_DIR = MODELS_DIR / "checkpoints"

EXAMPLES_DIR = PROJECT_ROOT / "examples"
EXAMPLES_VIDEOS_DIR = EXAMPLES_DIR / "videos"
EXAMPLES_PICTURES_DIR = EXAMPLES_DIR / "pictures"

# Model settings
DEFAULT_MODEL_PATH = TRAINED_MODELS_DIR / "detector_v1.0.onnx"
CONFIDENCE_THRESHOLD = 0.5
NMS_THRESHOLD = 0.4

# Video processing settings
DEFAULT_FPS = 30
FRAME_WIDTH = 1920
FRAME_HEIGHT = 1080

# Image processing settings
IMAGE_SIZE = (640, 640)  # Model input size

# Raspberry Pi specific settings
IS_RASPBERRY_PI = os.path.exists('/proc/device-tree/model')
USE_GPU_ACCELERATION = False  # Set to True if GPU is available

# Logging settings
LOG_LEVEL = "INFO"
LOG_FILE = PROJECT_ROOT / "logs" / "referee_ai.log"

# Create necessary directories
for directory in [
    DATA_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR, TRAINING_DATA_DIR, VALIDATION_DATA_DIR,
    MODELS_DIR, TRAINED_MODELS_DIR, CHECKPOINTS_DIR,
    EXAMPLES_DIR, EXAMPLES_VIDEOS_DIR, EXAMPLES_PICTURES_DIR,
    PROJECT_ROOT / "logs"
]:
    directory.mkdir(parents=True, exist_ok=True)
