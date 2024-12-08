from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SONALI import app
from config import BOT_USERNAME
from SONALI.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """       Ｗｅｌｃｏｍｅ　ｔｏ　ｒｅｐｏ

1. “You must be the change you wish to see in the world.”

2. “Spread love everywhere you go. Let no one ever come to you without leaving happier.”

3. “The only thing we have to fear is fear itself.”

4. “Do one thing every day that scares you.” 
 
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔ᴅᴅ ᴍᴇ 𝗠ᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗗𝗽_𝗰𝗼𝗹𝗹𝗲𝗰𝘁𝗶𝗼𝗻", url="https://t.me/DP_WORLD7"),
          InlineKeyboardButton("ᵐⁱˢˢ🦋ᴀ ʀ ᴀ ᴅ ʜ ʏ ᴀ", url="https://t.me/ARADHYA_ASISTANT"),
          ],
               [
                InlineKeyboardButton("𝗧ᴇᴀᴍ 𝗜ɴᴄʀɪᴄɪʙʟᴇ 𝗕ᴏᴛs", url=f"https://t.me/ll_BOTCHAMBER_ll"),
],
[
InlineKeyboardButton("𝗠ᴀɪɴ 𝗕ᴏᴛ", url=f"https://t.me/zeus_MUSIC_ROBOT"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/6b113497feeae0968785e-bc3f1b4d6fd3a18755.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
