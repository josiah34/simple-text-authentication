from twilio.rest import Client
import twilio

import random

# Constants
ACCOUNT_SID = ""  # Your Twilio account SID
AUTH_TOKEN = ""  # Your Twilio account auth token


def send_verification_code(phone_number):
    """Function to create verification code and send it via Twilio client to the recipient phone number"""
    verification_code = str(random.randint(1000, 9999))
    try:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages.create(
            body=f"Your verfication code is: {verification_code} 😃",
            from_="",  # Your Twilio phone number
            to=phone_number,
        )
    except twilio.base.exceptions.TwilioException as e:
        print(f"Error initializing Twilio client:\n{e}")
    except:
        print("Error sending verification code")

    print(f"Verification code sent to {phone_number}!")
    return verification_code


def verify_code(verification_code, entered_code):
    """Function to verify the code entered by the user"""
    if verification_code == entered_code:
        return "You are verified!!"
    else:
        return "Wrong verification code"


if __name__ == "__main__":
    print("Welcome to the Twilio verification app!")
    phone_number = input("Enter your phone number: ")
    verification_code = send_verification_code(phone_number)
    entered_code = input("Enter the verification code: ")
    message = verify_code(verification_code, entered_code)
    print(message)
