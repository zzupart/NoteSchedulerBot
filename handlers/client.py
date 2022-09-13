from create_bot import dp, bot
from aiogram import Dispatcher, types

async def command_start(msg: types.message):
    await bot.send_message(msg.from_user.id, 'Hi!🖐️ I am Note Scheduler - bot, created to help people make notes📜')

async def command_make_note(msg: types.maessage):
    await bot.send_message(msg.from_user.id, 'Alright, a new note\nSend message to note')
async def send_notification(msg: types.message):
    await bot.send_message(msg.from_user.id, 'Okey, now send a date when you want to return your note')

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(command_start, commands = ['start', 'help'])
