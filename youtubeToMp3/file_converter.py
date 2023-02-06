from moviepy.editor import VideoFileClip
import os

def convert_to_mp3(filename, output_dir="./songs/mp3/"):
    try:
        os.mkdir("./songs/mp3")
    except FileExistsError:
        pass
    clip = VideoFileClip("./songs/mp4/" + filename)
    clip.audio.write_audiofile(output_dir + filename[:-4] + ".mp3")
    clip.close()
