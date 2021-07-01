from flask import Flask
from flask_restx import Api
from controllers.LoginController import login_controller
from controllers.LoginController import api as ns_login
from controllers.UsuarioController import usuario_controller
from controllers.UsuarioController import ns_usuario

import config

app = Flask(__name__)

CORS(app)

api = Api(app,
          version='1.0',
          title='Gerenciador de Tarefas',
          description='Aplicação para gerenciar tarefas - Devaria 2021',
          doc='/docs')

def add_namespaces():
    api.add_namespace(ns_login, path=config.API_BASE_URL)
    api.add_namespace(ns_usuario, path=config.API_BASE_URL+'/usuario')
    app.register_blueprint(ns_tarefa, path=config.API_BASE_URL + '/tarefa')

if __name__ == '__main__':
    add_namespaces()

    app.run(host=config.API_HOST, port=config.API_PORT, debug=config.DEBUG)
