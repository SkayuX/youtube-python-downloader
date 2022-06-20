from moviepy.editor import *
from pytube import YouTube 
import os
import sys

url = input("link ")

yt = YouTube(url)

stream = yt.streams.get_by_itag(22)

stream.download()

file = stream.title+".mp4"
file2 = stream.title+".mp3"

os.rename(file, file2)

os.replace(stream.title+".mp3", "music/"+stream.title+".mp3")