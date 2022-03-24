from flask import render_template, redirect, url_for
from main import app


@app.route('/hjem')
@app.route('/')
def hjem():
    return render_template('hjem.html')

