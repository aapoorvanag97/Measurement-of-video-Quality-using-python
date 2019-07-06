import cv2
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
clip = VideoFileClip("skip.mp4")
print( clip.duration )
i = 0
while (i<clip.duration-1):
    ffmpeg_extract_subclip("skip.mp4", i, i+1, targetname="app"+str(i)+".mp4")
    i+=1
   
tresh = input("Enter threshold value")
c = float(tresh)
j = 0
while (j<clip.duration-1):
    cam = cv2.VideoCapture("app"+str(j)+".mp4")
    fps = cam.get(cv2.CAP_PROP_FPS)
    print("time",j,"sec",(fps))
    if fps < c:
       print("deviation")
    j+=1
