from dotenv import load_dotenv
import os
from twilio.rest import Client
import smtplib


class NotificationManager:
    """
    Sends flight deal notifications via SMS (Twilio) and Email (SMTP).
    """

    def __init__(self, origin, to, price):
        load_dotenv()
        self.fromm = origin
        self.to = to
        self.price = price
        self.account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        self.auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        self.client = Client(self.account_sid, self.auth_token)
        self.to_num = os.getenv('TO_NUM')
        self.from_num = os.getenv('FROM_NUM')

        self.my_email = os.getenv('MY_EMAIL')
        self.password = os.getenv('MAIL_PASSWORD')

    def send_sms(self):
        """
        Sends an SMS with flight deal info using Twilio.
        """
        message = self.client.messages.create(
            body=f"Only {self.price} from {self.fromm} to {self.to}",
            to=f"{self.to_num}",
            from_=f"{self.from_num}"
        )

    def send_emails(self, recipients, content):
        """
        Sends an email to a list of recipients with the flight deal content.

        :param recipients: List of email addresses
        :param content: Email body content
        """

        for item in recipients:
            try:
                with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                    connection.starttls()  # transport layer secuirty
                    connection.login(user=self.my_email, password=self.password)
                    connection.sendmail(from_addr=self.my_email, to_addrs=item,
                                        msg=f"Subject:Flight Offer Deal \n\n {content}")
                    print(f"[Email Sent] To: {item}")
            except Exception as e:
                print(f"[Email Error] Could not send to {item}: {e}")
