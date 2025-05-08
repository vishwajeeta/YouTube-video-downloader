import yt_dlp

def get_video_info(url):
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        formats = info.get('formats', [])
        filtered = [f for f in formats if f.get('filesize') and f.get('vcodec') != 'none']
        return info.get('title'), filtered

def download_video(url, format_id):
    def progress_hook(d):
        if d['status'] == 'downloading':
            percent = d.get('_percent_str', '').strip()
            print(f"Downloading... {percent}", end='\r')
        elif d['status'] == 'finished':
            print("\nDownload completed!")

    ydl_opts = {
        'format': format_id,
        'progress_hooks': [progress_hook],
        'outtmpl': 'downloads/%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    url = input("Enter YouTube URL: ").strip()
    try:
        title, formats = get_video_info(url)
        print(f"\nAvailable formats for: {title}\n")

        for idx, f in enumerate(formats):
            size_mb = f['filesize'] / (1024 * 1024)
            print(f"{idx + 1}. {f['format_id']} - {f['format_note']} - {f['ext']} - {size_mb:.2f} MB")

        choice = int(input("\nSelect the format number to download: ")) - 1
        selected_format_id = formats[choice]['format_id']
        download_video(url, selected_format_id)

    except Exception as e:
        print("Error:", e)
