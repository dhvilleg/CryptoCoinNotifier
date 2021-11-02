from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'


def find_value(data, key):
    if not isinstance(data, dict):
        return None

    try:
        return data[key]
    except KeyError:
        for sub_data in data.values():
            sub_value = find_value(sub_data, key)
            if sub_value is not None:
                return sub_value

    return None


def extractCryptoPrice(criptoCoin):
    cryptoExtracted = []
    parameters = {
        'symbol': criptoCoin
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'YOUR_COINBASE_API_KEY',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        symbol = find_value(data, 'symbol')
        price = find_value(data, 'price')
        cryptoExtracted.append(symbol)
        cryptoExtracted.append(price)
        return cryptoExtracted

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        cryptoExtracted.append(e)
        return cryptoExtracted
