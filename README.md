# YouTube Downloader

A Python-based YouTube video downloader that allows you to download videos from YouTube with customizable quality settings and progress tracking.

## Features

- Download YouTube videos in various quality formats
- Progress bar with download status
- Command-line interface for easy usage
- Customizable output directory
- Error handling for unavailable videos
- Support for both specific quality and highest available quality

## Requirements

- Python 3.6+
- pytubefix
- tqdm

## Installation

1. Clone or download this repository
2. Install the required dependencies:

```bash
pip install pytubefix tqdm
```

## Usage

### Command Line Interface

```bash
python src/main.py <YouTube_URL> [options]
```

#### Arguments

- `url`: The YouTube video URL to download (required)
- `-q, --quality`: Video quality (e.g., 720p, 1080p, highest) - default: highest
- `-o, --output_path`: Output directory to save the video - default: current directory

#### Examples

```bash
# Download video with highest quality
python src/main.py "https://www.youtube.com/watch?v=VIDEO_ID"

# Download video in 720p quality
python src/main.py "https://www.youtube.com/watch?v=VIDEO_ID" -q 720p

# Download video to specific directory
python src/main.py "https://www.youtube.com/watch?v=VIDEO_ID" -o "/path/to/downloads"

# Combine quality and output path options
python src/main.py "https://www.youtube.com/watch?v=VIDEO_ID" -q 1080p -o "/home/user/videos"
```

### Python Script Usage

```python
from src.main import YouTubeDownloader

# Create downloader instance
downloader = YouTubeDownloader(
    url="https://www.youtube.com/watch?v=VIDEO_ID",
    quality="720p",  # or "highest"
    output_path="./downloads"
)

# Start download
downloader.download()
```

## Project Structure

```
Youtube Downloader/
├── src/
│   ├── main.py          # Main downloader script
│   └── test.ipynb       # Jupyter notebook for testing
└── README.md            # This file
```

## Features Explained

### Quality Options
- `highest`: Downloads the highest available quality
- Specific resolutions: `720p`, `1080p`, `480p`, etc.

### Progress Tracking
The downloader includes a progress bar that shows:
- Download progress in bytes
- Current speed
- Estimated time remaining

### Error Handling
- Handles unavailable videos gracefully
- Shows available quality options if requested quality is not available
- Provides clear error messages

## Limitations

- Only downloads progressive streams (video + audio combined)
- Requires valid YouTube URLs
- Respects YouTube's terms of service

## Troubleshooting

### Common Issues

1. **Import Error**: Make sure you have installed pytubefix:
   ```bash
   pip install pytubefix
   ```

2. **Video Unavailable**: Some videos may be restricted or unavailable in your region.

3. **Quality Not Available**: If your requested quality is not available, the script will show you the available options.

## License

This project is for educational purposes. Please respect YouTube's terms of service and copyright laws when using this tool.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this project.
