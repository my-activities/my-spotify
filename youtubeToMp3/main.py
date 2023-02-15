import youtube_downloader
import file_converter
import sys
import os
import shutil

# copy songs from one directory to another
def copySongs(source="./songs/mp3/", destination="./../my_spotify/assets/song/"):
    try:
        os.mkdir(destination)
    except FileExistsError:
        pass
    for filename in os.listdir(source):
        shutil.copy(source + filename, destination)
        os.remove(source + filename)

if (len(sys.argv) == 2):
    link = sys.argv[1]
    print("Downloading...")
    filename = youtube_downloader.download_video(link, 'low')
    print("Converting...")
    file_converter.convert_to_mp3(filename)
    copySongs()
