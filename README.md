TikTok & Instagram Video Downloader Bot
This is a Telegram bot built with aiogram and yt-dlp.
It allows you to download videos from TikTok (without watermark) and Instagram Reels directly via links.

Features
Download TikTok videos without watermark.

Download Instagram Reels (including age-restricted content).

Automatically sends the downloaded video to the user in chat.

Requirements
Python 3.10+

yt-dlp

aiogram

For Instagram Reels, a cookies.txt file is required.

How to get cookies.txt (for Instagram Reels)
Some Reels are restricted by age (18+) and cannot be downloaded without being logged in.

Use Firefox and install the extension cookies.txt.

Log into your Instagram account (age must be 18+).

Open any Reels page.

Export cookies using the extension as cookies.txt.

Place cookies.txt in the project root folder.

Without valid cookies, some Reels may fail to download due to Instagram's restrictions.
