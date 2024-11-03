# Video Downloader

A Python-based video downloader that supports YouTube, TikTok, and Instagram. This tool uses `yt-dlp` and `instaloader` to download videos in formats compatible with QuickTime without heavy processing requirements.

## Features

- Downloads videos from:
  - **YouTube**: Downloads the best available MP4 format.
  - **TikTok**: Downloads videos in MP4 format.
  - **Instagram**: Supports posts, reels, and profiles.
- Simplified format settings to reduce CPU usage, making downloads faster and more efficient.

## Requirements

- **Python 3.7+**
- **ffmpeg** (optional, only required for re-encoding if needed)
  
### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Video-Downloader.git
   cd Video-Downloader
   
2. Set up a virtual environment and install dependencies:

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

3. Run the code

```bash
python Video_Downloader.py
```

4. Enter the URL for the video (YouTube, TikTok, or Instagram).

4.1 Optionally, specify the save path, or press Enter to use the default (./downloads).

## Example

- Please provide the URL (YouTube, TikTok, or Instagram): https://youtu.be/sampleurl
- Enter the save path or press Enter to use './downloads':

## Code Explanation
1. The downloader tries to download videos in compatible formats without re-encoding to reduce CPU load.
2. It automatically handles downloading and merging audio and video streams when necessary.

## License
This project is licensed under the MIT License.


### Additional Notes

- Update the repository link (`https://github.com/yourusername/Video-Downloader.git`) with your actual GitHub repository URL.
- Make sure to include a `requirements.txt` file if you haven’t already, listing `yt-dlp
