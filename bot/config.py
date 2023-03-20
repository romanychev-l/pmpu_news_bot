import os
import json

import dotenv

dotenv.load_dotenv()

MY_ID: int = int(os.getenv("VAR_MY_TELEGRAM_ID", 248603604))
# TG_CHANNEL: str = os.getenv("VAR_TG_CHANNEL", "@amcp_feed")
TG_CHANNEL: str = os.getenv("VAR_TG_CHANNEL", "@nethub_test_channel")
TG_BOT_TOKEN: str = os.getenv("VAR_TG_BOT_TOKEN", "5204155927:AAE7qaTWZ5la4YQw-JruHztc3ycfMUqYyZE")
VK_TOKEN: str = os.getenv("VAR_VK_TOKEN", "566214435662144356621443e5560a2ea255662566214430a2a6f6205658190bc5351eb")
VK_DOMAIN: str = os.getenv("VAR_VK_DOMAIN", "")

REQ_VERSION: float = float(os.getenv("VAR_REQ_VERSION", 5.103))
REQ_COUNT: int = int(os.getenv("VAR_REQ_COUNT", 2))
REQ_FILTER: str = os.getenv("VAR_REQ_FILTER", "owner")

SINGLE_START: bool = os.getenv("VAR_SINGLE_START", "").lower() in ("true",)
TIME_TO_SLEEP: int = int(os.getenv("VAR_TIME_TO_SLEEP", 120))
SKIP_ADS_POSTS: bool = os.getenv("VAR_SKIP_ADS_POSTS", "").lower() in ("true",)
SKIP_COPYRIGHTED_POST: bool = os.getenv("VAR_SKIP_COPYRIGHTED_POST", "").lower() in ("true")
SKIP_REPOSTS: bool = os.getenv("VAR_SKIP_REPOSTS", "false").lower() in ("true")

WHITELIST: list = json.loads(os.getenv("VAR_WHITELIST", "[]"))
BLACKLIST: list = json.loads(os.getenv("VAR_BLACKLIST", "[]"))
