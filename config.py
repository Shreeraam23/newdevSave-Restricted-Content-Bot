# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "28036362"))
API_HASH = getenv("API_HASH", "84e4bd8457dab2f065801bde8874842a")
BOT_TOKEN = getenv("BOT_TOKEN", "7658096840:AAFctpiYtmrhfwlpTb42b5bh2H72Ba8ILXE")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7576455886").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://koxiher824:uhWjdKAzmfAHcagy@cluster0.lg66r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002286606634")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002314245462"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "5000"))
