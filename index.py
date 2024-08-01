from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('اوم')
    

app = ApplicationBuilder().token("7398078714:AAEM2FrYLu84uQG9ny1alnWk3JoLaEtuXjM").build()

app.add_handler(CommandHandler("start", hello))

app.run_polling()