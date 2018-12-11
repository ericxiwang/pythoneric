import sys,os,json
from flask import Flask, render_template, request, redirect, url_for, session, current_app, Response

from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',title="AAAAA")

@app.route('/upload',methods=['POST','GET'])
def upload_img():
    if request.method == 'POST':
        input_image = request.files['file']
        basepath = os.path.dirname(__file__)
        upload_path = os.path.join(basepath, 'static',secure_filename(input_image.filename))
        input_image.save(upload_path)
        return redirect(url_for('list_uploaded_files'))
    return render_template('upload_image.html')