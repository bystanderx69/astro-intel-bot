from config import TELEGRAM_BOT_TOKEN
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Русский 🇷🇺", callback_data="lang_ru")],
        [InlineKeyboardButton("English 🇬🇧", callback_data="lang_en")],
        [InlineKeyboardButton("Español 🇪🇸", callback_data="lang_es")],
        [InlineKeyboardButton("Deutsch 🇩🇪", callback_data="lang_de")],
        [InlineKeyboardButton("Français 🇫🇷", callback_data="lang_fr")],
        [InlineKeyboardButton("العربية 🇸🇦", callback_data="lang_ar")]
    ]
    await update.message.reply_text(
        "🌐 Please choose your language:\n🌐 Пожалуйста, выберите язык:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def language_selected(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    lang_code = query.data.split("_")[1]
    context.user_data["lang"] = lang_code

    greetings = {
        "ru": "Привет! Я бот Astro Intel. ✨",
        "en": "Hi! I’m Astro Intel bot. ✨",
        "es": "¡Hola! Soy el bot Astro Intel. ✨",
        "de": "Hallo! Ich bin der Astro Intel Bot. ✨",
        "fr": "Salut ! Je suis le bot Astro Intel. ✨",
        "ar": "مرحباً! أنا روبوت Astro Intel. ✨"
    }

    await query.edit_message_text(text=greetings.get(lang_code, "Language set."))

def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(language_selected, pattern="^lang_"))
    app.run_polling()

if __name__ == "__main__":
    main()
