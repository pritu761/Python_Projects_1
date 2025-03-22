import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint

# Load environment variables from .env file
#load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/d9c42cd4fc0b47b96611a3aa6c70cb7d/flightDeals/prices"


class DataManager:

    def __init__(self):
        self._user = "pknath769"
        self._password = "Sachin@2005#"
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        pprint(data)
        return self.destination_data

    # 6. In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)