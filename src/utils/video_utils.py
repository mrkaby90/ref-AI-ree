"""
Video processing utilities for referee AI system
"""

import cv2
from pathlib import Path
from typing import Optional, Tuple


def load_video(video_path: str) -> Optional[cv2.VideoCapture]:
    """
    Load a video file for processing
    
    Args:
        video_path: Path to the video file
        
    Returns:
        VideoCapture object or None if failed
    """
    if not Path(video_path).exists():
        print(f"Error: Video file not found: {video_path}")
        return None
    
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video: {video_path}")
        return None
    
    return cap


def get_video_info(video_path: str) -> dict:
    """
    Get video metadata
    
    Args:
        video_path: Path to the video file
        
    Returns:
        Dictionary containing video information
    """
    cap = load_video(video_path)
    if cap is None:
        return {}
    
    info = {
        'width': int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        'height': int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
        'fps': cap.get(cv2.CAP_PROP_FPS),
        'frame_count': int(cap.get(cv2.CAP_PROP_FRAME_COUNT)),
        'duration': cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS)
    }
    
    cap.release()
    return info


def extract_frame(video_path: str, frame_number: int) -> Optional[Tuple]:
    """
    Extract a specific frame from a video
    
    Args:
        video_path: Path to the video file
        frame_number: Frame number to extract
        
    Returns:
        Tuple of (success, frame) or None if failed
    """
    cap = load_video(video_path)
    if cap is None:
        return None
    
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    ret, frame = cap.read()
    
    cap.release()
    return (ret, frame) if ret else None
