from os import environ, getenv
from Script import script

# 🚀 __Bot Configuration__
SESSION = environ.get('SESSION', 'RexBots')  # Session name
API_ID = int(environ.get('API_ID', '28578880'))
API_HASH = environ.get('API_HASH', '5f8c87efde57e01d12c0ce98ffdf5928')
BOT_TOKEN = environ.get('BOT_TOKEN', '')

# 👑 __Owner & Admins__
ADMINS = [int(i) for i in environ.get('ADMINS', '6814614245').split()]
AUTH_CHANNEL = [int(i) for i in environ.get("AUTH_CHANNEL", "-1003377088473").split()]
OWNER_USERNAME = environ.get("OWNER_USERNAME", 'skm')
BOT_USERNAME = environ.get("BOT_USERNAME", 'video_to_link_generation_bot')

# 🔗 __Channel & Support Links__
CHANNEL = environ.get('CHANNEL', 'https://t.me/Hasjsgdkd_bot')
SUPPORT = environ.get('SUPPORT', 'https://t.me/durov')
HOW_TO_VERIFY = environ.get('HOW_TO_VERIFY', 'https://t.me/how_to_open_link_ak')
HOW_TO_OPEN = environ.get('HOW_TO_OPEN', 'https://t.me/how_to_open_link_ak')

# 📢 __Log Channels__
BIN_CHANNEL = int(environ.get("BIN_CHANNEL", '-1003402780677'))
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", '-1003402780677'))
PREMIUM_LOGS = int(environ.get("PREMIUM_LOGS", '-1003402780677'))
VERIFIED_LOG = int(environ.get('VERIFIED_LOG', '-1003402780677'))
SUPPORT_GROUP = int(environ.get("SUPPORT_GROUP", "-1003402780677"))

# ✅ __Feature Toggles__
VERIFY = True # Enable user verification
FSUB = environ.get("FSUB", True)  # Force Subscribe
ENABLE_LIMIT = environ.get("ENABLE_LIMIT", True)
BATCH_VERIFY = False
IS_SHORTLINK = True
MAINTENANCE_MODE = environ.get("MAINTENANCE_MODE", False)
PROTECT_CONTENT = environ.get('PROTECT_CONTENT', True)
PUBLIC_FILE_STORE = environ.get('PUBLIC_FILE_STORE', True)
BATCH_PROTECT_CONTENT = environ.get('BATCH_PROTECT_CONTENT', True)

# 🔗 __Shortlink Configuration__
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'shrinkme.io')
SHORTLINK_API = environ.get('SHORTLINK_API', 'f6a16e5604aab9e7b6afb641d78b916fdaca2ccc')

# 💾 __Database Configuration__
DB_URL = environ.get('DATABASE_URI', "")
DB_NAME = environ.get('DATABASE_NAME', "skm")

# 📸 __Media & Images__
QR_CODE = environ.get('QR_CODE', 'https://ibb.co/mVkSySr7')
VERIFY_IMG = environ.get("VERIFY_IMG", "https://ibb.co/mVkSySr7")
AUTH_PICS = environ.get('AUTH_PICS', 'https://ibb.co/mVkSySr7')
PICS = environ.get('PICS', 'https://ibb.co/mVkSySr7')
FILE_PIC = environ.get('FILE_PIC', 'https://ibb.co/mVkSySr7')

# 📝 __Captions__
FILE_CAPTION = environ.get('FILE_CAPTION', script.CAPTION)
BATCH_FILE_CAPTION = environ.get('BATCH_FILE_CAPTION', script.CAPTION)
CHANNEL_FILE_CAPTION = environ.get('CHANNEL_FILE_CAPTION', script.CAPTION)

# ⏱️ __Time & Limits__
PING_INTERVAL = int(environ.get("PING_INTERVAL", 1200))
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', 60))
RATE_LIMIT_TIMEOUT = int(environ.get("RATE_LIMIT_TIMEOUT", 600))
MAX_FILES = int(environ.get("MAX_FILES", 500))
VERIFY_EXPIRE = int(environ.get('VERIFY_EXPIRE', 3))  # Hours

# ⚙️ __Worker & App Config__
WORKERS = int(environ.get('WORKERS', 10))
MULTI_CLIENT = False
NAME = environ.get('name', 'SM')

# 🌐 __Web Server__
ON_HEROKU = 'DYNO' in environ
APP_NAME = environ.get('APP_NAME') if ON_HEROKU else None

PORT = int(environ.get('PORT', 2626))
NO_PORT = str(environ.get("NO_PORT", "true")).lower() in ("true", "1", "yes")
HAS_SSL = str(environ.get("HAS_SSL", "true")).lower() in ("true", "1", "yes")

# URL Generation
BIND_ADDRESS = environ.get("WEB_SERVER_BIND_ADDRESS", "")   ##without https:// paste the base url here 
FQDN = environ.get("FQDN", BIND_ADDRESS)

if not FQDN.startswith("http"):
    PROTOCOL = "https" if HAS_SSL else "http"
    PORT_SEGMENT = "" if NO_PORT else f":{PORT}"
    
    # Clean up trailing slashes for consistency
    FQDN = FQDN.rstrip('/')
    URL = f"{PROTOCOL}://{FQDN}{PORT_SEGMENT}/"
else:
    URL = FQDN

