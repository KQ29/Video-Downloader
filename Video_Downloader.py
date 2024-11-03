import os
import logging
import instaloader
from TikTokApi import TikTokApi
import yt_dlp

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def download_youtube_video(url, save_path):
    ydl_opts = {
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'ffmpeg_location': '/usr/local/bin/ffmpeg'  # Path for ffmpeg
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
        api = TikTokApi()
        video = api.video(url=url)
        video_data = video.bytes()
        video_id = video.id
        file_path = os.path.join(save_path, f'tiktok_{video_id}.mp4')
        with open(file_path, 'wb') as f:
            f.write(video_data)
        logging.info(f"TikTok video downloaded: {file_path}")
    except Exception as e:
        logging.error(f"Error downloading TikTok video: {str(e)}")

def download_instagram_content(url, save_path):
    try:
        # Initialize Instaloader
        loader = instaloader.Instaloader(dirname_pattern=save_path)
        
        # Prompt for Instagram login if needed
        username = input("Enter your Instagram username (or press Enter to skip): ").strip()
        if username:
            password = input("Enter your Instagram password: ").strip()
            loader.login(username, password)

        # Check if URL is a post or reel and download accordingly
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

def download_content_from_url(url, save_path='./downloads'):
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
    save_path = input("Enter the save path or press Enter to use './downloads': ") or './downloads'
    os.makedirs(save_path, exist_ok=True)
    download_content_from_url(url, save_path)
