import asyncio, logging
import logging
import sys
from aiogram import F
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from config import TOKEN
from mate import mate


dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    Reaction on command '/start'
    """
    await message.answer(f'Hello, this is a Moderator bot, find out more information /about')

@dp.message(Command('about'))
async def command_about_handler(message: Message) -> None:
    """
    Reaction on command '/about'
    """
    await message.answer(f'This moderator bot was created for groups to monitor insults')

@dp.message(CommandStart('help'))
async def command_start_handler(message: Message) -> None:
    """
    Reaction on command '/help'
    """
    await message.answer(f'Any more questions? call or write to @neprostoilya')

@dp.message()
async def reation_on_mate_handler(message: types.Message) -> None:
    """ 
    Reaction on mate in group 
    """
    for word in mate:
        if word in message.text.lower():
            await message.delete()
            await message.answer(
                text='Dont swear'
            )   
async def main() -> None:
    """
    Main 
    """
    print(TOKEN)
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__ == "__main__":
    """
    Start bot
    """
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())