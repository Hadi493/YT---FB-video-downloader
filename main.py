import os
from rich.prompt import Prompt

def download_video(url):
    from yt_dlp import YoutubeDL

    home_dir = os.path.expanduser("~")
    download_dir = os.path.join(home_dir, "Videos", "for-YT")
    os.makedirs(download_dir, exist_ok=True)

    ydl_opts = {
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    while True:
        url = Prompt.ask("\nEnter video URL")
        
        if url.lower() == 'q':
            break
            
        download_video(url)

if __name__ == "__main__":
    main()