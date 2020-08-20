from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from data import constants

lang = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=constants.Uz),
            KeyboardButton(text=constants.Ru)
        ],
    ],
    resize_keyboard=True
)

share_number_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Telefon raqamni ulashish", request_contact=True),
        ],
    ],
    resize_keyboard=True
)

share_number_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Поделиться контактом", request_contact=True),
        ],
    ],
    resize_keyboard=True
)

regions_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Toshkent"),
            KeyboardButton(text="Andijon viloyati")
        ],
        [
            KeyboardButton(text="Namangan viloyati"),
            KeyboardButton(text="Farg\'ona viloyati")
        ],
        [
            KeyboardButton(text="Sirdaryo viloyati"),
            KeyboardButton(text="Jizzax viloyati")
        ],
        [
            KeyboardButton(text="Samarqand viloyati"),
            KeyboardButton(text="Buxoro viloyati")
        ],
        [
            KeyboardButton(text="Navoiy viloyati"),
            KeyboardButton(text="Qashqadaryo viloyati")
        ],
        [
            KeyboardButton(text="Surxondaryo viloyati"),
            KeyboardButton(text="Xorazm viloyati")
        ],
    ],
    resize_keyboard=True
)

regions_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ташкент"),
            KeyboardButton(text="Андижанская область")
        ],
        [
            KeyboardButton(text="Наманганская область"),
            KeyboardButton(text="Ферганская область")
        ],
        [
            KeyboardButton(text="Сырдарьинская область"),
            KeyboardButton(text="Джизакская область")
        ],
        [
            KeyboardButton(text="Самаркандская область"),
            KeyboardButton(text="Бухарская область")
        ],
        [
            KeyboardButton(text="Навоийская область"),
            KeyboardButton(text="Кашкадарьинская область")
        ],
        [
            KeyboardButton(text="Сурхандарьинская область"),
            KeyboardButton(text="Хорезмская область")
        ],
    ],
    resize_keyboard=True
)

money_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ha"),
            KeyboardButton(text="Yo\'q")
        ],
    ],
    resize_keyboard=True
)

money_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Да"),
            KeyboardButton(text="Нет")
        ],
    ],
    resize_keyboard=True
)

restart_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=constants.restart_uz)
        ],
    ],
    resize_keyboard=True
)

restart_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=constants.restart_ru)
        ],
    ],
    resize_keyboard=True
)