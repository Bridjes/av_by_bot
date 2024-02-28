from aiogram.contrib.fsm_storage.files import JSONStorage
from pathlib import Path
from .local_settings import API_Key
from aiogram import Dispatcher, Bot

bot = Bot(token=API_Key)
dp = Dispatcher(bot, storage=JSONStorage(Path.cwd() / "fsm_data.json"))