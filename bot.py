from create_bot import dp
from aiogram.utils import executor
from handlers import client, admin, other
from note_service import service
from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()
scheduler.add_job(service, "interval", minutes=1)
scheduler.start()

async def on_startup(_):
    print('Bot succesfuly started')

client.register_handlers(dp)
admin.register_handlers(dp)
other.register_handlers(dp)

executor.start_polling(dp, on_startup = on_startup)
