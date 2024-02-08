from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """ Команда /start """
    await message.answer(
        text=f"Hello, {message.from_user.full_name}"
    )


@router.message()
async def echo_message(message: Message) -> None:
    await message.answer(
        text=f'{hbold(message.text)}' + '\n\nУмница, теперь иди домой!',
    )
