from flask import Flask, jsonify
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackContext, Application
from telegram.ext import filters
import logging
import threading

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define constants
BOT_TOKEN = "7244777025:AAGSZao_l4r9rICiP9YrJrO_RBklWG056Os"
web_link = "https://telegram-bot-enagage.vercel.app"
community_link = "https://t.me/EngageCommunity"

# Initialize the Flask app
app = Flask(__name__)

async def start(update: Update, context: CallbackContext):
    start_payload = context.args[0] if context.args else ""
    url_sent = f"{web_link}?ref={start_payload}"
    user = update.message.from_user
    user_name = f"@{user.username}" if user.username else user.first_name
    keyboard = [
        [InlineKeyboardButton("👋 Start now!", web_app={"url": url_sent})],
        [InlineKeyboardButton("Join our Community", url=community_link)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "*Welcome to Engage Tap Bot, your gateway to earning $ENG tokens while engaging with top Web3 projects!*\n\n"
        "🚀 *Earn $ENG Tokens:* Join the Engage Bot on Telegram, complete social tasks to earn Engage points and receive an airdrop based on your accumulated points.\n\n"
        "⬆️ *Receive Unique Airdrops from Top-Tier Projects:* The higher your level, the more you receive from airdrops of top-tier projects.\n\n"
        "🎮 *Play Games to Earn:* Dive into various games within the bot to earn even more Engage Points.\n\n"
        "💎 *Unlock Advanced Tasks:* Use your ENG points to access more challenging tasks and boost your earnings.\n\n"
        "⚡ *Purchase Boosts:* Enhance your bot’s performance with special boosts available through Engage points.\n\n"
        "🏆 *Access Premium Rewards:* Participate in exclusive reward campaigns and tap into premium reward pools using your Engage points.\n\n"
        "Engage with the bot now and start earning your rewards!",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

# Create the Application and add handlers
application = Application.builder().token(BOT_TOKEN).build()
application.add_handler(CommandHandler("start", start))

@app.route('/')
def index():
    return jsonify({"message": "Flask server is running"})

def run_flask():
    app.run(port=3003)

def run_bot():
    application.run_polling()

if __name__ == '__main__':
    # Run Flask server in a separate thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    # Run Telegram bot
    run_bot()
