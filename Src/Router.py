from flask import Blueprint, render_template

Router = Blueprint('router', __name__)

@Router.route("/")
@Router.route("/home")
def home():
    return render_template('Home.html') 

@Router.route("/grid")
def grid():
    return render_template('Grid.html') 

@Router.route("/loading")
def loading():
    return render_template('animationLoading.html')