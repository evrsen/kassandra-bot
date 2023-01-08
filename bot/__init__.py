from os import getenv
from discord import Intents

token = getenv("BOT_TOKEN")
prefix = getenv("BOT_PREFIX")
pg_user = getenv("POSTGRES_USER")
pg_pass = getenv("POSTGRES_PASSWORD")
pg_db = getenv("POSTGRES_DB")

intents = Intents.default()
intents.message_content = True