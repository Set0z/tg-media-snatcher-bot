import os
import io
import logging
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.types import Update, BufferedInputFile
from aiogram.dispatcher.middlewares.base import BaseMiddleware

load_dotenv()
TOKEN = os.getenv("TOKEN")
OWNER = int(os.getenv("OWNER"))

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    handlers=[
        logging.FileHandler("logs.txt", encoding="utf-8"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)
logging.getLogger("aiogram").setLevel(logging.WARNING)

bot = Bot(token=TOKEN)
dp = Dispatcher()

class CatchAllMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        if isinstance(event, Update):
            msg = event.business_message
            if msg and msg.reply_to_message:
                reply = msg.reply_to_message
                file_id = None
                media_type = None


                if reply.photo:
                    if not reply.has_protected_content:
                        return await handler(event, data)
                    if reply.from_user and reply.from_user.id == OWNER:
                        return await handler(event, data)
                    file_id = max(reply.photo, key=lambda p: p.file_size).file_id
                    media_type = "photo"
                elif reply.video:
                    if not reply.has_protected_content:
                        return await handler(event, data)
                    if reply.from_user and reply.from_user.id == OWNER:
                        return await handler(event, data)
                    file_id = reply.video.file_id
                    media_type = "video"

                if not file_id:
                    return await handler(event, data)

                logger.info(f"Found {media_type} from {msg.chat.first_name}")

                try:
                    logger.info("Downloading to memory...")
                    buffer = io.BytesIO()
                    await bot.download(file_id, destination=buffer)
                    buffer.seek(0)
                    logger.info("Downloaded!")

                    caption = f'{"Фото" if media_type == "photo" else "Видео"} из чата <a href="tg://openmessage?user_id={msg.chat.id}">{msg.chat.first_name}</a>'

                    logger.info("Sending...!")
                    if media_type == "photo":
                        file = BufferedInputFile(buffer.read(), filename="photo.jpg")
                        await bot.send_photo(OWNER, file, caption=caption, parse_mode="HTML")
                    elif media_type == "video":
                        file = BufferedInputFile(buffer.read(), filename="video.mp4")
                        await bot.send_video(OWNER, file, caption=caption, parse_mode="HTML")

                    logger.info("Sent!")
                except Exception as e:
                    logger.error(f"Error: {e}")

        return await handler(event, data)

dp.update.middleware(CatchAllMiddleware())

async def main():
    logger.info("Bot started...")
    await bot.delete_webhook()
    await dp.start_polling(
        bot,
        allowed_updates=[
            'business_message',
            'edited_business_message',
            'deleted_business_messages',
            'business_connection'
        ]
    )

asyncio.run(main())