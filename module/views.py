import sys,os,json
from flask import Flask, render_template, request, redirect, url_for, session, current_app, Response
import requests
from werkzeug.utils import secure_filename
camera_link="rtsp://admin:xsight@123@10.16.10.222:554/Streaming/Channels/001"
from camera import VideoCamera
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    frame = camera.get_image()
    yield (b'--frame\r\n'
           b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    '''while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')'''

@app.route('/video_feed')
def video_feed(link=camera_link):

    return Response(gen(VideoCamera(link)),
                    mimetype='multipart/x-mixed-replace; boundary=frame')




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
