import json

from Core.services.technical.RequestService import RequestService


class EstimationService:
    @classmethod
    def estimate(cls, departure_date):
        url = "https://opendata.bordeaux-metropole.fr/api/records/1.0/search/?dataset=ci_courb_a&rows=193"
        response = RequestService.get(url)
        return json.loads(response)
