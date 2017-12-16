from flask_restplus import Api
from flask import Blueprint

apis = Blueprint('api', __name__)

api = Api(apis, version='1.0', title='Sports API',
    description='sports fixtures, standings and livescore API',
)

from .sports import api as teams
from .api_v2 import api as api_v2

api.add_namespace(teams)
api.add_namespace(api_v2)