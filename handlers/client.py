from create_bot import dp, bot
from aiogram import Dispatcher, types

async def command_start(msg: types.message):
    await bot.send_message(msg.from_user.id, 'Hi!🖐️ I am Note Scheduler - bot, created to help people make notes📜')

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(command_start, commands = ['start', 'help'])
