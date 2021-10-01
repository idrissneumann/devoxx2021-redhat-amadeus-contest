from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from api_root import RootEndPoint
from api_manifest import ManifestEndPoint
from api_amadeus import AmadeusEndPoint

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)

health_check_routes = ['/', '/health', '/health/', '/v1/health', '/v1/health/']
manifest_routes = ['/manifest', '/manifest/', '/v1/manifest', '/v1/manifest/']
amadeus_routes = ['/amadeus', '/amadeus/', '/v1/amadeus', '/v1/amadeus/']

api.add_resource(RootEndPoint, *health_check_routes)
api.add_resource(ManifestEndPoint, *manifest_routes)
api.add_resource(AmadeusEndPoint, *amadeus_routes)

if __name__ == '__main__':
    app.run()
