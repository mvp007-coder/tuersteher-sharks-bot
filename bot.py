import logging
import os

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

logging.basicConfig(level=logging.INFO)

TOKEN = os.environ["BOT_TOKEN"]
GROUP_ID = -1004388254877
ALLGEMEIN_THREAD = 10
BEFEHL_NAME = "bannisko"
BEFEHL_EMOJI = "🦈🍆"


async def befehl(update: Update, context: ContextTypes.DEFAULT_TYPE):
    m = update.message
    if not m or not m.text:
        return
    erstes = m.text.split()[0].lstrip("/").split("@")[0].lower()
    if erstes != BEFEHL_NAME:
        return
    thread = m.message_thread_id if m.is_topic_message else None
    if thread not in (None, ALLGEMEIN_THREAD):
        return
    await m.reply_text(BEFEHL_EMOJI)


def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.Chat(GROUP_ID) & filters.COMMAND, befehl))
    app.run_polling(allowed_updates=["message"])


if __name__ == "__main__":
    main()
