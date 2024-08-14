from flask import Flask, render_template, request
import dropbox

app = Flask(__name__)
dbx = dropbox.Dropbox("hi this is sivaganapathi,unable to commit in github so here i changed my token")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    if not file:
        return "No file selected"
    filename = file.filename
    if not filename:
        return "No file selected"
    dbx.files_upload(file.read(), f"/images/{filename}")
    return "File uploaded successfully"

if __name__ == '__main__':
    app.run(debug=True)
