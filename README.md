# TeraBox Telegram Bot

**Description**
A Telegram bot that downloads videos directly from TeraBox links and sends them to you on Telegram. Includes progress updates during download.

**Features**
- Download from TeraBox
- Progress updates
- File delivery in Telegram

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
   
   On Windows (PowerShell):
   ```powershell
   $env:BOT_TOKEN="your-telegram-bot-token"
   ```
   On Linux/macOS:
   ```sh
   export BOT_TOKEN="your-telegram-bot-token"
   ```
4. Run the bot:
   ```sh
   python main.py
   ```


**Usage**
- Send a public TeraBox video link to the bot in Telegram.
- The bot will fetch, download, and send the video file to you, with progress updates.

**Credits**
Developed by [devforgekush](https://github.com/devforgekush)

**Credits**
Developed by `devforgekush`.
