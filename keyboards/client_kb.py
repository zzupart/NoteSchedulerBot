from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
    
b1 = KeyboardButton('/make_note📜')
b2 = KeyboardButton('/my_notes🔔')
b3 = KeyboardButton('/credits💻')

kb_client = ReplyKeyboardMarkup(resize_keyboard = True)

kb_client.row(b1, b2).row(b3)
