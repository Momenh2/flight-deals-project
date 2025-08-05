"""
This script integrates all components of the flight deal tracker:
- Fetches current prices from Google Sheets via Sheety
- Searches for better flight deals using an API
- Updates Google Sheet with improved deals
- Notifies users via SMS and email
"""

from sheet_data_manager import DataManager

from flight_data_handler import FlightData

from flight_Api_search import FlightSearch

from notification_system_manager import NotificationManager

SheetData = DataManager()

for i in range(2, 6): # You need to adjust it based on how many flights are your program tracking in your spreadsheet
    if i == 5:
        break
    IataCode = SheetData.get_iata_code_of_row(i)
    currentRowPrice = float(SheetData.get_specific_row_price(IataCode))

    Search = FlightSearch(IataCode)

    data = Search.search()
    print("after data = ")

    Fdata = FlightData(data)

    RealMinPrice = Fdata.get_minimum_price_flight(currentRowPrice)

    if float(RealMinPrice) < float(currentRowPrice):
        SheetData.update_price(IataCode, RealMinPrice)
        emails = SheetData.get_customer_emails()
        Notification = NotificationManager("SYD",f"{IataCode}",float(RealMinPrice))
        Notification.send_sms()
        Notification.send_emails(emails,f"from SYD TO {IataCode}")
