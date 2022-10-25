#EXERCICI4

import os

#Change the stereo audio into mono output
os.system ("ffmpeg -i bbbVideo.mp4 -ac 1 bbbVideo_mono.mp4")

#Change the  mono audio into a stereo output
os.system("ffmpeg -i bbbVideo_mono.mp4 -ac 2 bbbVideo_stereo.mp4")
