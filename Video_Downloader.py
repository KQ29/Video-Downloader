import os
import logging
import instaloader
import yt_dlp  # For YouTube and TikTok downloads

# Constants
DEFAULT_SAVE_PATH = './downloads'
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'

# Set up logging
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

def download_youtube_video(url, save_path):
    # Simplified options to download the best available MP4 format without enhancements
    ydl_opts = {
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        'format': 'mp4',  # Best available MP4 format without any quality enhancements
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            logging.info(f"Downloading YouTube video from URL: {url}")
            ydl.download([url])
            logging.info("YouTube video downloaded successfully.")
    except Exception as e:
        logging.error(f"Error downloading YouTube video: {str(e)}")

def download_tiktok_video(url, save_path):
    try:
        ydl_opts = {
            'outtmpl': os.path.join(save_path, 'tiktok_%(id)s.%(ext)s'),
            'format': 'mp4',  # Only download mp4 format
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            logging.info(f"Downloading TikTok video from URL: {url}")
            ydl.download([url])
            logging.info("TikTok video downloaded successfully.")
    except Exception as e:
        logging.error(f"Error downloading TikTok video: {str(e)}")

def download_instagram_content(url, save_path):
    try:
        loader = instaloader.Instaloader(dirname_pattern=save_path)
        username = input("Enter your Instagram username (or press Enter to skip): ").strip()
        if username:
            password = input("Enter your Instagram password: ").strip()
            loader.login(username, password)

        if "/p/" in url or "/reel/" in url:
            shortcode = url.split("/")[-2]
            post = instaloader.Post.from_shortcode(loader.context, shortcode)
            loader.download_post(post, target=save_path)
            logging.info("Instagram post or reel downloaded successfully.")
        elif "/profile/" in url:
            profile_name = url.split("/")[-2]
            loader.download_profile(profile_name, profile_pic_only=False)
            logging.info(f"Instagram profile content downloaded for: {profile_name}")
        else:
            logging.error("Unsupported Instagram link format.")
    except Exception as e:
        logging.error(f"Error downloading Instagram content: {str(e)}")

def download_content_from_url(url, save_path=DEFAULT_SAVE_PATH):
    if "youtube.com" in url or "youtu.be" in url:
        download_youtube_video(url, save_path)
    elif "tiktok.com" in url:
        download_tiktok_video(url, save_path)
    elif "instagram.com" in url:
        download_instagram_content(url, save_path)
    else:
        logging.error("Unsupported platform. Please provide a valid YouTube, TikTok, or Instagram URL.")

if __name__ == "__main__":
    url = input("Please provide the URL (YouTube, TikTok, or Instagram): ")
    save_path = input(f"Enter the save path or press Enter to use '{DEFAULT_SAVE_PATH}': ") or DEFAULT_SAVE_PATH
    os.makedirs(save_path, exist_ok=True)
    download_content_from_url(url, save_path)
