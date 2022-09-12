from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import config as cfg

async def on_startup(_):
    print('Bot succesfuly started')

bot = Bot(cfg.TgTOKEN)
dp = Dispatcher(bot)


executor.start_polling(dp, on_startup = on_startup)
