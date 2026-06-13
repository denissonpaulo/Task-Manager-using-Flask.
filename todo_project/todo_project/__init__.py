from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


app = Flask(__name__)

import logging
from logging.handlers import SysLogHandler

# Configuração do Syslog nativo para auditoria DevSecOps
syslog_handler = SysLogHandler(address='/dev/log')
syslog_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - TaskManagerSecurity - %(levelname)s - %(message)s')
syslog_handler.setFormatter(formatter)
app.logger.addHandler(syslog_handler)

app.config['SECRET_KEY'] = '45cf93c4d41348cd9980674ade9a7356'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login' 
login_manager.login_message_category = 'danger'

bcrypt = Bcrypt(app)

# Always put Routes at end
from todo_project import routes
