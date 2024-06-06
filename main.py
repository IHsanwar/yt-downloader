from flask import Flask, request, render_template, send_file
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    ytlink = request.form['ytlink']
    ytdownload = YouTube(ytlink)
    stream = ytdownload.streams.get_highest_resolution()
    file_path = stream.download()


    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
