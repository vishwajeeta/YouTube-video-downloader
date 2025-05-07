from pytube import YouTube

# Function to track the progress of the download
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    print(f"Download Progress: {percentage:.2f}%")

def download_video(url, path='./'):
    try:
        # Create a YouTube object using the URL
        yt = YouTube(url, on_progress_callback=on_progress)

        # List available video streams
        print("Available streams:")
        streams = yt.streams.filter(progressive=True)  # Use progressive streams for video+audio

        # Display stream options with file size
        for i, stream in enumerate(streams):
            print(f"{i + 1}. {stream.resolution} - {stream.mime_type} - {stream.fps} fps - Size: {stream.filesize / (1024 * 1024):.2f} MB")

        # Ask user to choose the stream
        choice = int(input("Enter the stream number you want to download: ")) - 1
        stream = streams[choice]

        # Download the video
        print(f"Downloading '{yt.title}' in {stream.resolution}...")
        stream.download(path)
        print("Download completed!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace with the YouTube video URL you want to download
    video_url = input("Enter the YouTube video URL: ")

    # Call the download function
    download_video(video_url)
