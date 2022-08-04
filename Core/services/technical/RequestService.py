import requests


class RequestService:

    @classmethod
    def get(cls, url, **kwargs):
        response = requests.get(url, **kwargs)
        return response
