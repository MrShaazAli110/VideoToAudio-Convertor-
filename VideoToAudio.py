import moviepy 
from tkinter.filedialog import *

vid = askopenfilename()
video = moviepy.VideoFileClip(vid)

aud = video.audio
aud.write_audiofile("File.mp3")

print("--End--")
