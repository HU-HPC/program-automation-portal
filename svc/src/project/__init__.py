from src.project.http.endpoints import *
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
app = Flask('project')
app.config['SECRET_KEY'] = 'random'
app.debug = True
toolbar = DebugToolbarExtension(app)
