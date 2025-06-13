from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile
import os
import subprocess

router = Router()

class OrderVideo(StatesGroup):
    waiting_for_tiktok_url = State()
    waiting_for_inst_reels_url = State()

def download_tiktok_video(url):
    result = subprocess.run([
        'yt-dlp',
        url,
        '-o', 'tiktok.%(ext)s'
    ])
    return 'tiktok.mp4' if result.returncode == 0 else None

def download_instagram_reel(url: str) -> str:
    result = subprocess.run([
        'yt-dlp',
        '--cookies', 'cookies.txt',
        url,
        '-o', 'reel.%(ext)s'
    ], shell=True, capture_output=True, text=True)

    print(result.stdout)  
    print(result.stderr)  

    return 'reel.mp4' if result.returncode == 0 else None


@router.message(Command("start"))
async def start(message: Message):
    buttons = [
        [InlineKeyboardButton(text="TikTok", callback_data="tiktok"),
         InlineKeyboardButton(text="Instagram", callback_data="inst_reels")]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    await message.answer(
        "👋 Hi! I'm a bot that helps you **download videos from Instagram and TikTok without watermarks**.\n\n"
        "Click a button and send me the video link. I'll handle the rest! 🔗", reply_markup=kb
    )

@router.callback_query(F.data == "tiktok")
async def tiktok_video(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Now send me the TikTok video link")
    await state.set_state(OrderVideo.waiting_for_tiktok_url)
    await callback.answer()

@router.callback_query(F.data == "inst_reels")
async def instagram_reels(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Now send me the Instagram Reels link")
    await state.set_state(OrderVideo.waiting_for_inst_reels_url)
    await callback.answer()

async def process_for_download(message: Message, state: FSMContext, platform=None):
    await message.answer("Downloading video...")
    path = None
    if platform == "tiktok":
        path = download_tiktok_video(message.text)
    elif platform == "inst":
        path = download_instagram_reel(message.text)
    if path and os.path.exists(path):
        video = FSInputFile(path)
        await message.answer_video(video=video, caption="Here is your video!")
        try:
            os.remove(path)  
        except Exception as e:
            await message.answer(f"⚠️ Could not delete the file: {e}")
    else:
        await message.answer("Failed to download the video. Please make sure the link is correct.")
    
    await state.clear()


@router.message(OrderVideo.waiting_for_tiktok_url)
async def tiktok_download_handler(message: Message, state: FSMContext):
    await process_for_download(message, state, platform="tiktok")

@router.message(OrderVideo.waiting_for_inst_reels_url)
async def instagram_download_handler(message: Message, state: FSMContext):
    await process_for_download(message, state, platform="inst")
