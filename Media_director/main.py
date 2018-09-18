# -*- coding: utf-8 -*-
import json
import os
import requests
import telegram
from flask import Flask, request

app = Flask(__name__)

TOKEN = os.getenv('TOKEN')
host = os.getenv('CORE_HOST')
URL = os.getenv('FQDN')
print(TOKEN)
print(host)
print(URL)

bot = telegram.Bot(token=TOKEN)
# bot.delete_webhook()
s = bot.setWebhook('%s/telegram' % URL)
print(s)



@app.route('/', methods=['GET'])
def hello():
    return "<h1 style='color:blue'>Working OK</h1>"


@app.route('/telegram', methods=['POST', 'GET'])
def webhook_handler():
    req = request.get_json(force=True)
    print(req)
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat.id
        text = update.message.text
        userid = update.message.from_user.id
        username = update.message.from_user.username
        print(text)
        if text is None:
            return 'ok'
        response_agent = request_core(text, userid)
        for response in response_agent:
            print(response)
            if response.get("text"):
                bot.send_message(chat_id=chat_id, text=response.get("text"))
            if response.get("image"):
                bot.send_photo(chat_id=chat_id, photo=response.get("image"))
    return 'ok'


def request_core(text, user_id):
    url = 'http://' + host + ':5005/webhooks/rest/webhook'
    headers = {'Content-type': 'application/json',  # Определение типа данных
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8'}
    data = {"message": text, "sender": user_id}
    answer = requests.post(url, data=json.dumps(data), headers=headers)
    print(answer)
    response = answer.json()
    print(response)
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
