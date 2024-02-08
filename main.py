import asyncio
import logging
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from dotenv import load_dotenv

import handlers


load_dotenv()
TOKEN = getenv("BOT_TOKEN")


async def main() -> None:
    dp = Dispatcher()
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

    dp.include_router(handlers.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        # filename=os.path.join(os.path.dirname(__file__), "PR.log"),
        # filemode="a",
        encoding='utf-8',
        format="%(asctime)s : %(levelname)s : %(message)s"
    )

    logging.info("START")
    asyncio.run(main())
