from datetime import datetime
from database import database
from apscheduler.schedulers.asyncio import AsyncIOScheduler

async def start_service():
    scheduler = AsyncIOScheduler() 
    scheduler.add_job(service, "interval", minutes=1)
    scheduler.start()

<<<<<<< HEAD
async def connect():
    db = await aiosqlite.connect("notes.db")
    await db.execute("""CREATE TABLE IF NOT EXISTS notes (user_id INT, date DATETIME, message TEXT)""")
    await db.commit()
    print('Bot connected to database')

=======
>>>>>>> 4d2b497f17322f710d8d79651c02ace77f52f96b
async def service():
    rows = await database.execute("""SELECT * FROM notes""", select=True, all=True)

    for row in rows:
        now = datetime.now()
        note_date = row[1]
        if now >= note_date:
            pass # отправляем челику
        else:
            return
