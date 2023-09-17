from config import app
from Src.Router import Router
from flask import Flask


app.register_blueprint(Router)
