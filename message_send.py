import requests


def telegram_bot_sendtext(bot_message):
    bot_token = 'YOUR:TELEGRAM_API_TOKEN'
    bot_chatID = 'YOUR_CHAT_ID_OR_GROUP_ID'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

