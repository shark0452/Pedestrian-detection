import cv2
from cvs import * 

cap = cvs.VideoCapture("/home/lesson2_codes/video1.mp4")
frame_id = 0
while True:
    frame = cap.read()
    if frame is None:
        print("Camera cap over!")
        continue
    frame_id += 1
    if not int(frame_id) % 5 == 0: continue
    cvs.imshow(frame)