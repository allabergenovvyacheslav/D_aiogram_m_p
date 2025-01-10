# -*- coding: utf-8 -*-

from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

start_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📝 Прайс-лист на паркет"),
            KeyboardButton(text="ℹ️ О компании Мир паркета")
        ],
        [
            KeyboardButton(text='📝 Прайс-лист на услуги'),
            KeyboardButton(text="📝 Наши работы")
        ]
    ], resize_keyboard=True
)

catalog_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Штучный паркет дуб радиал",
                                 callback_data='parquet_flooring_RS')
        ],
        [
            InlineKeyboardButton(text="Штучный паркет дуб селект",
                                 callback_data='parquet_flooring_S')
        ],
        [
            InlineKeyboardButton(text="Штучный паркет дуб натур",
                                 callback_data='parquet_flooring_N')
        ],
        [
            InlineKeyboardButton(text="Штучный паркет дуб рустик",
                                 callback_data='parquet_flooring_R')
        ],
        [
            InlineKeyboardButton(text="Широкоформатный паркет дуб радиал",
                                 callback_data='large_format_parquet_RS')
        ],
        [
            InlineKeyboardButton(text="Широкоформатный паркет дуб селект",
                                 callback_data='large_format_parquet_S')
        ],
        [
            InlineKeyboardButton(text="Широкоформатный паркет дуб натур",
                                 callback_data='large_format_parquet_N')
        ],
        [
            InlineKeyboardButton(text="Широкоформатный паркет дуб рустик",
                                 callback_data='large_format_parquet_R')
        ],
        [
            InlineKeyboardButton(text="Массивная доска дуб селект",
                                 callback_data='solid_wood_parquet_S')
        ],
        [
            InlineKeyboardButton(text="Массивная доска дуб натур",
                                 callback_data='solid_wood_parquet_N')
        ],
        [
            InlineKeyboardButton(text="Массивная доска дуб рустик",
                                 callback_data='solid_wood_parquet_R')
        ],
        [
            InlineKeyboardButton(text="Другие предложения", callback_data='other')
        ]
    ]
)

works_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Настил фанеры", callback_data="fanera_works")],
        [InlineKeyboardButton(text="Укладка паркета", callback_data="parquet_works")],
        [InlineKeyboardButton(text="Финишная отделка", callback_data="otdelka_works")]
    ]
)

order_work_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🛍 Заказать",
                              url="https://uslugi.yandex.ru/profile/MirParketa-904060?action=addReview")],
        [InlineKeyboardButton(text="🔙 Назад",
                              callback_data="back_to_works")]
    ]
)

buy_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='🛍 Купить', url='https://mir-parketa-naberezhnaja-reki-fontanki.clients.site/')],
        [InlineKeyboardButton(text='🔙 Назад', callback_data='back_to_catalog')]
    ]
)

AdminPanel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👥 Пользователи", callback_data="users"),
        ],
        [
            InlineKeyboardButton(text="📊 Статистика", callback_data="statistick"),
        ],
        [
            InlineKeyboardButton(text="✉️ Рассылка", callback_data="mailing"),
        ],
        [
            InlineKeyboardButton(text="❌ Блокировка", callback_data="block"),
        ],
    ]
)

back_to_admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_admin"),
        ],
    ]
)
