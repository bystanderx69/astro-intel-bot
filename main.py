from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from config import TELEGRAM_BOT_TOKEN

# Словарь приветствий
GREETINGS = {
    "ru": "Привет! Добро пожаловать в Astro Intelligence 🪐\n\nЭтот бот создаёт персональные гороскопы и рекомендации по нумерологии. Начнём?",
    "en": "Hello! Welcome to Astro Intelligence 🪐\n\nThis bot gives you personalized horoscopes and numerology tips every day. Shall we begin?"
}

# Команда /start — выбор языка
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru"),
         InlineKeyboardButton("🇬🇧 English", callback_data="lang_en")],
        [InlineKeyboardButton("🇪🇸 Español", callback_data="lang_es"),
         InlineKeyboardButton("🇫🇷 Français", callback_data="lang_fr")],
        [InlineKeyboardButton("🇩🇪 Deutsch", callback_data="lang_de")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("🌐 Please select your language / Пожалуйста, выберите язык:", reply_markup=reply_markup)

# Обработка выбора языка
async def language_selected(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang_code = query.data.split("_")[1]
    greeting = GREETINGS.get(lang_code, GREETINGS["en"])
    await query.edit_message_text(text=greeting)

# Запуск
def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(language_selected, pattern="^lang_"))
    app.run_polling()

if __name__ == "__main__":
    main()
