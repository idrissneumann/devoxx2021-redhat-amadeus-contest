from flask_restful import Resource
from http_utils import *
from amadeus_utils import *

class AmadeusEndPoint(Resource):
    def get(self):
        args = get_args()
        origin = get_arg(args, 'origin')
        destination = get_arg(args, 'destination')
        departure_date = get_arg(args, 'departure_date')
        as_array = cast_boolean(get_arg(args, 'as_array'))

        return flight_offers_search(origin, destination, departure_date, as_array)
