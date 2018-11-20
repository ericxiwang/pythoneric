import cv2


class VideoCamera(object):
    def __init__(self,video_link):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(video_link)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

if __name__ == '__main__':
    vcap=VideoCamera("rtsp://admin:xsight@123@10.16.10.222:554/Streaming/Channels/001")
    while (1):
        ret, frame = vcap.video.read()
        cv2.imshow('video', frame)
        cv2.waitKey(1)
