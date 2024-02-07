from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from datetime import datetime
current_year = datetime.now().year

style_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Современный"),
            KeyboardButton(text="Классика"),
        ],

        [
            KeyboardButton(text="Анлийский"),
            KeyboardButton(text=" Шале"),
        ],

        [
            KeyboardButton(text="Кантри"),
            KeyboardButton(text="Неоклассика"),
        ],

        [
            KeyboardButton(text="Loft"),
            KeyboardButton(text="Скандинавский стиль"),
        ],

    ],
    resize_keyboard=True
)

organisations_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ОАО «Астон»"),
            KeyboardButton(text="ООО «Неолюкс»"),

        ],

    ],
    resize_keyboard=True
)
price_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1250"),
            KeyboardButton(text="1500"),
        ],

        [
            KeyboardButton(text="1800"),
            KeyboardButton(text="2000"),
        ],

        [
            KeyboardButton(text="2200"),
        ],

    ],
    resize_keyboard=True
)

town_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Краснодар"),
            KeyboardButton(text="Москва"),
        ],

        [
            KeyboardButton(text="Екатеринбург"),
            KeyboardButton(text="Сочи"),
        ],

    ],
    resize_keyboard=True
)

yes_or_no = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1"),
            KeyboardButton(text="0"),
        ],

    ],
    resize_keyboard=True
)

source = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Instagram"),
            KeyboardButton(text="www.neoluxe.ru"),
        ],
        [
            KeyboardButton(text="рекомендации"),
            KeyboardButton(text="реклама"),
        ],

    ],
    resize_keyboard=True
)

services = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="дизайн-проект"),
            KeyboardButton(text="обмеры"),
        ],
        [
            KeyboardButton(text="комплектация"),
            KeyboardButton(text="фор-проект"),
        ],

        [
            KeyboardButton(text="планировка"),
            KeyboardButton(text="другое"),
        ],

    ],
    resize_keyboard=True
)

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/add_lid"),
            KeyboardButton(text="/add_profit"),
            KeyboardButton(text="/cancel"),

        ],

        [
            KeyboardButton(text="/invoice"),
            KeyboardButton(text="/admin"),
            KeyboardButton(text="/worksheet_link"),
        ],
[
            KeyboardButton(text="/echo"),
            KeyboardButton(text="/price"),
            KeyboardButton(text="/make_legal_contract"),
        ],

    ],
    resize_keyboard=True
)

units_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="м2."),
            KeyboardButton(text="шт."),
            KeyboardButton(text="кг."),

        ],

        [
            KeyboardButton(text="месяц."),
            KeyboardButton(text="час."),
            KeyboardButton(text="пог.м."),
        ],

    ],
    resize_keyboard=True
)

years = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=str(current_year)),
            KeyboardButton(text=str(current_year-1)),
            KeyboardButton(text=str(current_year-2)),

        ],

        [
            KeyboardButton(text=str(current_year-3)),
            KeyboardButton(text=str(current_year-4)),
            KeyboardButton(text=str(current_year-5)),
        ],

    ],
    resize_keyboard=True
)

months = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1"),
            KeyboardButton(text="2"),
            KeyboardButton(text="3"),

        ],

        [
            KeyboardButton(text="4"),
            KeyboardButton(text="5"),
            KeyboardButton(text="6"),
        ],
[
            KeyboardButton(text="7"),
            KeyboardButton(text="8"),
            KeyboardButton(text="9"),

        ],

        [
            KeyboardButton(text="10"),
            KeyboardButton(text="11"),
            KeyboardButton(text="12"),
        ],


    ],
    resize_keyboard=True
)

income_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Комплектация"),
            KeyboardButton(text="1й платёж дизайн проект"),
            KeyboardButton(text="2й платёж дизайн проект"),
            KeyboardButton(text="3й платёж дизайн проект"),

        ],

        [
            KeyboardButton(text="Итоговый платёж дизайн проект"),
            KeyboardButton(text="Авторский надзор"),
            KeyboardButton(text="Обмеры"),
            KeyboardButton(text="Фор-проект"),
        ],

        [
            KeyboardButton(text="Планировка"),
            KeyboardButton(text="Проект дома"),
            KeyboardButton(text="Реклама в Инстаграм"),
            KeyboardButton(text="Консультации"),
        ],

    ],
    resize_keyboard=True
)
