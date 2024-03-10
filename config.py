from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "1500"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/e736724b3263561a666cd.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/e736724b3263561a666cd.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/VK4444")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/vk4444")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1279427042").split()))


FAILED = "https://graph.org/file/e736724b3263561a666cd.jpg"
