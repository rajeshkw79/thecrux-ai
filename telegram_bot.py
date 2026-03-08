import os, subprocess
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ALLOWED_USER = int(os.getenv("TELEGRAM_USER_ID"))
BOT_DIR = os.path.dirname(os.path.abspath(__file__))

def is_allowed(update: Update) -> bool:
    return update.effective_user.id == ALLOWED_USER

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if is_allowed(update):
        await update.message.reply_text("Your AI assistant is online.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_allowed(update):
        return
    try:
        result = subprocess.run(
            ["claude", "-p", update.message.text],
            capture_output=True, text=True, timeout=120, cwd=BOT_DIR
        )
        response = result.stdout.strip() or result.stderr.strip() or "No response from Claude."
    except subprocess.TimeoutExpired:
        response = "Claude timed out."
    except Exception as e:
        response = f"Error: {e}"
    for i in range(0, len(response), 4096):
        await update.message.reply_text(response[i:i + 4096])

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot is running...")
    app.run_polling()
