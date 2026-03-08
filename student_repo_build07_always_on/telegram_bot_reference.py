"""
Reference Telegram bot for Build 7 - Phase 1.
Reads TELEGRAM_BOT_TOKEN and TELEGRAM_USER_ID from .env in the same directory.
Passes messages to Claude via `claude -p` so it reads your CLAUDE.md.

Usage:
  pip install python-telegram-bot python-dotenv
  python telegram_bot_reference.py
"""

import os
import subprocess
from pathlib import Path
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

load_dotenv(Path(__file__).parent / ".env")

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
ALLOWED_USER_ID = int(os.environ["TELEGRAM_USER_ID"])
PROJECT_DIR = str(Path(__file__).parent)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ALLOWED_USER_ID:
        return
    await update.message.reply_text("Your AI assistant is online.")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ALLOWED_USER_ID:
        return

    user_msg = update.message.text
    await update.message.reply_text("Thinking...")

    try:
        result = subprocess.run(
            ["claude", "-p", user_msg],
            capture_output=True, text=True, timeout=120,
            cwd=PROJECT_DIR
        )
        response = result.stdout.strip() or result.stderr.strip() or "No response from Claude."
    except subprocess.TimeoutExpired:
        response = "Claude took too long to respond. Try a shorter question."
    except FileNotFoundError:
        response = "Claude CLI not found. Make sure 'claude' is on your PATH."

    # Telegram has a 4096-character message limit — chunk if needed
    for i in range(0, len(response), 4096):
        await update.message.reply_text(response[i:i + 4096])


app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print(f"Bot running. Only responding to user ID: {ALLOWED_USER_ID}")
print("Press Ctrl+C to stop.")
app.run_polling()
