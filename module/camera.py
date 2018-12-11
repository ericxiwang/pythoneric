import cv2
import time
class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture('rtsp://admin:xsight@123@10.16.10.222:554/Streaming/Channels/001')
        self.img_path = "static/images/faces/eric.jpg"
        self.cascPath_1 = "/usr/local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml"
        self.cascPath_2 = "/usr/local/lib/python3.7/site-packages/cv2/data/haarcascade_eye.xml"
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')

    def __del__(self):
        self.video.release()

    def get_frame(self):
        faceCascade = cv2.CascadeClassifier(self.cascPath_1)

        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        '''image = cv2.imread(self.img_path)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(30, 30))
        print(faces)
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)'''

        ret, jpeg = cv2.imencode('.jpg', image)






        return jpeg.tobytes()




if __name__ == '__main__':
    print("AA")