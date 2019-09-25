from flask import Flask, render_template, request
from werkzeug import secure_filename
import subprocess
import sys
app = Flask(__name__)

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      result = subprocess.Popen(["python", "autograde.py", ">", "sample.txt" ], stdout=subprocess.PIPE)
      output, err = result.communicate()
      return render_template('sample.html', text = output)
   
if __name__ == '__main__':
   app.run(host ='0.0.0.0', debug=True)
