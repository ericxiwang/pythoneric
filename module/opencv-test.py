import cv2,os
import numpy as np


img_path='static/images/faces/trump.jpg'
video_link="rtsp://admin:xsight@123@10.16.10.222:554/Streaming/Channels/001"

'''image=cv2.imread(img_path,0)


cv2.imshow("test",image)

cv2.waitKey(0)
cv2.destroyAllWindows()'''


def rtsp_streaming(video_link):
    vcap = cv2.VideoCapture(video_link)
    while(1):
        ret,frame = vcap.read()
        cv2.imshow('video',frame)
        cv2.waitKey(1)

if __name__ == '__main__':
    rtsp_streaming(video_link=video_link)