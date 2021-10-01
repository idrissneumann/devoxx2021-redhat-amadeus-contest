from amadeus import Client, ResponseError
from common_utils import *
from logging_utils import *

amadeus = Client(
    client_id=get_env_value('AMADEUS_API_KEY'),
    client_secret=get_env_value('AMADEUS_API_SECRET')
)

def flight_offers_search(origin, destination, departure_date, as_array):
    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=origin,
            destinationLocationCode=destination,
            departureDate=departure_date,
            adults=1)
        result = []
        for item in response.data:
            departure = item['itineraries'][0]['segments'][0]['departure']['at']
            arrival = item['itineraries'][-1]['segments'][-1]['arrival']['at']
            price = "{} {}".format(item['price']['total'], item['price']['currency'])
            vclass = item['travelerPricings'][0]['fareDetailsBySegment'][0]['cabin']

            if as_array:
                result.append([departure, arrival, price, vclass])
            else:
                result.append({
                    "departure": departure,
                    "arrival": arrival,
                    "price": price,
                    "class": vclass
                })
        return result
    except ResponseError as error:
        log_msg('ERROR', 'flight_offers_search', error)
        return None
