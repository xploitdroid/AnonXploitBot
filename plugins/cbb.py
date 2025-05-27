from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>𝙲𝚘𝚖𝚙𝚕𝚎𝚝𝚎𝚕𝚢 𝙰𝚗𝚘𝚗𝚢𝚖𝚘𝚞𝚜 𝙵𝚒𝚕𝚎 𝚂𝚎𝚗𝚍𝚒𝚗𝚐 𝙱𝚘𝚝 𝙲𝚛𝚎𝚊𝚝𝚎𝚍 𝙱𝚢 </b> <a href='https://t.me/Darkthrax'>𝙳𝚊𝚛𝚔𝚃𝚑𝚛𝚊𝚡</a> \n\n<b>𝚃𝚑𝚒𝚜 𝙱𝚘𝚝 𝚒𝚜 𝙲𝚛𝚎𝚊𝚝𝚎𝚍 𝙵𝚘𝚛 𝙿𝚛𝚒𝚟𝚊𝚌𝚢 𝙰𝚗𝚍 𝚂𝚎𝚌𝚞𝚛𝚒𝚝𝚢 𝚁𝚎𝚊𝚜𝚘𝚗𝚜</b> \n\n<b>𝚃𝚑𝚒𝚜 𝙱𝚘𝚝 𝚒𝚜 𝙲𝚘𝚖𝚙𝚕𝚎𝚝𝚎𝚕𝚢 𝙵𝚛𝚎𝚎 𝙵𝚘𝚛 𝙴𝚟𝚎𝚛𝚢𝚘𝚗𝚎 𝚃𝚘 𝚄𝚜𝚎</b> \n\n<b>⚠️ 𝙱𝚘𝚝 𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛 :- @DarkThrax</b>",            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass





# Developer Ankit 
# Don't Remove Credit 🥺
# Telegram Channel @XploitBots
# Backup Channel @XploitdroidBots
# Developer @Xploitdroid
