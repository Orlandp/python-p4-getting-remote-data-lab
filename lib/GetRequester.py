import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        """
        Sends a GET request to the URL provided during initialization
        and returns the raw response body as text.
        """
        response = requests.get(self.url)
        response.raise_for_status()  # raise exception if status code is 4xx/5xx
        return response.text


    def load_json(self):
         """
        Sends a GET request, retrieves the response body,
        and parses it into a Python object (list or dict).
        """
         response_body = self.get_response_body()
         return json.loads(response_body)