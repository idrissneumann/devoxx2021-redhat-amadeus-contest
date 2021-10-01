from flask_restful import Resource

class AirportsEndPoint(Resource):
    def get(self):
        return {
            "CDG": "Paris CDG",
            "ORY": "Paris Orly",
            "TUN": "Tunis",
            "CMN": "Casablanca",
            "CAI": "Cairo",
            "MED": "Madinah",
            "JED": "Djeddah",
            "RUH": "Riyadh",
            "LCY": "London",
            "SXF": "Berlin",
            "SYD": "Sydney",
            "BKK": "Bankok",
            "SIN": "Singapor",
            "HKG": "Hong Kong"
        }
