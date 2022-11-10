import os

from pytube import YouTube

yt = YouTube('https://youtu.be/8p62rAu6IDM')

#target dir
path = "d:\\youtube"

r = yt.streams.filter(resolution="1080p").first().download(path, "v.mp4")
#r = yt.streams.filter(only_audio=True).first().download(path, "a.mp4")


#v = ffmpeg.input(os.path.join(path, "v.mp4"))
#a = ffmpeg.input(os.path.join(path, "a.mp4"))

#r = ffmpeg.concat(v,a, v=1,a=1).output(os.path.join(path, "Stas.mp4")).run()

print(r)