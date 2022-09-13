from typing import Iterable, Any
from aiosqlite import connect, Cursor, Row
from aiosqlite.context import Result

class database:
    async def setup():
        db = await connect("notes.db")
        await db.execute("""CREATE TABLE IF NOT EXISTS notes (user_id INT, date DATETIME, message TEXT)""")
        await db.commit()
    async def execute(sql, params: Iterable[Any] = None, select: bool = False, all: bool = False
        ) -> Result[Cursor] | Result[Iterable[Row]]:
        db = await connect("notes.db")
        if select:
            cursor = await db.execute(sql, params)
            if all:
                return await cursor.fetchall()
            else:
                return await cursor.fetchone()
        else:
            return await db.execute(sql, params)