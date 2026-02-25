import os
import logging

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# Token env se lenge (Render me BOT_TOKEN set kiya hai)
TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable set nahi hai. Render me jaake add karo.")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Namaste bhai! 👋\n"
        "Ye tumhara Saved Messages OCR Search Bot ka basic version hai.\n\n"
        "Abhi ke liye:\n"
        "• /start = ye message\n"
        "• Photo ya document bhejo = main confirm karunga.\n\n"
        "Baad me isme OCR (image se text) + search system add karenge. 🔍"
    )


async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📸 Photo mil gaya bhai!\n"
        "Next step me is photo se text nikalne (OCR) ka system lagayenge."
    )


async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📄 Document mil gaya bhai!\n"
        "Isme se bhi baad me text nikalenge aur searchable bana denge."
    )


async def fallback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Kuch bhi aur message aaya to
    if update.message:
        await update.message.reply_text(
            "Filhaal main basic mode me hu.\n"
            "Mujhe /start bhejo, ya koi photo/document bhejo. 🙂"
        )


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.add_handler(MessageHandler(filters.Document.ALL, handle_document))
    app.add_handler(MessageHandler(filters.ALL, fallback))

    print("🚀 Bot start ho gaya (polling mode)...")
    app.run_polling()


if __name__ == "__main__":
    main()
