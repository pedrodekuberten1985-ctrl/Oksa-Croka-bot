import os
from telegram.ext import Application, CommandHandler

async def start(update, context):
    await update.message.reply_text("Привет! Я бот для Оксаны ❤️")

async def help_command(update, context):
    await update.message.reply_text("Напиши /start — и я отвечу!")

def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise ValueError("❌ Не найден BOT_TOKEN. Добавь его в переменные окружения!")

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("✅ Бот запущен и ожидает сообщения...")
    app.run_polling()

if __name__ == "__main__":
    main()
