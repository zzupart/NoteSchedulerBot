import os
from typing import Iterable, Any
from aiosqlite import connect

class database:
    async def setup():
        print(os.getcwd())
        db = await connect(os.getcwd() + "\db.db")
        await db.execute("""CREATE TABLE IF NOT EXISTS notes (user_id INT, date DATETIME, message TEXT)""")
        await db.commit()
    async def execute(sql, params: Iterable[Any] = None, select: bool = False, all: bool = False):
        db = await connect("db.db")
        if select:
            cursor = await db.execute(sql, params)
            if all:
                return await cursor.fetchall()
            else:
                return await cursor.fetchone()
        else:
            return await db.execute(sql, params)
    async def insert_note(user_id, date, message):
        db = await connect("db.db")
        await db.execute("""INSERT INTO notes (user_id, date, message) VALUES (?, ?, ?)""", (user_id, date, message))
        await db.commit()
    async def delete_note(user_id, date, message):
        db = await connect("db.db")
        await db.execute("""DELETE FROM notes WHERE user_id = ?, date = ?, message = ?""", (user_id, date, message))
