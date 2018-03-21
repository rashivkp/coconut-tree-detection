from flask import Flask, flash, render_template, request, redirect, url_for
import os, uuid
from werkzeug.utils import secure_filename
from inference import run_inference
from settings import Config

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])
app = Flask(__name__)
app.secret_key = Config.SECRET_KEY
app.config['UPLOAD_FOLDER'] = 'uploads'


@app.route('/', methods=['GET', 'POST'])
def hello():

    output_filename = None
    coconut_count = None
    if request.method == 'POST':
        if 'image' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['image']
        if file.filename == '':
            flash( 'No selected file' )
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
                filename = "%s%s" % (uuid.uuid4(), filename)

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            coconut_count = run_inference(os.path.join(app.config['UPLOAD_FOLDER'], filename), filename)

            return redirect(url_for('result', file=filename, count=coconut_count, _anchor="output"))
        # check if the post request has
    return render_template('index.html', output_filename=None, coconut_count=None)

@app.route('/<file>/<count>', methods=['GET'])
def result(file, count):
    return render_template('index.html', file=file, count=count)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

if __name__=='__main__':
    app.run(debug=True, port=5000)
