import cv2
import sys
import numpy as np


img_path="static/images/faces/eric.jpg"
video_link="rtsp://admin:xsight@123@10.16.10.222:554/Streaming/Channels/001"




def open_image(img_path):
    cascPath_1 = "/usr/local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml"
    cascPath_2 = "/usr/local/lib/python3.7/site-packages/cv2/data/haarcascade_eye.xml"

    face_cascade = cv2.CascadeClassifier(cascPath_1)
    eye_cascade = cv2.CascadeClassifier(cascPath_2)

    image=cv2.imread(img_path)

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.4, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = image[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    cv2.imshow('img', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()





def rtsp_streaming(video_link):
    vcap = cv2.VideoCapture(video_link)

    while(1):
        ret,frame = vcap.read()
        cv2.imshow('video',frame)
        cv2.waitKey(1)

if __name__ == '__main__':
    #rtsp_streaming(video_link=video_link)
    open_image(img_path)