# Models Directory

This directory stores AI models used for referee decision support.

## Subdirectories

### `trained/`
Fully trained, production-ready models:
- Final model weights
- Model architectures
- Inference configurations
- Model metadata and performance metrics

### `checkpoints/`
Training checkpoints saved during model development:
- Intermediate weights
- Best-performing snapshots
- Recovery points for training continuation

## Model Formats

Supported model formats:
- `.pt` / `.pth` - PyTorch models
- `.h5` / `.hdf5` - Keras/TensorFlow models
- `.onnx` - ONNX format (recommended for cross-platform deployment)
- `.tflite` - TensorFlow Lite (optimized for Raspberry Pi)

## Model Organization

Organize models by type and version:

```
models/
├── trained/
│   ├── detector_v1.0.onnx
│   ├── classifier_v1.0.onnx
│   └── tracker_v1.0.onnx
└── checkpoints/
    ├── detector_epoch10.pt
    └── detector_epoch20.pt
```

## Usage

Load models in your code:

```python
import onnxruntime as ort

# Load ONNX model
session = ort.InferenceSession("models/trained/detector_v1.0.onnx")
```

## Model Download

Large models are not committed to git. Download pre-trained models from:
- Project releases
- Cloud storage links
- Model registry
