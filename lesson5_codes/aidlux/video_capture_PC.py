import cv2

cap = cv2.VideoCapture("video1.mp4")
frame_id = 0
while cap.isOpened():
    ok, image = cap.read()
    if not ok:
        print("Camera cap over!")
        continue
    frame_id += 1
    if not int(frame_id) % 5 == 0: continue
    image = cv2.resize(image,(900,600))
    cv2.imshow("image",image)
    cv2.waitKey(10)