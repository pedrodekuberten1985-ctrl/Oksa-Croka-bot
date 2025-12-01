import os
from telegram.ext import Application, CommandHandler

async def start(update, context):
    await update.message.reply_text("Привет! Я OksaCroka_bot ❤️")

async def help_command(update, context):
    await update.message.reply_text("Я всегда рядом для тебя!")

def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise RuntimeError("❌ BOT_TOKEN не найден! Убедись, что он добавлен в переменные окружения.")

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("✅ Бот запущен и работает на Render!")
    app.run_polling()

if __name__ == "__main__":
    main()
