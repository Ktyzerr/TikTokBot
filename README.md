# TikTok & Instagram Video Downloader Bot

Telegram bot to download videos from TikTok (without watermark) and Instagram Reels.

## Features

- Download TikTok videos without watermark  
- Download Instagram Reels including age-restricted content  
- Sends downloaded videos directly in chat

## Requirements

- Python 3.10+  
- yt-dlp  
- aiogram  
- For Instagram Reels downloads, you need a `cookies.txt` file

## Getting cookies.txt for Instagram Reels

Instagram restricts some Reels (18+) and requires login cookies to download them.

1. Use **Firefox** browser  
2. Install the [cookies.txt extension](https://addons.mozilla.org/en-US/firefox/addon/cookies-txt/)  
3. Log in to your Instagram account (age 18+)  
4. Open any Instagram Reels page  
5. Export cookies using the extension as `cookies.txt`  
6. Place `cookies.txt` in your project root folder

Without these cookies, some Instagram Reels will not download due to age restrictions.

## Installation

```bash
pip install aiogram yt-dlp
Setup
Put your bot token inside your bot script, e.g.

python
Копировать
Редактировать
API_TOKEN = "YOUR_TELEGRAM_BOT_API_KEY"
Make sure cookies.txt is in your project folder (for Instagram Reels downloads)

Run the bot
bash
Копировать
Редактировать
python bot.py
