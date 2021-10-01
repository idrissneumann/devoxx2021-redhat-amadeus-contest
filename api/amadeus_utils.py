from amadeus import Client, ResponseError
from common_utils import *
from logging_utils import *

amadeus = Client(
    client_id=get_env_value('AMADEUS_API_KEY'),
    client_secret=get_env_value('AMADEUS_API_SECRET')
)

def flight_offers_search(origin, destination, departure_date):
    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=origin,
            destinationLocationCode=destination,
            departureDate=departure_date,
            adults=1)
        result = []
        for item in response.data:
            result.append({
                "departure": item['itineraries'][0]['segments'][0]['departure']['at'],
                "arrival": item['itineraries'][-1]['segments'][-1]['arrival']['at'],
                "price": "{} {}".format(item['price']['total'], item['price']['currency'])
            })
        return result
    except ResponseError as error:
        log_msg('ERROR', 'flight_offers_search', error)
        return None
