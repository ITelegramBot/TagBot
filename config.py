import os

MONGO_URL = os.getenv("MONGO_URL", "")
MONGO_DB = os.getenv("MONGO_DB", "tagbot")
MONGO_DB = os.getenv("MONGO_DB", "telegram")
MONGO_COLL = os.getenv("MONGO_COLL", "tagbot")

MONGO_LIMIT = os.getenv("MONGO_LIMIT", "limit")
LIMIT_PRE_MIN = int(os.getenv("LIMIT_PRE_MIN", 10))

MONGO_USERNAME = os.getenv("MONGO_USERNAME", "username")

BOT_ID = os.getenv("BOT_ID", "")
