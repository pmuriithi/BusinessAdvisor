import os
import json
import xlrd
from xlrd import open_workbook
from flask import Flask, request, redirect, url_for,render_template
from werkzeug import secure_filename
from flask import send_from_directory
#where we store the uploaded file(use double slash to avoid the IOError22: invalid filename)
UPLOAD_FOLDER =  'C:\\Users\\POLY\\Google Drive\\Desktop\\UPC\\BIP\\project\\temp\\test'
#The file formats that are acceptable for upload
ALLOWED_EXTENSIONS = set(['xls','xlsx'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#check that the uploaded file is in the right format in our case .xls or .xlsx.
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
		   
@app.route('/')
def upload_data():
	return render_template('upload.html')


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename) 
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			#redirect the user to the URL of the uploaded file
            return redirect(url_for('uploaded_file',
                                    filename=filename))
	else:
		redirect(url_for('upload_data'))# we need to show a notification stating that the file cannot be found
		return 'Invalid file'
			
		
#serving the uploaded file. Takes in the filename as a parameter and finds it in the upload directory and shows it on the browser
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


							   
if __name__ == '__main__':
	app.debug = True
	app.run()