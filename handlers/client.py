import re
from datetime import datetime, timedelta
from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import bot, dp
from database import database
from keyboards import client_kb

class NoteMaker(StatesGroup):
    note = State()
    date = State()

async def command_start(msg: types.message):
    await bot.send_message(msg.from_user.id, 'Hi!🖐️ I am Note Scheduler - bot, created to help people make notes📜', reply_markup = client_kb.kb_client)

async def command_credits(msg: types.message):
    await bot.send_message(msg.from_user.id, 'Developers of this bot⌨️:\n@osp54\n@zzupart')

async def command_make_note(msg: types.message):
    await bot.send_message(msg.from_user.id, 'Alright, a new note\nSend message to note', reply_markup = ReplyKeyboardRemove())
    await NoteMaker.note.set()

async def send_notification(msg: types.message):
    global notification
    notification = msg.text
    await bot.send_message(msg.from_user.id, 'Okey, now send a time to count when you want to return your note in format x seconds(xs), x minutes(xm), x hours(xh), x days(xd)\nFor example: 25m')
    await NoteMaker.next()

async def send_date(msg: types.message, state: FSMContext):
    date = msg.text
    time_list = re.split('(\d+)', date)
    time_in_s = None
    if time_list[2] == "s":
        time_in_s = int(time_list[1])
    elif time_list[2] == "m":
        time_in_s = int(time_list[1]) * 60
    elif time_list[2] == "h":
        time_in_s = int(time_list[1]) * 60 * 60
    elif time_list[2] == "d":
        time_in_s = int(time_list[1]) * 60 * 60 * 24
    elif date == 0 or date == "0":
        print('Turip ip ip')
    try:
        await database.insert_note(msg.from_user.id, datetime.now() + timedelta(seconds=time_in_s), notification)
    except Exception as e:
        await bot.send_message(msg.from_user.id, 'Error, please make sure you send correct date', reply_markup = client_kb.kb_client)
        print(e)
    else:
        await bot.send_message(msg.from_user.id, 'New notification created sucessfuly', reply_markup = client_kb.kb_client)
    await state.finish()

async def command_my_notes(msg: types.message):
    rows = await database.execute("""SELECT * FROM notes WHERE user_id = ?""", (msg.from_user.id,), select=True, all=True)
    gen = ""
    for row in rows:
        gen += f"{row[2]}: {row[1]}\n"
    if gen == "":
        await bot.send_message(msg.from_user.id, "Not found your notes.")
    else:
        await bot.send_message(msg.from_user.id, gen)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(send_notification, state = NoteMaker.note)
    dp.register_message_handler(send_date, state = NoteMaker.date)
    dp.register_message_handler(command_start, commands = ['start', 'help'])
    dp.register_message_handler(command_make_note, commands = ['make_note📜'])
    dp.register_message_handler(command_my_notes, commands = ['my_notes🔔'])
    dp.register_message_handler(command_credits, commands = ['credits💻'])
