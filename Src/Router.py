from flask import Blueprint, render_template
from Src.Resources.Amplitude import Amplitude
from Src.Resources.Profundidade import Profundidade
from Src.Resources.Aprofundamento import Aprofundamento
from Src.Resources.Bidirecional import Bidirecional

Router = Blueprint('router', __name__)

teste = [
    "2-4",
    "3-5",
    "3-6",
    "4-5",
    "4-6",
    "5-5",
    "5-3",
    "4-3",
    "3-3",
    "3-2",
    "4-2",
    "5-6",
    "6-5",
    "6-4",
    "6-3",
    "5-2"
];


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

@Router.route("/amplitude")
def amplitude():
    search = Amplitude(teste, "3-5", "6-3")
    
    return search.make()

@Router.route("/profundidade", defaults={'limit':None})
@Router.route("/profundidade/<int:limit>")
def profundidade(limit):
    search = Profundidade(teste, "3-5", "6-3")
    
    return search.make(limit)

@Router.route("/aprofundamento")
def aprofundamento():
    search = Aprofundamento(teste, "3-5", "6-3")
    
    return search.make(len(teste))


@Router.route("/bidirecional")
def bidirecional():
    search = Bidirecional(teste, "3-5", "6-3")
    
    return search.make()