import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
COMMAND_PREFIX = os.getenv("COMMAND_PREFIX", "!")

WELCOME_CHANNEL_ID = int(os.getenv("WELCOME_CHANNEL_ID", 0))
GOODBYE_CHANNEL_ID = int(os.getenv("GOODBYE_CHANNEL_ID", 0))

if not DISCORD_TOKEN:
    raise ValueError(
        "Eror tolol wkwkkw"
    )
