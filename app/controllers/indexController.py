from flask import render_template
import os.path


def root_dir():
    return os.path.abspath(os.path.dirname(__file__))


def indexCtrl():
    return render_template('index.html', title='Home')
