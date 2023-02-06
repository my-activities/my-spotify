import youtube_downloader
import file_converter
import sys

if (len(sys.argv) == 2):
    link = sys.argv[1]
    print("Downloading...")
    filename = youtube_downloader.download_video(link, 'low')
    print("Converting...")
    file_converter.convert_to_mp3(filename)
