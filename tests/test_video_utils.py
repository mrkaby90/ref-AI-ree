"""
Tests for video utilities
"""

import pytest
from pathlib import Path
from src.utils.video_utils import get_video_info, load_video


def test_load_video_nonexistent():
    """Test loading a non-existent video file"""
    result = load_video("nonexistent_video.mp4")
    assert result is None


def test_get_video_info_nonexistent():
    """Test getting info from a non-existent video file"""
    result = get_video_info("nonexistent_video.mp4")
    assert result == {}


# Note: Actual video processing tests require sample video files
# Add more tests when example videos are available in examples/videos/
