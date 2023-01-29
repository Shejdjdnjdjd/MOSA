from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "24928036"))
API_HASH = getenv("API_HASH", "762f095044e7a6952422685e8abb4701")
BOT_TOKEN = getenv("BOT_TOKEN", "5574038306:AAEWYHQuKQP_0cnUWWxRArXeqElnuKzInUo")
SESSION_NAME = getenv("SESSION_NAME", "1BJWap1wBu2D70hlZnQobPN7up4qcnevkYTXgACFqm4myhQqV25JvLtXMAL8tLZ-okorzD0VCraqpKL0OTy6gqrFDDFWynoGN4LHEkkCS3hlmy4kEC4C8rtvUsGMg9QoUVNVmBhwTNmUIKhkHSnVi5qykQ_nadS_o433Ir7DFz6gnad--8jvgbyIQlzPAIpVUk-4GGqJl2VH8JMQ-eldP4SF_MLod4jQnBlfe0MiQUBs2AmV7KwQ5C0qv2Q7SPOfLaWv4coda0qpzbd_CJzze9_nUFoEbib4WifeoFsVZYHa1TFcYQnb-q0-gEVRVVHrIuZvusxx1N-4UAYrNMZVHUycITOEiVcA=")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "Y_G_U")
ALIVE_NAME = getenv("ALIVE_NAME", "Fakm")
BOT_USERNAME = getenv("BOT_USERNAME", "Eev1eebot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/levina-lab/video-stream")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Y_9_C")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0 .heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "5812571544").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5812571544").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
