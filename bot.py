from create_bot import dp
from aiogram.utils import executor
from handlers import client, admin, other
<<<<<<< HEAD
from note_service import service
from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()
scheduler.add_job(service, "interval", seconds=30)
scheduler.start()
=======
from notes import note_service
>>>>>>> refs/remotes/origin/master

async def on_startup(_):
    await note_service.start_db()
    await note_service.connect()
    print('Bot succesfuly started')

client.register_handlers(dp)
admin.register_handlers(dp)
other.register_handlers(dp)

executor.start_polling(dp, on_startup = on_startup)
