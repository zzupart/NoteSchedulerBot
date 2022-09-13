from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from config import TgTOKEN

bot = Bot(TgTOKEN)
dp = Dispatcher(bot)
