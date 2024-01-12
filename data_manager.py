import requests
import os

SHEETY_PRICES_ENDPOINT = os.environ["SHEETY_PRICES_ENDPOINT"]
SHEETY_USERS_ENDPOINT = os.environ["SHEETY_USER_ENDPOINT"]
BEARER = os.environ["BEARER"]


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        headers = {
            "Authorization": f"Bearer {BEARER}",
            "Content-Type": "application/json",
        }
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            headers = {
                "Authorization": f"Bearer {BEARER}",
                "Content-Type": "application/json",
            }

            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=headers
            )
            print(response.text)

    def get_customer_emails(self):
        headers = {
            "Authorization": f"Bearer {BEARER}",
            "Content-Type": "application/json",
        }

        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=headers)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
