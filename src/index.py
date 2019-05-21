from flask import Flask, render_template, request, jsonify
from train_md import loadmodel
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static/docs')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def get_file_content():
    pass


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')
    
@app.route("/results", methods=["GET", "POST"])
def results():
    content = ""
    if request.method == "POST":
        if 'doc-file' in request.files:
            file = request.files['doc-file']
            content = get_file_content(file)
            # path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
            # file.save(path)
        else:
            content = request.form['content']
            
    model = loadmodel()
    res = model.predict(
        [content]
    )

    if not res:
        return "not found"

    return jsonify({
        "res": res.tolist(),
    })

if __name__ == "__main__":
    app.run()