from random import choices
import os
import requests
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def get_mars_photos(sol, count=3, api_key='NASA_API_KEY'):
    rover_url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
    params = {'sol': sol, 'api_key': api_key}
    response = requests.get(rover_url, params=params).json()
    photos = response['photos']

    return choices(photos, k=count)

def send_mars_email(api_key, from_email, to_email, img_urls):
    sg = SendGridAPIClient(api_key)

    message = Mail(
        from_email=from_email,
        to_emails=to_email,
        subject='Here are your Mars Rover pictures',
        html_content='<strong>Check out these Mars pics</strong><br>' +
                     ''.join([f'<img src="{img_url}"></img>' for img_url in img_urls]))

    response = sg.send(message)
    print(response.status_code, response.body, response.headers)

if __name__ == '__main__':
    sendgrid_api_key = 'YOUR_SENDGRID_API'
    from_email = 'SENDER_MAIL'
    to_email = 'RECEIVER_MAIL'
    sol = 1000
    photo_count = 10


    photo_urls = [photo['img_src'] for photo in get_mars_photos(sol, count=photo_count)]

    
    send_mars_email(sendgrid_api_key, from_email, to_email, photo_urls)
