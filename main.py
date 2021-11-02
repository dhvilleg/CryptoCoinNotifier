from extractDataFromCoinMarket import extractCryptoPrice
from extractDataFromBinance import extractCryptoValue
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
        flagValue = int(conf_list[3])
        datetime_object = datetime.datetime.now()
        cryptoInfo = extractCryptoPrice(criptoCoin)

        aux = str(cryptoInfo[1])
        cryptoValue = float(aux.replace(',', ''))

        log_file.write("El precio del: {} al {} es de: {}\n".format(criptoCoin, datetime_object, cryptoValue))

        if flagValue == 1:
            cryptoUSD_value = extractCryptoValue(criptoCoin)
            usdCryptoValue = float(cryptoInfo[1]) * float(cryptoUSD_value[1])
            message = telegram_bot_sendtext("El valor de mi inversion en {} en dolares es de: {}".format(cryptoInfo[0], usdCryptoValue))
            log_file.write(str(message))
            log_file.write("\n")

        if cryptoValue <= minValue:
            message = telegram_bot_sendtext("El precio del: {} esta a la baja con valor {}".format(cryptoInfo[0], cryptoInfo[1]))
            log_file.write(str(message))
            log_file.write("\n")

        if cryptoValue > maxValue:
            message = telegram_bot_sendtext("El precio del: {} esta al alza con valor {}".format(cryptoInfo[0], cryptoInfo[1]))
            log_file.write(str(message))
            log_file.write("\n")

        flagValue = ""

    log_file.close()


