from flask import Flask, Blueprint
from App.api.v1.views.user_views import api_v1

my_app = Flask(__name__)

my_app.register_blueprint(api_v1, url_prefix="/api/v1")
