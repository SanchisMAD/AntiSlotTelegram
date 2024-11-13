from telegram import Update
from telegram.ext import Application, MessageHandler, filters

# Bot token
TOKEN = '7874640057:AAERI1_agBABdCckM71H85UWNxJjz2X3c30'

async def handle_message(update: Update, context):
    if update.message and update.message.dice:
        try:
            # Delete any dice message, including slot machine
            await update.message.delete()
            if update.message.from_user:
                print(f"Deleted dice message (emoji: {update.message.dice.emoji}, value: {update.message.dice.value}) from user {update.message.from_user.username}")
            else:
                print(f"Deleted dice message (emoji: {update.message.dice.emoji}, value: {update.message.dice.value}) from unknown user")
        except Exception as e:
            print(f"Error deleting message: {e}")

def main():
    # Create the Application and pass it your bot's token
    application = Application.builder().token(TOKEN).build()

    # Add a handler for dice messages
    application.add_handler(MessageHandler(filters.Dice.ALL, handle_message))

    # Start the bot
    print("Bot is running. Press Ctrl+C to stop.")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()