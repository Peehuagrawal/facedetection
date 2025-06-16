import cv2
import mediapipe as mp
import time

cap= cv2.VideoCapture("faceimages/2.mp4")
pTime=0

while True:
    success, img= cap.read()
    
    cTime= time.time()
    fps= 1/(cTime-pTime)
    cv2.putText(img, f'FPS:{int(fps)}', (28,78), cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),2)
    cv2.imshow("Image", img)
    cv2.waitKey(10)