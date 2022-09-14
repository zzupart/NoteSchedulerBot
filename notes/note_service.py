from datetime import datetime
from database import database
from create_bot import bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

async def start_service():
    scheduler = AsyncIOScheduler() 
    scheduler.add_job(service, "interval", minutes=1)
    scheduler.start()

async def service():
    rows = await database.execute("""SELECT * FROM notes""", select=True, all=True)

    for row in rows:
        now = datetime.now()
        note_date = row[1]
        if now >= note_date:
            await bot.send_message(row[0], row[2])
        else:
            return
