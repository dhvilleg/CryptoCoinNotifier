from extractDataFromCoinMarket import extractCryptoPrice
from message_send import telegram_bot_sendtext
import datetime

if __name__ == '__main__':
    conf_file = open("cryptoNotify.conf")
    conf_list = []
    log_file = open("CryptoNotify.log", "a")  # append mode
    for i in conf_file:
        conf_list = i.split(':')
        criptoCoin = conf_list[0]
        minValue = float(conf_list[1])
        maxValue = float(conf_list[2])
        datetime_object = datetime.datetime.now()
        cryptoInfo = extractCryptoPrice(criptoCoin)
        aux = str(cryptoInfo[1])

        cryptoValue = float(aux.replace(',', ''))
        log_file.write("El precio del: {} al {} es de: {}\n".format(criptoCoin, datetime_object, cryptoValue))
        if cryptoValue <= minValue:
            message = telegram_bot_sendtext("El precio del: {} esta a la baja con valor {}".format(cryptoInfo[0], cryptoInfo[1]))
            log_file.write(str(message))
            log_file.write("\n")

        if cryptoValue > maxValue:
            message = telegram_bot_sendtext("El precio del: {} esta al alza con valor {}".format(cryptoInfo[0], cryptoInfo[1]))
            log_file.write(str(message))
            log_file.write("\n")

    log_file.close()





