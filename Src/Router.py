from flask import Blueprint, render_template, request
from Src.Resources.Amplitude import Amplitude
from Src.Resources.Profundidade import Profundidade
from Src.Resources.Aprofundamento import Aprofundamento
from Src.Resources.Bidirecional import Bidirecional
from Src.Resources.CustoUniforme import CustoUniforme
from Src.Resources.Greedy import GreedySearch
# from Src.Resources.Aestrela import AStartSeach
# from Src.Resources.AIAestrela import AiaStartSeach

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
    ambient = request.args.get('ambient').split(',')
    beginning = request.args.get('beginning')
    destination = request.args.get('destination')

    search = Amplitude(ambient, beginning, destination)
    
    return search.make()

@Router.route("/profundidade", defaults={'limit':None})
@Router.route("/profundidade/<int:limit>")
def profundidade(limit):
    ambient = request.args.get('ambient').split(',')
    beginning = request.args.get('beginning')
    destination = request.args.get('destination')

    search = Profundidade(ambient, beginning, destination)
    
    return search.make(limit)

@Router.route("/aprofundamento")
def aprofundamento():
    ambient = request.args.get('ambient').split(',')
    beginning = request.args.get('beginning')
    destination = request.args.get('destination')

    search = Aprofundamento(ambient, beginning, destination)
    
    return search.make(len(teste))


@Router.route("/bidirecional")
def bidirecional():
    ambient = request.args.get('ambient').split(',')
    beginning = request.args.get('beginning')
    destination = request.args.get('destination')

    search = Bidirecional(ambient, beginning, destination)
    
    return search.make()

@Router.route("/custo_uniforme")
def custo_uniforme():
    ambient = request.args.get('ambient').split(',')
    beginning = request.args.get('beginning')
    destination = request.args.get('destination')

    search = CustoUniforme(ambient, beginning, destination)

    return search.make()

@Router.route("/greedy")
def greedy():
    ambient = request.args.get('ambient').split(',')
    beginning = request.args.get('beginning')
    destination = request.args.get('destination')

    search = GreedySearch(ambient, beginning, destination)

    return search.make()

# @Router.route("/aestrela")
# def aStar():
#     ambient = request.args.get('ambient').split(',')
#     beginning = request.args.get('beginning')
#     destination = request.args.get('destination')

#     search = AStartSeach(ambient, beginning, destination)

#     return search.make()

# @Router.route("/aiaestrela")
# def aiaStar():
#     ambient = request.args.get('ambient').split(',')
#     beginning = request.args.get('beginning')
#     destination = request.args.get('destination')

#     search = AiaStartSeach(ambient, beginning, destination)

#     return search.make()




