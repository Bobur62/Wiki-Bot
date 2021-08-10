# from telegram.bot import Bot
# from telegram.user import User

from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.update import Update
import settings

# bot = Bot(token="1909013629:AAGfSC7t8hTPvMtoSJPQ68EvsfToeWumDaQ")
# # print(bot.get_me())
# user: User = bot.get_me()
# print(user.first_name)


updeter = Updater(token=settings.TELEGRAM_TOKEN)

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Salom')
    context.bot.send_message(
        chat_id=update.message.chat_id, text='Salom yana bir bor'
    )


dispatcher = updeter.dispatcher
dispatcher.add_handler(CommandHandler('start', start))

updeter.start_polling()
updeter.idle()