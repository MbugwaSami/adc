
from flask import Blueprint
from flask_restful import Api, Resource
#from .views import ProductsApi, SingleProductAp

app_v1 = Blueprint('app_v1',__name__, url_prefix="/api/v1")
api_v1 = Api(app_v1)
