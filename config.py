import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "7562162609:AAG0SSDDr-js6606LJQWv6weda3xdF6SCI0")
API_ID = int(os.environ.get("API_ID", "21442811"))
API_HASH = os.environ.get("API_HASH", "b6e4ff464a9a82bea74f72dd70eab0a1")


OWNER_ID = int(os.environ.get("OWNER_ID", "8181951014"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://AnonXploit:AnonXploit@cluster0.ekhbgxy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "AnonXploit")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002515503407"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))


FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "90")) # auto delete in seconds


PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[6848088376]
    for x in (os.environ.get("ADMINS", "8181951014").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', "True") == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "❌Don't Send Me Messages Directly I'm Only File Share Bot !"

START_MSG = os.environ.get("START_MESSAGE", "𝙷𝚊𝚒 {mention}\n\n𝙸 𝚊𝚖 𝚢𝚘𝚞𝚛 𝚊𝚍𝚟𝚊𝚗𝚌𝚎 𝙰𝚗𝚘𝚗𝚢𝚖𝚘𝚞𝚜 𝚏𝚒𝚕𝚎 𝚂𝚎𝚗𝚍𝚎𝚛 𝙱𝚘𝚝 ❤️/n𝙸𝚏 𝚈𝚘𝚞𝚛 𝚞𝚜𝚒𝚗𝚐 𝚖𝚎 𝚝𝚑𝚊𝚗 𝚒 𝚠𝚒𝚕𝚕 𝙵𝚘𝚛𝚠𝚊𝚛𝚍 𝚢𝚘𝚞𝚛 𝚏𝚒𝚕𝚎𝚜 𝙴𝚊𝚜𝚒𝚕𝚢 𝚊𝚗𝚍 𝙰𝚗𝚘𝚗𝚢𝚖𝚘𝚞𝚜𝚕𝚢 🏴\n𝙱𝚘𝚝 𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛 :- @𝙳𝚊𝚛𝚔𝚃𝚑𝚛𝚎𝚡.")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {mention}\n\n<b>You Need To Join In My Channel/Group To Use Me\n\nKindly Please Join Channel</b>")





ADMINS.append(OWNER_ID)
ADMINS.append(8181951014)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   





# Developer Ankit 
# Don't Remove Credit 🥺
# Telegram Channel @XploitBots
# Backup Channel @XploitdroidBots
# Developer @Xploitdroid
