from config import TELEGRAM_BOT_TOKEN
from telegram.ext import Application, CommandHandler

async def start(update, context):
    await update.message.reply_text("Привет! Я бот Astro Intel. 🔮")

def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
