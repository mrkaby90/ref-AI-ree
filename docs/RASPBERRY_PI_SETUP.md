# Configuration for Raspberry Pi 5 Deployment

## Hardware Requirements
- Raspberry Pi 5 (4GB or 8GB RAM recommended)
- MicroSD card (64GB+ recommended)
- Power supply (27W USB-C)
- Camera module (optional, for live capture)

## Software Setup

### 1. Operating System
Install Raspberry Pi OS (64-bit) Lite or Desktop version:
```bash
# Use Raspberry Pi Imager to flash the OS
```

### 2. System Updates
```bash
sudo apt update
sudo apt upgrade -y
```

### 3. Python Environment
```bash
# Install Python 3.11+ if not available
sudo apt install python3 python3-pip python3-venv -y

# Create virtual environment
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Raspberry Pi Specific Packages
```bash
# For GPIO control
pip install RPi.GPIO

# For camera support (if using Pi Camera Module)
sudo apt install -y python3-picamera2
```

### 6. Performance Optimization

#### Enable Hardware Acceleration
```bash
# For OpenCV with hardware acceleration
sudo apt install python3-opencv

# For TensorFlow Lite (optimized for ARM)
pip install tflite-runtime
```

#### Memory Management
Add to `/boot/config.txt`:
```
# Increase GPU memory for video processing
gpu_mem=256
```

### 7. Auto-start on Boot (Optional)
Create a systemd service:
```bash
sudo nano /etc/systemd/system/referee-ai.service
```

Add:
```ini
[Unit]
Description=Referee AI Service
After=network.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/ref-AI-ree
ExecStart=/home/pi/ref-AI-ree/venv/bin/python src/main.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl enable referee-ai.service
sudo systemctl start referee-ai.service
```

## Notes
- Use TensorFlow Lite or ONNX Runtime for better performance on ARM architecture
- Consider using quantized models to reduce memory usage
- Test thermal throttling under sustained AI inference loads
