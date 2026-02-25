import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Token code me NA daalo.
# Render me BOT_TOKEN environment variable set karenge.
TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable set nahi hai. Render me jaake add karo.")

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Namaste bhai! 👋\n"
        "Ye tumhara Saved Messages OCR Search Bot ka basic version hai.\n\n"
        "Abhi ke liye:\n"
        "• /start = ye message\n"
        "• Photo ya document bhejo = main confirm karunga.\n\n"
        "Baad me isme OCR (image se text) + search system add karenge. 🔍"
    )


@dp.message(lambda m: m.photo)
async def handle_photo(message: types.Message):
    await message.answer(
        "📸 Photo mil gaya bhai!\n"
        "Next step me is photo se text nikalne (OCR) ka system lagayenge."
    )


@dp.message(lambda m: m.document)
async def handle_document(message: types.Message):
    await message.answer(
        "📄 Document mil gaya bhai!\n"
        "Isme se bhi baad me text nikalenge aur searchable bana denge."
    )


@dp.message()
async def fallback(message: types.Message):
    await message.answer(
        "Filhaal main basic mode me hu.\n"
        "Mujhe /start bhejo, ya koi photo/document bhejo. 🙂"
    )


async def main():
    logging.basicConfig(level=logging.INFO)
    print("🚀 Bot start ho gaya (polling mode)...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
