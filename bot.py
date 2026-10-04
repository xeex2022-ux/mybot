from flask import Flask
import telebot
import threading
import os

TOKEN = '8352755688:AAF3lIqO5YaHjy6UDCC_bs-WsxSrrW7RuOk'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "هلا والله البوت شغال 24 ساعة 🔥")

@bot.message_handler(func=lambda m: True)
def all_msg(m):
    bot.reply_to(m, f"وصلتني: {m.text}")

@app.route('/')
def home():
    return "Bot is Running 24/7"

def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
