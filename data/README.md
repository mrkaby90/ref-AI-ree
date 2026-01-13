# Data Directory

This directory contains all data used by the AI system.

## Subdirectories

### `raw/`
Original, unprocessed data files:
- Raw video recordings
- Original images
- Unprocessed sensor data

### `processed/`
Data that has been processed by the AI pipeline:
- Annotated videos
- Detected events
- Analysis results
- Generated reports

### `training/`
Dataset used for training AI models:
- Labeled video clips
- Annotated images
- Ground truth data
- Training metadata

### `validation/`
Dataset used for validating model performance:
- Test videos
- Validation images
- Performance metrics
- Benchmark results

## Data Format

Processed data is typically stored in JSON format for easy parsing:

```json
{
  "video_id": "match_001",
  "timestamp": "2024-01-13T18:00:00Z",
  "events": [
    {
      "type": "potential_foul",
      "time": "00:15:30",
      "confidence": 0.85,
      "description": "Player contact detected"
    }
  ]
}
```

## Privacy and Security

- Do not commit sensitive or personal data
- Ensure proper licensing for any sports footage
- Follow data protection regulations (GDPR, etc.)
