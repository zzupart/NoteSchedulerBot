from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from config import TgTOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(TgTOKEN)
dp = Dispatcher(bot, storage = MemoryStorage())
