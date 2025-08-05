# ✈️ Flight Deals Tracker

A Python-based application that monitors real-time flight prices and sends notifications when lower fares are found. The system is designed to help users discover cheaper flight options departing from a specific city — by default, **Sydney, Australia**.

---

## 📌 Project Features

- ✅ Connects to the Sheety API to manage data stored in Google Sheets.
- ✅ Integrates with the Tequila API by Kiwi.com for flight data and searches.
- ✅ Collects user emails via a Google Form and stores them in a separate sheet.
- ✅ Sends:
  - ✉️ Email alerts to subscribed users.
  - 📱 SMS alerts using Twilio when lower flight prices are found.
- ✅ Supports real-time tracking and updates flight data automatically.

---

## 🗂️ Project Structure

FlightDeals/
│
├── flight_Api_search.py # Main execution script (entry point)
├── flight_data_handler.py # Handles filtering and extracting minimum flight info
├── flight_search.py # Handles API calls to Tequila for flight data
├── notification_system_manager.py # Handles sending SMS and emails via Twilio/SMTP
├── sheet_data_manager.py # Communicates with Sheety API (Google Sheets)
├── .env # Stores environment variables (API keys, URLs)
├── requirements.txt # Python dependencies
├── .gitignore # Files and folders to ignore in version control
└── README.md # Project documentation


---

## ⚙️ Tech Stack & APIs Used

- **Python 3.10+**
- **APIs:**
  - [Kiwi Tequila API](https://tequila.kiwi.com/portal/login) — for flight search.
    - ⚠️ Requires an API key and location codes.
    - Note: Limited daily searches depending on the plan.
  - [Sheety API](https://sheety.co/) — to interact with Google Sheets.
  - [Twilio API](https://www.twilio.com/) — for sending SMS.
    - ⚠️ Requires a verified phone number on free accounts.
- **Google Forms + Sheets** — for collecting user data and storing destinations.

---

## 📋 How It Works

1. **User signs up via Google Form** — their data is stored in a Google Sheet.
2. The app reads destination data from a separate tab in the same Sheet.
3. It fetches flight data using the Tequila API.
4. If a cheaper flight is found:
   - The app updates the Sheet.
   - Sends SMS and/or email alerts to all subscribed users.

---

## 📍 Configuration

You must create a `.env` file in your root project directory with the following keys:

```dotenv
FLIGHT_PRICE_URL=your_sheety_prices_endpoint
USERS_URL=your_sheety_users_endpoint
FLIGHT_PRICE_PUT_URL=your_sheety_prices_put_endpoint
TEQUILA_API_KEY=your_tequila_api_key
TWILIO_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
TWILIO_FROM=your_twilio_phone_number
MY_NUMBER=your_verified_phone_number
EMAIL=your_email_address
PASSWORD=your_email_app_password
⚠️ Use an App Password if using Gmail for email notifications https://support.google.com/accounts/answer/185833?hl=en

```

## 🚀 Future Enhancements
✅ Automatically detect and add new destination cities.

✅ Allow users to customize departure location.

⏳ Add support for round trips and multiple date options.

⏳ Build a front-end dashboard for users to manage their subscriptions.


## 🛡️ License
This project is licensed under the MIT License.


## 🙌 Author
Momen H.
GitHub Profile »

