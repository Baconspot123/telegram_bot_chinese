import logging
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from deep_translator import GoogleTranslator

# Enable logging so you can see details in your terminal
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Updated with your new token!
TOKEN = “Insert token her!!”

async def start(update: Update, context: CallbackContext) -> None:
    """Sends a greeting message when the command /start is issued."""
    await update.message.reply_text(
        "👋 Hello! Send me any text, and I will translate it!\n\n"
        "• English text will turn into *Chinese (Simplified)*.\n"
        "• Chinese text will turn into *English*.",
        parse_mode="Markdown"
    )

async def handle_translation(update: Update, context: CallbackContext) -> None:
    """Detects Chinese characters locally and routes the translation flawlessly."""
    user_text = update.message.text
    
    try:
        loop = asyncio.get_running_loop()
        
        # Local check: Looks for common Chinese Unicode character ranges
        has_chinese = any('\u4e00' <= char <= '\u9fff' for char in user_text)
        
        if has_chinese:
            # Force source as Chinese and target as English
            source_lang = 'zh-CN'
            target_lang = 'en'
            lang_label = "English"
        else:
            # Force source as English and target as Chinese
            source_lang = 'en'
            target_lang = 'zh-CN'
            lang_label = "Chinese (Simplified)"
            
        # Perform the translation using explicit source and target languages
        translated_text = await loop.run_in_executor(
            None, lambda: GoogleTranslator(source=source_lang, target=target_lang).translate(user_text)
        )
        
        # Reply back to the user
        response = f"*Translation ({lang_label}):*\n{translated_text}"
        await update.message.reply_text(response, parse_mode="Markdown")
        
    except Exception as e:
        logger.error(f"Translation error: {e}")
        await update.message.reply_text("⚠️ Sorry, I ran into an error trying to translate that. Please try again!")

def main():
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_translation))

    # Run the bot until you press Ctrl-C
    print("Bot is running... Press Ctrl+C to stop.")
    application.run_polling()

if __name__ == '__main__':
    main()
