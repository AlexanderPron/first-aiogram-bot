import logging
import configparser
import os.path
from pathlib import Path
from sqlalchemy.orm import declarative_base
from utils.botObjects import MasterData

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_FILE = os.path.join(BASE_DIR, "logs/bot.log")
DEV_SETTINGS = os.path.join(BASE_DIR, "dev_settings.ini")
SETTINGS = os.path.join(BASE_DIR, "settings.ini")
CURR_SETTINGS = ""

try:
    f = open(LOG_FILE)
except IOError:
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    f = open(LOG_FILE, 'w')
    f.close

logging.basicConfig(
    level=logging.WARNING,
    filename=LOG_FILE,
    format='%(asctime)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    encoding='utf-8',
)
logger = logging.getLogger(__name__)
config = configparser.ConfigParser()

if os.path.isfile(DEV_SETTINGS):
    config.read(DEV_SETTINGS)
    CURR_SETTINGS = DEV_SETTINGS
elif os.path.isfile(SETTINGS):
    config.read(SETTINGS)
    CURR_SETTINGS = SETTINGS
else:
    logger.error('No settings file!')
    print('No settings file!')
    exit()
try:
    API_TOKEN = config["Telegram"]["token"]
    MANAGER_ID = config["Telegram"]["manager_id"]
except Exception:
    logger.error(f"Something wrong with {CURR_SETTINGS}")
    exit()

try:
    DB_HOST = config["DataBase"]["db_host"]
    DB_PORT = config["DataBase"]["db_port"]
    DB_USER = config["DataBase"]["db_user"]
    DB_NAME = config["DataBase"]["db_name"]
    DB_PASS = config["DataBase"]["db_pass"]
except Exception:
    logger.error(f"Something wrong with {CURR_SETTINGS}")
    exit()

engine_str = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
Base = declarative_base()

# =========== Переделать ==============
master1 = MasterData(
    master_id=1,
    first_name='Иван',
    last_name='Сусанин',
)
master2 = MasterData(
    master_id=2,
    first_name='Мария',
    last_name='Трошкина',
)
master3 = MasterData(
    master_id=3,
    first_name='Бек',
    last_name='Абдурахманов',
)
master4 = MasterData(
    master_id=4,
    first_name='Абдуазим',
    last_name='Араратов',
)
master5 = MasterData(
    master_id=5,
    first_name='Куни',
    last_name='Ли',
)
masters = [master1, master2, master3, master4, master5]
# ===============================================================
