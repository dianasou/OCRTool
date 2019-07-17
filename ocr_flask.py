'''Credit to source for solution
https://stackabuse.com/pytesseract-simple-python-optical-character-recognition/
'''

#import necessary modules/libraries
import os
from flask import Flask, render_template, request
from ocr_core import ocr_core

app = Flask(__name__)

upload_folder = '/uploads'
allowed_extensions = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions

@app.route('/', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        #check if post request has file 
        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected')
        file = request.files['file']
        #if user does not select file, browser submits empty part without filename
        if file.filename == '':
            return render_template('upload.html', msg='No file selected')

        if file and allowed_file(file.filename):
            file.save(os.path.join(os.getcwd() + upload_folder, file.filename))

            #call the OCR function on image file
            extracted_text = ocr_core(file)

            #extract the text and display it
            return render_template('upload.html',
                                   result = 'Result of extracted text:',
                                   extracted_text = extracted_text,
                                   img_src = upload_folder + file.filename)
    elif request.method == 'GET':
        return render_template('upload.html')

if __name__ == '__main__':
    app.run()