import os

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
DEVELOPER_CHAT_ID = os.getenv('DEVELOPER_CHAT_ID')