from pytube import YouTube

def download_video(url, path='./'):
    try:
        # Create a YouTube object using the URL
        yt = YouTube(url)

        # Choose the stream with the highest resolution
        stream = yt.streams.get_highest_resolution()

        # Download the video
        print(f"Downloading '{yt.title}'...")
        stream.download(path)
        print("Download completed!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace with the YouTube video URL you want to download
    video_url = input("Enter the YouTube video URL: ")

    # Call the download function
    download_video(video_url)
