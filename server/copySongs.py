import sys
import os
import shutil

# Copy songs from one directory to another
def copySongs(source="./songs/mp3/", destination="./../my_spotify/assets/song/"):
    try:
        os.mkdir(destination)
    except FileExistsError:
        pass
    for filename in os.listdir(source):
        shutil.copy(source + filename, destination)
        os.remove(source + filename)

if __name__ == "__main__":
    copySongs()