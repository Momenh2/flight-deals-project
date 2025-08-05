import requests
from dateutil.relativedelta import relativedelta
import datetime as dt
from dotenv import load_dotenv
import os


class FlightSearch:
    """
    Handles communication with the Amadeus Flight Offers API to search for flights.
    """

    def __init__(self, destination_code):
        """
        Initialize the search parameters and authentication.

        :param destination_code: IATA code of the destination city.
        """
        load_dotenv()
        now = dt.datetime.now()
        # Date after 6 months
        six_months_later = now + relativedelta(months=6)
        self.base_url = os.getenv('FLIGHT_SEARCH_BASE_URL')
        self.origin_location_code = "SYD"
        self.destinationLocationCode = destination_code
        self.departure_date = six_months_later.strftime("%Y-%m-%d")
        self.adults = 1

        self.params = {
            "originLocationCode": self.origin_location_code,
            "destinationLocationCode": self.destinationLocationCode,
            "departureDate": self.departure_date,
            "adults": self.adults,
        }
        auth_token = self.refresh_token()

        self.head = {
            "Authorization": F"Bearer {auth_token}"
        }

    def refresh_token(self):
        """
        Requests a new access token from Amadeus API using client credentials.
        :return: The access token as a string.
        """
        load_dotenv()
        token_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "client_credentials",
            "client_id": os.getenv('API_KEY'),
            "client_secret": os.getenv('API_SECRET')
        }

        try:
            response = requests.post(token_url, headers=headers, data=data)
            response.raise_for_status()
            access_token = response.json().get("access_token")
            if not access_token:
                raise ValueError("Access token not found in response.")
            return access_token
        except requests.RequestException as e:
            print(f"[ERROR] Failed to fetch access token: {e}")
            raise

    def search(self):
        """
        Sends a GET request to the flight search API with specified parameters.

        :return: JSON response from the API containing flight data.
        :raises: requests.HTTPError if the request fails.
        """
        res = requests.get(url=self.base_url, params=self.params, headers=self.head)
        res.raise_for_status()
        return res.json()
