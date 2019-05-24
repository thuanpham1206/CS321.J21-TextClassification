from flask import Flask, render_template, request, jsonify
from train_md import loadmodel, get_categories
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static/docs')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def get_file_content():
    pass


@app.route("/", methods=["GET", "POST"])
def index():
    categories = get_categories()
    print(type(categories))
    return render_template('index.html', categories=categories)
    
@app.route("/results", methods=["GET", "POST"])
def results():
    content = ""
    if request.method == "POST":
        # Get upload file (.doc, .txt, ...)
        # currently not in use
        if 'doc-file' in request.files:
            file = request.files['doc-file']
            content = get_file_content(file)
            path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
            file.save(path)
        else:
            content = request.form['content']
    
    # load the model
    model = loadmodel()

    # predict the content
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