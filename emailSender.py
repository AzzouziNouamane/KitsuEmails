import requests
from bs4 import BeautifulSoup
import smtplib
import time
import sys

def send_email(mediaSlug, mediaURL):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('nouamaneazzouzi19@gmail.com', 'mntudmjngnyfamdj')
    subject = 'new Episode of ' + mediaSlug + ' is OUT !'
    body = 'Check this link for more infos: ' + mediaURL

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'nouamaneazzouzi19@gmail.com',
        'nouamaneazzouzi19@gmail.com',
        msg
    )

    print('HEY EMAIL HAS BEEN SENT')

    server.quit()