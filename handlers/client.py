from database import database
from create_bot import dp, bot
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext, State, StatesGroup

class NoteMaker(StateGroup):
    note = State()
    date = State()

async def command_start(msg: types.message):
    await bot.send_message(msg.from_user.id, 'Hi!🖐️ I am Note Scheduler - bot, created to help people make notes📜')

async def command_make_note(msg: types.maessage):
    await bot.send_message(msg.from_user.id, 'Alright, a new note\nSend message to note')
    await NoteMaker.note.set()

async def send_notification(msg: types.message):
    notification = msg.text
    await bot.send_message(msg.from_user.id, 'Okey, now send a date when you want to return your note')
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
    dp.register_message_handler(command_start, commands = ['start', 'help'])
