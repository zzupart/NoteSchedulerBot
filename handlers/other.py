from create_bot import bot, dp
from aiogram import Dispatcher, types

async def unexpected_message(msg: types.message):
    await msg.reply('I dont understand clear English😯\nPlease send me a command')

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(unexpected_message)
