from datetime import datetime
from database import database
from bot import dp


async def service():
    rows = await database.execute("""SELECT * FROM notes""", select=True, all=True)

    for row in rows:
        now = datetime.now()
        note_date = row[1]
        if now >= note_date:
            pass # отправляем челику
        else:
            return