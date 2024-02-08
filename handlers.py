from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message


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
        text=f'||{message.text}||',
        parse_mode='markdownv2'
    )
