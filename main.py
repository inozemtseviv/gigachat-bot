import os
from dotenv import load_dotenv

from app.bot.bot import Bot

load_dotenv()

tg_giga = Bot(os.getenv('TG_TOKEN'))

tg_giga.run()