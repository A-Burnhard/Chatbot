
from typing import Final
from telegram.ext import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '6638899988:AAE3fyEhayk6J7Rn-g0rJb_4kU5K56OZXD8'
BOT_USERNAME : Final = '@legongpt_bot'


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello Kojo")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("yeah here to help  Kojo")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello Kojo")

#Responses

def handle_response(text:str) -> str:
    processed: str = text.lower()
    if 'hello' in processed:
        return 'hey love'
    
    return 'you koraa why'
    
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPES):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"  ')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME,'').strip()
            response: str = handle_response(new_text)

        else:
            response: str = handle_response(text)

        print('Bot:', response)
        await update.message.reply_text(response)

async def error (update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'update{update} caused error {context.type}')

if __name__ == '__main__':
    print('Starting bot....')
    app = Application.builder().token(TOKEN).build()

    #commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    #messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #Errors
    app.add_error_handler(error)

    #polls the bot
    print('Polling...')
    app.run_polling(poll_interval=2)

