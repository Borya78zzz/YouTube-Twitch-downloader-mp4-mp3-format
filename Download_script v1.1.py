import os
import sys
from yt_dlp import YoutubeDL

def download():
    print("What platform?")
    platform = str(input()).strip().lower()
    
    if platform in ["yt", "youtube"]:
        SAVE_DIR = r"D:\Downloader\YT"
        print("send youtube link")
        urls = str(input()).strip()
        
        if "youtube.com" in urls or "youtu.be" in urls:
            print("mp4 or mp3")
            form = str(input()).strip().lower()
            
            common_opts = {
                "http_headers": {
                    "User-Agent": "Mozilla/5.0"
                },
                "js_runtime": "none",
                "extractor_args": {
                    "youtube": {
                        "player_client": ["android"]
                    }
                },
                "youtube_include_dash_manifest": False
            }
            
            if form == "mp4":
                ydl_opts = {
                    **common_opts,
                    "outtmpl": os.path.join(SAVE_DIR, "%(title)s.%(ext)s"),
                    "format": "b",
                    "merge_output_format": "mp4"
                }
            elif form == "mp3":
                ydl_opts = {
                    **common_opts,
                    "outtmpl": os.path.join(SAVE_DIR, "%(title)s.%(ext)s"),
                    "format": "bestaudio",
                    "postprocessors": [{
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192"
                    }]
                }
            else:
                print("wrong format")
                return 0
            
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([urls])
            print("done!")
            return 0

    if platform in ["twitch", "tw"]:
        SAVE_DIR = r"D:\Downloader\Twitch"
        print("send twitch link")
        urls = str(input()).strip()
        if "twitch.tv" in urls:
            print("mp4 or mp3")
            form = str(input()).strip().lower()
            if form == "mp4":
                ydl_opts = {
                    "outtmpl": os.path.join(SAVE_DIR, "%(title)s.%(ext)s"),
                    "format": "bestvideo+bestaudio/best",
                    "http_headers": {
                        "User-Agent": "Mozilla/5.0"
                    }
                }
            elif form == "mp3":
                ydl_opts = {
                    "outtmpl": os.path.join(SAVE_DIR, "%(title)s.%(ext)s"),
                    "format": "bestaudio",
                    "http_headers": {
                        "User-Agent": "Mozilla/5.0"
                    },
                    "postprocessors": [{
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192"
                    }]
                }
            else:
                print("wrong format")
                return 0

            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([urls])
            print("done!")
            return 0
    else:
        print("Sorry, platform not available!")
        return 0

if __name__ == "__main__":
    if not os.path.exists(r"D:\Downloader\YT"): os.makedirs(r"D:\Downloader\YT")
    if not os.path.exists(r"D:\Downloader\Twitch"): os.makedirs(r"D:\Downloader\Twitch")
    while True:
        try:
            download()
        except Exception as e:
            print(f"Error: {e}")
