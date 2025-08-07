import threading

from app.utils.file_utils import *
from app.utils.tray import *
# Настройка логгера
logger = create_logger("main")
toggle_logging(logger)


def main():
    while not stop_event.is_set(): # Цикл, пока не закрыт трей
        print("successful")




if __name__ == "__main__":
    if check_file("app/env/config.env") and check_file("app/env/logger_config.env"):
        # Для синхронизации между потоками
        stop_event = threading.Event()

        # Создаём и запускаем трей(В отдельном потоке)
        icon = create_tray(stop_event)
        thread = threading.Thread(target=run_icon, args=(icon, stop_event), daemon=True)
        thread.start()

        main()