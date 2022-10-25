#EXERCICI3

import os
#First of all we will cut the bbbVideo to 30 seconds to then resize that video
os.system("ffmpeg -i bbbVideo.mp4 -ss 0 -to 30 -c:v copy -c:a copy cutVideo30seg.mp4")

#Resize the bbbVideo to 720p
os.system("ffmpeg -i cutVideo30seg.mp4 -vf scale=-1:720 bbbVideo_720p.mp4")

#Resize the 30 seconds bbbVideo to 480p
os.system("ffmpeg -i cutVideo30seg.mp4 -vf scale=-1:480 bbbVideo_480.mp4")

#Resize the 30 seconds bbbVideo to 360x240
os.system("ffmpeg -i cutVideo30seg.mp4 -vf scale=360:240 bbbVideo_260x240.mp4")

#Resize the 30 seconds bbbVideo to 160x120
os.system("ffmpeg -i cutVideo30seg.mp4 -vf scale=160:120 bbbVideo_160x120.mp4")


