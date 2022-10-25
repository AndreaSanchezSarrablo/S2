
import os

#Ask the user for a number of seconds
N = int(input('Enter the number of seconds you want form the video:'))

#We cut N seconds from the video starting from the begining, we are specifiying to cut the video from time = 0 to time = N seconds
os.system("ffmpeg -i bbbVideo.mp4 -ss 0 -t " +str(N) + " -c:v copy -c:a copy cuttedVideo.mp4")

