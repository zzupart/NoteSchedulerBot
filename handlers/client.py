from database import database
from create_bot import dp, bot
from aiogram import types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

class NoteMaker(StatesGroup):
    note = State()
    date = State()

async def command_start(msg: types.message):
    await bot.send_message(msg.from_user.id, 'Hi!🖐️ I am Note Scheduler - bot, created to help people make notes📜')

async def command_make_note(msg: types.message):
    await bot.send_message(msg.from_user.id, 'Alright, a new note\nSend message to note')
    await NoteMaker.note.set()

async def send_notification(msg: types.message):
    notification = msg.text
    await bot.send_message(msg.from_user.id, 'Okey, now send a time to count when you want to return your note in format x seconds(xs), x minutes(xm), x hours(xh), x days(xd)\nFor example: 25m')
    await NoteMaker.next()

async def send_date(msg: types.message):
    date = msg.text
    try:
        await insert_note(msg.from_user.id, date, notification)
    except:
        await bot.send_message(msg.from_user.id, 'Error, please make sure you send correct date')
    else:
        await bot.send_message(msg.from_user.id, 'New notification created sucessfuly')

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(send_notification, state = NoteMaker.note)
    dp.register_message_handler(send_date, state = NoteMaker.date)
    dp.register_message_handler(command_start, commands = ['start', 'help'])
    dp.register_message_handler(command_make_note, commands = ['make_note'])
