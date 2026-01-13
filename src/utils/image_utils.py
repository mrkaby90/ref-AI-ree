"""
Image processing utilities for referee AI system
"""

import cv2
import numpy as np
from pathlib import Path
from typing import Optional


def load_image(image_path: str) -> Optional[np.ndarray]:
    """
    Load an image file
    
    Args:
        image_path: Path to the image file
        
    Returns:
        Image as numpy array or None if failed
    """
    if not Path(image_path).exists():
        print(f"Error: Image file not found: {image_path}")
        return None
    
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not load image: {image_path}")
        return None
    
    return image


def resize_image(image: np.ndarray, width: int, height: int) -> np.ndarray:
    """
    Resize image to specified dimensions
    
    Args:
        image: Input image
        width: Target width
        height: Target height
        
    Returns:
        Resized image
    """
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_LINEAR)


def save_image(image: np.ndarray, output_path: str) -> bool:
    """
    Save image to file
    
    Args:
        image: Image to save
        output_path: Output file path
        
    Returns:
        True if successful, False otherwise
    """
    try:
        cv2.imwrite(output_path, image)
        return True
    except Exception as e:
        print(f"Error saving image: {e}")
        return False
