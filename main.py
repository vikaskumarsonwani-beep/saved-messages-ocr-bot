import os
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Token env se lenge (Render me BOT_TOKEN set kiya hai)
TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable set nahi hai. Render me jaake add karo.")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text(
        "Namaste bhai! 👋\n"
        "Ye tumhara Saved Messages OCR Search Bot ka basic version hai.\n\n"
        "Abhi ke liye:\n"
        "• /start = ye message\n"
        "• Photo ya document bhejo = main confirm karunga.\n\n"
        "Baad me isme OCR (image se text) + search system add karenge. 🔍"
    )


def handle_photo(update, context):
    update.message.reply_text(
        "📸 Photo mil gaya bhai!\n"
        "Next step me is photo se text nikalne (OCR) ka system lagayenge."
    )


def handle_document(update, context):
    update.message.reply_text(
        "📄 Document mil gaya bhai!\n"
        "Isme se bhi baad me text nikalenge aur searchable bana denge."
    )


def fallback(update, context):
    if update.message:
        update.message.reply_text(
            "Filhaal main basic mode me hu.\n"
            "Mujhe /start bhejo, ya koi photo/document bhejo. 🙂"
        )


def main():
    # Updater purane (v13) style ka hai – ye hi stable hai
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.photo, handle_photo))
    dp.add_handler(MessageHandler(Filters.document, handle_document))
    dp.add_handler(MessageHandler(Filters.all, fallback))

    print("🚀 Bot start ho gaya (polling mode)...")
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
