from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**
🌠I'm ѕαυαи💞 - a bot which helps you to listen music on vc. \n🥀Run smoothly \n🔥 Listen high quality music \n🌷 Owner [Saurav Pandey] (https://t.me/SauravPanday)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌹Owner🌹", url="https://t.me/SauravPanday")
                  ],[
                    InlineKeyboardButton(
                        "⚜Support⚜", url="https://t.me/Online_hangover"
                    ),
                    InlineKeyboardButton(
                        "⚜Updates⚜", url="https://t.me/SauanNews"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "🌹Add Me🌹", url="https://t.me/SauanBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("hexor") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**ѕαυαи💞 is On\n@DigiGleam <3**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚜Updates⚜", url="https://t.me/SauanNews")
                ]
            ]
        )
   )
