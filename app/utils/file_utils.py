from pathlib import Path
import logging
import os

from app.utils.general_utils import *
from app.utils.notification import My_notification
from app.template.env_content import config_env_lines




# Настройка логгера
logger = create_logger("main")
toggle_logging(logger)



# Экземпляр класса уведомлений
notyfi = My_notification() 

def check_file(path: str) -> bool:
    """Проверка что файл существует(для ENV)
    
    Args:
        path (str) : Относительный путь до файла который нужно проверить.
    
    Returns:
        bool : Если файла не существует, создаёт его и возвращает False
    """
    path = fr"{os.getcwd()}\{path}"

    if Path(path).is_file():
        return True
    else:
        create_file(path, config_env_lines)

        (notyfi  # Показываем уведомление
        .create_notification("WARNING | Создан ENV файл", f"Создан файл по пути {path} проверьте и заполните его", duration="long")
        .show())

        logger.warning(f"Создан файл по пути: {path}")

        return False
    

def create_file(filepath: str, line_content: list[str]) -> None:
    """Создаёт и записывает заданные линии в файл

    Args:
        filepath     (str)       : Путь до целевого файла
        line_content (list[str]) : Массив строк которыми заполнится файл
    
    Return:
        None
    """

    with open(filepath, "w", encoding="UTF-8") as file:
        file.writelines('\n'.join(line_content))



