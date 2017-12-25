import os

MONGO_URL = os.getenv("MONGO_URL", "")
MONGO_DB = os.getenv("MONGO_DB", "tagbot")
MONGO_DB = os.getenv("MONGO_DB", "telegram")
MONGO_COLL = os.getenv("MONGO_COLL", "tagbot")

BOT_ID = os.getenv("BOT_ID", "")
