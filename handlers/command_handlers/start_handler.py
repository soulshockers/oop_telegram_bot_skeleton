from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from handlers.base_handler import BaseHandler


class StartHandler(BaseHandler):
    @classmethod
    def register(cls, app) -> None:
        app.add_handler(CommandHandler("start", cls.callback))

    @staticmethod
    async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(f'Start {update.effective_user.first_name}')
