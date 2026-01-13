"""
Main entry point for the referee AI system
"""

import argparse
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.config.settings import EXAMPLES_VIDEOS_DIR, EXAMPLES_PICTURES_DIR
from src.utils.video_utils import get_video_info
from src.utils.image_utils import load_image


def main():
    """Main function to run the referee AI system"""
    parser = argparse.ArgumentParser(description='Referee AI Decision Support System')
    parser.add_argument('--input', type=str, help='Input video or image file path')
    parser.add_argument('--type', type=str, choices=['video', 'image'], 
                       help='Type of input (video or image)')
    parser.add_argument('--list-examples', action='store_true',
                       help='List available example files')
    
    args = parser.parse_args()
    
    if args.list_examples:
        list_examples()
        return
    
    if args.input:
        process_input(args.input, args.type)
    else:
        print("Referee AI Decision Support System")
        print("==================================")
        print("\nUsage:")
        print("  python src/main.py --input <file_path> --type <video|image>")
        print("  python src/main.py --list-examples")
        print("\nExample:")
        print("  python src/main.py --input examples/videos/sample.mp4 --type video")


def list_examples():
    """List all example files in the examples directory"""
    print("\nAvailable Example Videos:")
    print("-------------------------")
    video_files = list(EXAMPLES_VIDEOS_DIR.glob('*'))
    if video_files:
        for video_file in video_files:
            if video_file.is_file():
                print(f"  - {video_file.name}")
    else:
        print("  No example videos found. Add videos to examples/videos/")
    
    print("\nAvailable Example Pictures:")
    print("---------------------------")
    image_files = list(EXAMPLES_PICTURES_DIR.glob('*'))
    if image_files:
        for image_file in image_files:
            if image_file.is_file():
                print(f"  - {image_file.name}")
    else:
        print("  No example pictures found. Add images to examples/pictures/")


def process_input(input_path: str, input_type: str = None):
    """Process input video or image"""
    input_file = Path(input_path)
    
    if not input_file.exists():
        print(f"Error: File not found: {input_path}")
        return
    
    # Auto-detect type if not specified
    if input_type is None:
        video_extensions = {'.mp4', '.avi', '.mov', '.mkv'}
        image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp'}
        
        if input_file.suffix.lower() in video_extensions:
            input_type = 'video'
        elif input_file.suffix.lower() in image_extensions:
            input_type = 'image'
        else:
            print(f"Error: Cannot determine file type for: {input_path}")
            return
    
    print(f"\nProcessing {input_type}: {input_file.name}")
    print("=" * 50)
    
    if input_type == 'video':
        info = get_video_info(str(input_file))
        if info:
            print(f"Video Information:")
            print(f"  Resolution: {info['width']}x{info['height']}")
            print(f"  FPS: {info['fps']:.2f}")
            print(f"  Frame Count: {info['frame_count']}")
            print(f"  Duration: {info['duration']:.2f} seconds")
            print("\nNote: AI analysis will be implemented in future versions")
    
    elif input_type == 'image':
        image = load_image(str(input_file))
        if image is not None:
            print(f"Image Information:")
            print(f"  Shape: {image.shape}")
            print(f"  Size: {image.shape[1]}x{image.shape[0]}")
            print("\nNote: AI analysis will be implemented in future versions")


if __name__ == "__main__":
    main()
