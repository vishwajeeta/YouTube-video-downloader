import os
import yt_dlp
import imageio_ffmpeg


def download_video(url):
    def progress_hook(d):
        if d['status'] == 'downloading':
            percent = d.get('_percent_str', '').strip()
            speed = d.get('_speed_str', '').strip()
            eta = d.get('_eta_str', '').strip()
            print(f"Downloading... {percent} | Speed: {speed} | ETA: {eta}", end='\r')
        elif d['status'] == 'finished':
            print("\n✅ Download completed!")

    # Ensure the downloads folder exists
    os.makedirs("downloads", exist_ok=True)

    # Get ffmpeg binary path
    ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'ffmpeg_location': ffmpeg_path,
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'progress_hooks': [progress_hook],
        'quiet': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print("\n❌ Error during download:", e)


if __name__ == "__main__":
    url = input("Enter YouTube video URL: ").strip()
    if url:
        download_video(url)
    else:
        print("No URL provided.")
