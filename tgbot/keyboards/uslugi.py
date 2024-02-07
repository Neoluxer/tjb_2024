from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

uslugi = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Обмеры (70)"),
            KeyboardButton(text="Планировочные решения (150)"),
        ],

        [
            KeyboardButton(text="Фор-проект (400) "),
            KeyboardButton(text="Д.П.с комплектацией"),
        ],

        [
            KeyboardButton(text="Полный дизайн проект (1500)"),
        ],

        [
            KeyboardButton(text="Д.П.с комплектацией и авторским (2200)"),
            KeyboardButton(text="Д.П.с авторским (1800)" ),
        ],

    ],
    resize_keyboard=True
)
