from app.utils.file_utils import *

# Настройка логгера
logger = create_logger("main")
toggle_logging(logger)


def main():
    print("successful")




if __name__ == "__main__":
    if check_file("app/env/config.env") and check_file("app/env/logger_config.env"):
        main()