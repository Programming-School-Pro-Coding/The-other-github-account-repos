import requests
import time

#globel variables
api_key = 'aa9904d9-ef6c-423b-8e01-6ce90b5caf8b'
bot_key = '1736646297:AAFN5fmhveUQsVeap2E56GM90qvG9RmXyMk'
chat_id = '1745875954'
limit = 65000
time_interval = 10 * 60

def get_price():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

    parameters = {
        'start':'1',
        'limit':'100'
    }
    
    

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }


    responce = requests.get(url, headers=headers, params=parameters).json()
    btc_price = responce['data'][0]['quote']['USD']['price']
    return btc_price

def send_update(chat_id, msg):
    url = f"https://api.telegram.org/bot{bot_key}/sendMassage?chat_id={chat_id}&text={msg}"
    requests.get(url)

def main():
    while True:
        price = get_price()
        print(price)
        if price < limit:
            send_update(chat_id, f"بقولك ايه يا باشا سعر البيتكوين:{price}")
        time.sleep(5 * 60)

main()

