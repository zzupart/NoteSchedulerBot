from datetime import datetime
import aiosqlite
from apscheduler.schedulers.asyncio import AsyncIOScheduler

async def start_db():
    scheduler = AsyncIOScheduler() 
    scheduler.add_job(service, "interval", minutes=1)
    scheduler.start()

async def connect():
    db = await aiosqlite.connect("notes.db")
    await db.execute("""CREATE TABLE IF NOT EXISTS notes (user_id INT, date DATETIME, message TEXT)""")
    await db.commit()
    print('Bot connected to database')

async def service():
    db = await aiosqlite.connect("notes.db")
    cursor = await db.execute("""SELECT * from notes""")
    rows = await cursor.fetchall()

    for row in rows:
        now = datetime.now()
        note_date = row[1]
        if now >= note_date:
            pass # отправляем челику
        else:
            return
