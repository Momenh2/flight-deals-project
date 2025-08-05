import requests
from dotenv import load_dotenv
import os



class DataManager:
    """
    Handles reading and updating flight price and user data from Sheety API.
    """

    def __init__(self):
        load_dotenv()
        self.response = requests.get(url=os.getenv('FLIGHT_PRICE_URL'))
        self.response.raise_for_status()
        self.res = self.response.json()

        self.response2 = requests.get(url=os.getenv('USERS_URL'))
        self.response2.raise_for_status()
        self.res2 = self.response2.json()
        self.postUrl = os.getenv('FLIGHT_PRICE_PUT_URL')

    def get_customer_emails(self):
        """
        Retrieve a list of email addresses from the user data.

        Returns:
            list: A list of email addresses (strings) from the Sheety user API.
        """
        arr = [item["whatIsYourEmail?"] for item in self.res2["users"]]
        return arr

    def get_iata_code_of_row(self, id):
        """
        Get the IATA airport code for a given row ID in the prices sheet.

        Args:
            id (int): The ID of the row in the Google Sheet.

        Returns:
            str: The IATA airport code corresponding to the given row ID.
        """
        for item in self.res["prices"]:
            if item["id"] == id:
                return item["iataCode"]

    def get_specific_row_price(self, iataCode):
        """
        Get the lowest recorded flight price for a given destination IATA code.

        Args:
            iataCode (str): The IATA airport code to look up.

        Returns:
            float: The stored lowest price for the destination.
        """
        for item in self.res["prices"]:
            if item["iataCode"] == iataCode:
                return item["lowestPrice"]

    def update_price(self, iataCode, newprice):
        """
        Update the lowest price for a given destination in the Google Sheet.

        Args:
            iataCode (str): The IATA airport code of the destination to update.
            newprice (float): The new, lower price to be saved.

        Side Effects:
            Sends a PUT request to the Sheety API to update the row.
            Prints a success message if the update is successful.
        """
        the_id = None
        city = None
        found = False

        for item in self.res["prices"]:
            if item["iataCode"] == iataCode:
                the_id = item["id"]
                city = item["city"]
                found = True
                break
        if found:
            body = {
                "price": {
                    "city": city,
                    "iataCode": iataCode,
                    "lowestPrice": newprice
                }
            }
            put = requests.put(url=f"{self.postUrl}/{the_id}", json=body)
            put.raise_for_status()
            print("updated successfully")
