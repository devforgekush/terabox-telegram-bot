
# TeraBox Telegram Bot

**Description**
A Telegram bot that downloads videos directly from TeraBox links (`terabox.com`, `1024terabox.com`, `terabox.club`) and sends them to you on Telegram. Includes progress updates during download. Supports private links using cookies.

**Features**
- Download from TeraBox (`terabox.com`, `1024terabox.com`, `terabox.club`)
- Progress updates
- File delivery in Telegram
- Private link support (via cookies)

**Installation**
1. Clone the repository:
   ```sh
   git clone https://github.com/devforgekush/terabox-telegram-bot.git
   cd terabox-telegram-bot
   ```
2. Install requirements:
   ```sh
   pip install -r requirements.txt
   ```
3. Set environment variables:
   - `BOT_TOKEN`: Your Telegram bot API key
   - `TERABOX_COOKIES`: (optional) Cookie string for private TeraBox links (format: `key1=value1; key2=value2; ...`)
   
   On Windows (PowerShell):
   ```powershell
   $env:BOT_TOKEN="your-telegram-bot-token"
   $env:TERABOX_COOKIES="your-terabox-cookies"
   ```
   On Linux/macOS:
   ```sh
   export BOT_TOKEN="your-telegram-bot-token"
   export TERABOX_COOKIES="your-terabox-cookies"
   ```
4. Run the bot:
   ```sh
   python main.py
   ```

**Usage**
- Send a public or private TeraBox video link to the bot in Telegram.
- The bot will fetch, download, and send the video file to you, with progress updates.

**Credits**
Developed by [devforgekush](https://github.com/devforgekush)
