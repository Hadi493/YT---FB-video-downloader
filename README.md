# 🎥 Video Downloader Pro

A powerful and user-friendly Python tool to download videos from YouTube and Facebook with ease! This tool automatically downloads videos in the best available quality and saves them to your Videos/TTR directory.

## ✨ Features

- 🎯 Simple and interactive command-line interface
- 📺 Support for both YouTube and Facebook videos
- 🎮 Real-time download progress display
- 🎨 Beautiful colored output for better user experience
- 📁 Organized downloads in your Videos/TTR folder
- 🚀 Downloads in best available quality
- ⚡ Fast and efficient downloads using yt-dlp

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.7 or higher
- pip (Python package installer)

## 📥 Installation

1. Clone or download this repository:
```bash
git clone https://github.com/Hadi493/YT---FB-video-downloader.git
cd YT---FB-video-downloader
source .venv/bin/activate
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## 🚀 How to Use

1. Open your terminal and navigate to the project directory:
```bash
cd path/to/video-downloader
```

2. Run the script:
```bash
python main.py
```

3. When the program starts:
   - You'll see a welcome message
   - Simply paste the URL of the video you want to download
   - The video will be saved to `/home/cyber-green/Videos/TTR/`
   - To quit the program, type 'q' and press Enter

## 📝 Example Usage

```
$ python main.py

Video Downloader - YouTube & Facebook
Enter 'q' to quit

Enter video URL: https://www.youtube.com/watch?v=example
Fetching video information...
Downloading: 45.2%
Download completed. Converting...
Successfully downloaded: Example Video
```

## 📂 Where to Find Your Downloads

All downloaded videos are automatically saved to:
```
/home/cyber-green/Videos/TTR/
```

## ⚠️ Important Notes

- Make sure you have enough disk space before downloading videos
- Download speed depends on your internet connection
- Some videos might be restricted or private and cannot be downloaded
- Always respect copyright and terms of service of the platforms

## 🔧 Troubleshooting

If you encounter any issues:

1. Make sure you have the latest version of the requirements:
```bash
pip install --upgrade -r requirements.txt
```

2. Verify that the video URL is correct and accessible
3. Check if you have write permissions in the TTR directory
4. Ensure your internet connection is stable

## 📜 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Feel free to fork this repository and submit pull requests. All contributions are welcome!