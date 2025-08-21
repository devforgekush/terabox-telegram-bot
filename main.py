"""
TeraBox Telegram Bot
Downloads videos from TeraBox links and sends them to Telegram users with progress updates.

Developer: devforgekush
"""
import os
import re
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


BOT_TOKEN = os.getenv("BOT_TOKEN")
# Optional: TeraBox cookies for private links
TERABOX_COOKIES = os.getenv("TERABOX_COOKIES")

def parse_cookies(cookie_str):
    """Parse cookie string into a dict for requests."""
    if not cookie_str:
        return None
    cookies = {}
    for item in cookie_str.split(';'):
        if '=' in item:
            k, v = item.strip().split('=', 1)
            cookies[k] = v
    return cookies

COOKIES = parse_cookies(TERABOX_COOKIES)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📥 Send me a TeraBox link, I'll fetch the video for you!")


def get_terabox_link(url: str) -> str:
    """
    Extract direct video download link from TeraBox page HTML.
    Supports cookies for private links.
    """
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers, cookies=COOKIES)

    # Support terabox.com, 1024terabox.com, and terabox.club download links
    match = re.search(r'"(https://download\\.(terabox|1024terabox|terabox\\.club)\\.com[^"]+)"', r.text)
    if match:
        return match.group(1)
    # Debug: print HTML if link not found
    print("[DEBUG] TeraBox HTML Response:\n", r.text[:2000])  # Print first 2000 chars
    return None

async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.strip()
    msg = await update.message.reply_text("⏳ Fetching video...")

    try:
        dl_url = get_terabox_link(url)
        if not dl_url:
            await msg.edit_text("❌ Couldn't fetch video link. Check if the TeraBox link is public.")
            return

        # Check size before downloading
        r_head = requests.head(dl_url, headers={"User-Agent": "Mozilla/5.0"}, cookies=COOKIES)
        size = int(r_head.headers.get("content-length", 0))

        TELEGRAM_LIMIT = 1900 * 1024 * 1024

        if size > TELEGRAM_LIMIT:
            await msg.edit_text(
                f"⚠️ Video too large for Telegram upload ({size/1024/1024:.2f} MB).\n"
                f"Here’s the direct download link:\n{dl_url}"
            )
            return

        filename = "video.mp4"
        r = requests.get(dl_url, stream=True, cookies=COOKIES)
        downloaded = 0
        last_update = 0

        with open(filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024*1024):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    progress = int(downloaded / size * 100)
                    if progress - last_update >= 10:  # Update every 10%
                        await msg.edit_text(f"⬇️ Downloading... {progress}%")
                        last_update = progress

        await msg.edit_text("✅ Download complete! Uploading...")
        await update.message.reply_video(video=open(filename, "rb"))
        os.remove(filename)
        await msg.edit_text("✅ Done!")

    except Exception as e:
        await msg.edit_text(f"⚠️ Error: {str(e)}")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link))
    app.run_polling()

if __name__ == "__main__":
    main()
