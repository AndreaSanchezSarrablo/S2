#EXERCICI2

import os

#Extract the YUV histogram from the input video and then show both the input video and the YUV histogram along time, we are rescaling the size of the histogram
#that will take place in the upper left corner. And then we do an overlay of the input vide and the YUV histogram.
os.system('ffmpeg -i cuttedVideo.mp4 -vf "split=2[a][b],[b]histogram,scale = 150:150,format=yuv420p[hh],[a][hh]overlay" -c:a copy video_histogram.mp4')



