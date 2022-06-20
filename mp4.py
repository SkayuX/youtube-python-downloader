from pytube import YouTube 
import os
import sys

url = input("link ")

yt = YouTube(url)

stream = yt.streams.get_by_itag(22)

stream.download()

os.replace(stream.title+".mp4", "videos/"+stream.title+".mp4")