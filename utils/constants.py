import logging
import configparser
import os.path
from pathlib import Path
from sqlalchemy.orm import declarative_base


BASE_DIR = Path(__file__).resolve().parent.parent
LOG_FILE = os.path.join(BASE_DIR, "logs/bot.log")
DEV_SETTINGS = os.path.join(BASE_DIR, "dev_settings.ini")
SETTINGS = os.path.join(BASE_DIR, "settings.ini")
CURR_SETTINGS = ""

logging.basicConfig(filename=LOG_FILE, format='%(asctime)s -%(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
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
