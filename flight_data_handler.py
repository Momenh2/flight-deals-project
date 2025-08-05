class FlightData:
    """
    Handles and processes flight data retrieved from the API.
    """
    def __init__(self, data_json):
        """
        Initialize with raw JSON data.

        :param data_json: The full response JSON containing flight offers.
        """
        self.flightsData = data_json["data"]

    def get_minimum_price_flight(self, current_min_price):
        """
        Returns the lowest price from the available flight offers that is lower than the current known minimum.

        :param current_min_price: The price to compare against.
        :return: The lowest price found (or the current price if none are cheaper).
        """

        for i in range(len(self.flightsData)):
            if float(self.flightsData[i]["price"]["total"]) < float(current_min_price):
                current_min_price = self.flightsData[i]["price"]["total"]
        return current_min_price
