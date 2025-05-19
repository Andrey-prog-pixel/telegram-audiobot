from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = '7629141481:AAFLbrYAzUJBvjxE0Yonq-TGPfiwf_xNunI'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я аудиотренинг-бот.\nВведите дату, время и место вашего рождения:"
    )

if __name__ == '__main__':
    print("Бот запускается...")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен. Ожидаю сообщения в Telegram...")
    app.run_polling()
