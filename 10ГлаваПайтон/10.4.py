from pathlib import Path
import os
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

try:
    o = input("То что хотите сохранить: ")

    path = Path("higaa.txt")
    path.write_text(o, encoding="utf-8")

    logging.info("Файл higaa.txt создан и текст сохранён")

    h = input("Удалить ваше предложение (y/n): ")

    if h == "y":
        os.remove("higaa.txt")
        logging.info("Файл higaa.txt удалён пользователем")
    else:
        logging.info("Пользователь оставил файл")

except Exception as e:
    logging.error(f"Ошибка: {e}")