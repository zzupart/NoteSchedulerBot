import aiosqlite

async def service():
    db = await aiosqlite.connect("notes.db")
    cursor = await db.execute("""SELECT * from notes""")
    rows = await cursor.fetchall()

    for row in rows:
        print(row[0])
        print(row[1])
        print(row[2])
    
    