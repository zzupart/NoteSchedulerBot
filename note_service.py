from datetime import datetime
import aiosqlite

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