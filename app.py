from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint
import os

image_folder = os.path.join('static', 'images')

app = Flask(__name__)


@app.route("/")
def index():
	filename = os.path.join(image_folder, 'data-scientist.jpg')
	return render_template('index.html', ds_image = filename)




if __name__ == '__main__':
        app.run(debug=True)