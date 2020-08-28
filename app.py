from flask import Flask, request, jsonify
from flask_sslify import SSLify
import json
from bot import Bot
from config import Config
from handler import handle

app = Flask(__name__)
sslify = SSLify(app)
cfg = Config()

bot = Bot(cfg.TOKEN)
webhook = bot.set_webhook(cfg.HOST)
if not webhook['ok']:
    print(f"Description --> {webhook['description']}")
    raise 'Webhook Error'


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        response = request.get_json()
        handle(response, bot, cfg)
        #write_json(response)
        return jsonify(response)
    return '<h1>Wellcome</h1>'
    


if __name__ == '__main__':
    app.run(port=5001)
