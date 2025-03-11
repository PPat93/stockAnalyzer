""" 
Mailer component:
Receives data from Integrator: -> Analyzer, -> Database;
Creates email and it's content;
Sends email;
"""

import smtplib
import ssl
import os
from email.message import EmailMessage

PORT = 465
sender_email = os.environ.get("predictorMailerAddress")
sender_pass = os.environ.get("predictorAppPass")
notifyee_email = os.environ.get("notifyeeMailerAddress")


class Mailer:
    """Class for stock notification sending"""

    def __init__(self, ticker: str) -> None:
        self.ticker = ticker

    def compose_email(self, content):
        """Create a message that will be send"""
        composed_message = EmailMessage()

        composed_message["Subject"] = f"Change on {self.ticker}"
        composed_message["From"] = sender_email
        composed_message["To"] = notifyee_email
        composed_message.set_content(
            f"Hi! \nI found an interesting change on {self.ticker}.\n{content}"
        )
        return composed_message

    def send_email(self, message):
        """Send notification email with the specified message"""
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", PORT, context=context) as server:
            server.login(sender_email, sender_pass)
            server.send_message(message)