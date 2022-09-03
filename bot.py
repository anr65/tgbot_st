from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters

TELEGRAM_TOKEN = '5619065755:AAE-y3LbNOLKI1K30ZH4mJ7vJ7VHEbMx0CA'
TELEGRAM_SUPPORT_CHAT_ID = '323090420'
WELCOME_MESSAGE = 'Привет, это поддержка SharkTeam, напишите ваш вопрос'

updater = Updater(TELEGRAM_TOKEN)
dp = updater.dispatcher



def start(update, context):
    update.message.reply_text(WELCOME_MESSAGE)

    user_info = update.message.from_user.to_dict()

    context.bot.send_message(
        chat_id=TELEGRAM_SUPPORT_CHAT_ID,
        text=f"? Connected {user_info}.",
    )


def forward_to_chat(update, context):
    update.message.forward(chat_id=TELEGRAM_SUPPORT_CHAT_ID)


def forward_to_user(update, context):
    user_id = update.message.reply_to_message.forward_from.id
    context.bot.copy_message(
        message_id=update.message.message_id,
        chat_id=user_id,
        from_chat_id=update.message.chat_id
    )


dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.chat_type.private, forward_to_chat))
dp.add_handler(MessageHandler(Filters.chat(TELEGRAM_SUPPORT_CHAT_ID) & Filters.reply, forward_to_user))

