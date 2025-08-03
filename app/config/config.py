from dotenv import load_dotenv
import os

from app.config.logger_config import str_to_bool
load_dotenv(dotenv_path="app/env/config.env")


SHOW_NOTIFICATION=str_to_bool((os.getenv("NOTIFICATION")))

# ENV_DIRECTORY=fr"app\env"
