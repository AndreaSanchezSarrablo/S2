#EXERCICI2

import os

#Extract the YUV histogram from the previous cutted video
os.system('ffmpeg -i cuttedVideo.mp4 -vf "split=2[a][b],[b]histogram,scale = 150:150,format=yuv420p[hh],[a][hh]overlay" -c:a copy video_histogram.mp4')

#Create new video with both images at the same time

