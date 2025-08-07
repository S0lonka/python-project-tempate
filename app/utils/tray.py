from pystray import Icon, Menu, MenuItem
from PIL import Image

from app.config.tray_flag import stop_event 
from app.utils.general_utils import create_logger, toggle_logging
from app.config.project_config import PROJECT_NAME

# Глобальный флаг для выхода
exit_flag = False

logger = create_logger("tray")
toggle_logging(logger)

def create_tray(stop_event_flag):
    '''Основной конструктор иконки трея'''

    icon_image = Image.open("app/img/icon/icon.ico")

    # Создаём трей
    tray_icon = Icon(
        name = f"{PROJECT_NAME}",
        title = f"{PROJECT_NAME}",
        icon = icon_image,

        # Настройка пунктов меню
        menu = Menu(
            MenuItem('Выйти', lambda icon, item: off_assistant(icon, item, stop_event_flag))
        )
    )

    return tray_icon


def run_icon(icon, flag_event):
    icon.run()
    flag_event.set()  # Сигнализируем, что трея завершился


def off_assistant(icon, item, stop_event_flag):
    logger.info("Пользователь выбрал 'Выход'")
    
    icon.stop()
    stop_event_flag.set()