import yt_dlp
from rich.console import Console
from rich.prompt import Prompt
from rich import print as rprint

console = Console()

def download_video(url: str, output_path: str = "/home/cyber-green/Videos/TTR/%(title)s.%(ext)s"):
    """
    Download video from YouTube or Facebook
    """
    ydl_opts = {
        'format': 'best',  # Download best quality
        'outtmpl': output_path,  # Output template
        'quiet': False,  # Show progress
        'no_warnings': False,
        'progress_hooks': [progress_hook],
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            rprint(f"[yellow]Fetching video information...[/yellow]")
            info = ydl.extract_info(url, download=True)
            rprint(f"[green]Successfully downloaded: {info['title']}[/green]")
    except Exception as e:
        rprint(f"[red]Error downloading video: {str(e)}[/red]")

def progress_hook(d):
    if d['status'] == 'downloading':
        if 'total_bytes' in d:
            percentage = (d['downloaded_bytes'] / d['total_bytes']) * 100
            console.print(f"Downloading: {percentage:.1f}%", end='\r')
    elif d['status'] == 'finished':
        console.print("\nDownload completed. Converting...")

def main():
    rprint("[bold blue]Video Downloader - YouTube & Facebook[/bold blue]")
    rprint("[yellow]Enter 'q' to quit[/yellow]")
    
    while True:
        url = Prompt.ask("\nEnter video URL")
        
        if url.lower() == 'q':
            break
            
        download_video(url)

if __name__ == "__main__":
    main()