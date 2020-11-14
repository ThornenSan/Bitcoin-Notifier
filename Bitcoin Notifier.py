import smtplib
import time
from datetime import datetime


from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json



gmail_user = 'input_gmail'
gmail_password = 'input_passworld'
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '5000',
    'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '6f9fa77a-0b77-4ede-8b94-5d49daa6578a',
}


def Info():
    session = Session()
    session.headers.update(headers)
    price = 0

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        price = round(float(data["data"][0]["quote"]["USD"]["price"]), 2)
        send_email(price)
        print(price)

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


def send_email(price):
    now = datetime.now()
    sent_from = gmail_user
    to = ['target_gamail']
    subject = 'NODix project testing'
    body = """
           This is the current price of Bitcoin!
           date: %s
           price: %
           Do you want to buy or sell?
           """ % (now.strftime('%d.%m.%Y %H:%M'), price)
    email_text = """\
           from: %s
           To: %s
           Subject: %s

           %s
           """ % (sent_from, ", ".join(to), subject, body)
    try:

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
        print('Message Sent!')

    except:
        print('something went wrong')


print("Please Input Every Seconds you want to receive the Info of Bitcoin: ")
try:
    period = int(input())
    while period:
        Info()
        time.sleep(period)
        print(period)
except:
    print('Please input integer')


