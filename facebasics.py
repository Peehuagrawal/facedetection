import cv2
import mediapipe as mp
import time

cap= cv2.VideoCapture("faceimages/1.mp4")
pTime=0

mpFace= mp.solutions.face_detection
mpDraw= mp.solutions.drawing_utils
faceDetection= mpFace.FaceDetection()

while True:
    success, img= cap.read()
    
    imgRGB= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results= faceDetection.process(imgRGB)
    #print(results)

    if results.detections:
        for id, detection in enumerate(results.detections):
            mpDraw.draw_detection(img, detection)
            #print(id,detection)
            #print(detection.score)
            #print(detection.location_data.relative_bounding_box)
            bboxC=detection.location_data.relative_bounding_box
            ih,iw,ic= img.shape
            bbox= 
                

    cTime= time.time()
    fps= 1/(cTime-pTime)
    cv2.putText(img, f'FPS:{int(fps)}', (28,78), cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),2)
    cv2.imshow("Image", img)
    cv2.waitKey(20)