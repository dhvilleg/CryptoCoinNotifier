from binance.spot import Spot


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


def extractCryptoValue(cryptoCoin):
    client = Spot(key='YOUR_BINANCE_KEY_ACCESS',
                  secret='YOUR_BINANCE_SECRET_ACCESS')
    data = client.account()
    cryptoValueList = []
    symbol = find_value(data, 'balances')
    for i in symbol:
        if i['asset'] == cryptoCoin:
            cryptoValueList.append(i['asset'])
            cryptoValueList.append(i['free'])
    return cryptoValueList
