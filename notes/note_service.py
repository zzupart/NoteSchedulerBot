from datetime import datetime
from database import *
from create_bot import bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

async def start_service():
    scheduler = AsyncIOScheduler() 
    scheduler.add_job(service, "interval", minutes=1)
    scheduler.start()

async def service():
    rows = await execute("""SELECT * FROM notes""", select=True, all=True)

    for row in rows:
        if datetime.now() >= datetime.fromisoformat(row[1]):
            await bot.send_message(row[0], row[2])
            await delete_note(row[0], row[1], row[2])
        else:
            return
