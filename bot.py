from create_bot import dp
from aiogram.utils import executor
from handlers import client, admin, other
from notes import note_service

async def on_startup(_):
    await note_service.start_db()
    await note_service.connect()
    print('Bot succesfuly started')

client.register_handlers(dp)
admin.register_handlers(dp)
other.register_handlers(dp)

executor.start_polling(dp, on_startup = on_startup)
