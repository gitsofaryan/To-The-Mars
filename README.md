## To-The-Mars

Python Script to Send a Random Mars Rover Image via Email Using SendGrid and Twilio

This Python script will retrieve a random image from NASA's Mars Rover Photos API and send it as an email attachment to a specified recipient using SendGrid and Twilio.

Dependencies

Python 3
Requests library
SendGrid Python library
Twilio Python library
Instructions

Install the required dependencies:
pip install requests
pip install sendgrid
pip install twilio
Create a file called mars.py and enter the following code:
Python
import requests
from sendgrid import SendGridAPIClient
from twilio.rest import Client

# API key for NASA's Mars Rover Photos API
API_KEY = "YOUR_API_KEY"

# SendGrid API key
SENDGRID_API_KEY = "YOUR_SENDGRID_API_KEY"

# Twilio account SID and auth token
ACCOUNT_SID = "YOUR_ACCOUNT_SID"
AUTH_TOKEN = "YOUR_AUTH_TOKEN"

# Email address of the recipient
RECIPIENT_EMAIL = "RECIPIENT_EMAIL"

def get_mars_photo_url():
    # Retrieve the latest image from the Mars Rover Photos API
    url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
    params = {
        "sol": "random",
        "api_key": API_KEY
    }
    response = requests.get(url, params)
    response_dictionary = response.json()

    # Return the URL of the image
    return response_dictionary["photos"][0]["img_src"]

def send_email(photo_url):
    # Create a SendGrid client
    sg = SendGridAPIClient(SENDGRID_API_KEY)

    # Create an email object
    email = sg.Mail()
    email.set_from("YOUR_SENDER_EMAIL")
    email.set_to(RECIPIENT_EMAIL)
    email.set_subject("Random Mars Rover Image")
    email.set_body("Here is a random image from Mars!")

    # Add the image attachment
    with open(photo_url, "rb") as f:
        attachment = sg.Attachment()
        attachment.set_content(f.read())
        attachment.set_type("image/jpeg")
        attachment.set_filename("mars.jpg")
        email.add_attachment(attachment)

    # Send the email
    sg.send(email)

if __name__ == "__main__":
    # Get the URL of the random Mars Rover image
    photo_url = get_mars_photo_url()

    # Send the email with the image attachment
    send_email(photo_url)
Use code with caution. Learn more
Replace the YOUR_API_KEY, YOUR_SENDGRID_API_KEY, YOUR_ACCOUNT_SID, YOUR_AUTH_TOKEN, and RECIPIENT_EMAIL variables with your own values.

Save the file and run it:

python mars.py
This will send an email to the specified recipient with a random image from NASA's Mars Rover Photos API.

Modifications to Send a Random Image

To modify the script to send a random image, you can make the following changes:

In the get_mars_photo_url() function, change the sol parameter to random.
In the send_email() function, change the body variable to something like the following:
Here is a random image from Mars!

[Image of Mars]
This will replace the body of the email with the following:

Here is a random image from Mars!

[Image of Mars]
The 
Image of MarsOpens in a new window
science.nasa.gov
 placeholder will be replaced with the URL of the random Mars Rover image.

Additional Modifications

You can also modify the script to add additional functionality, such as:

Sending the email at a specific time or date.
Sending the email to multiple recipients.
Including additional information in the email, such as the date and time the image was taken.
