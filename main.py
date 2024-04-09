import inspect
import logging

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

import handlers
from config.config import TELEGRAM_TOKEN

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)


class Bot:
    def __init__(self, telegram_token: str):
        self.app = ApplicationBuilder().token(telegram_token).build()
        self.register_handlers()

    def register_handlers(self):
        # Iterate over all members of the handlers module
        for name, obj in inspect.getmembers(handlers):
            # Check if the member is a class and has a register method
            if inspect.isclass(obj) and issubclass(obj, handlers.BaseHandler):
                # Call the register method for the class
                obj.register(self.app)

    def start(self):
        self.app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    Bot(TELEGRAM_TOKEN).start()
