# -*- coding: utf-8 -*-

import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text

import config
import database
import handlers.Start
import handlers.Category
import handlers.Admin

logging.basicConfig(level=logging.INFO)
api = config.API
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


dp.message_handler(lambda m: database.check_block(m.from_user.id))(handlers.Start.ban_message)
dp.callback_query_handler(lambda c: database.check_block(c.from_user.id))(handlers.Start.ban_callbackquery)

dp.message_handler(commands=['start'])(handlers.Start.start)
dp.message_handler(Text(equals=['ℹ️ О компании Мир паркета']))(handlers.Start.about_as)

dp.message_handler(commands=['admin'])(handlers.Admin.start)
dp.callback_query_handler(text="statistick")(handlers.Admin.statistick)
dp.callback_query_handler(text="users")(handlers.Admin.users)
dp.callback_query_handler(text="mailing")(handlers.Admin.mailing)
dp.message_handler(state=handlers.Admin.admins.mailing_step1)(handlers.Admin.mailing1)
dp.message_handler(content_types=types.ContentTypes.PHOTO,
                   state=handlers.Admin.admins.mailing_step2)(handlers.Admin.mailing2)
dp.callback_query_handler(text="block")(handlers.Admin.block)
dp.message_handler(state=handlers.Admin.admins.ban)(handlers.Admin.ban1)
dp.callback_query_handler(text="back_to_admin")(handlers.Admin.back_admin)

dp.message_handler(Text(equals=['📝 Прайс-лист на паркет']))(handlers.Category.price_parquet)
dp.callback_query_handler(text='parquet_flooring_RS')(handlers.Category.buy_parquet_flooring_R)
dp.callback_query_handler(text='parquet_flooring_S')(handlers.Category.buy_parquet_flooring_S)
dp.callback_query_handler(text='parquet_flooring_N')(handlers.Category.buy_parquet_flooring_N)
dp.callback_query_handler(text='parquet_flooring_R')(handlers.Category.buy_parquet_flooring_R)
dp.callback_query_handler(text='large_format_parquet_RS')(handlers.Category.buy_large_format_parquet_RS)
dp.callback_query_handler(text='large_format_parquet_S')(handlers.Category.buy_large_format_parquet_S)
dp.callback_query_handler(text='large_format_parquet_N')(handlers.Category.buy_large_format_parquet_N)
dp.callback_query_handler(text='large_format_parquet_R')(handlers.Category.buy_large_format_parquet_R)
dp.callback_query_handler(text='solid_wood_parquet_S')(handlers.Category.buy_solid_wood_parquet_S)
dp.callback_query_handler(text='solid_wood_parquet_N')(handlers.Category.buy_solid_wood_parquet_N)
dp.callback_query_handler(text='solid_wood_parquet_R')(handlers.Category.buy_solid_wood_parquet_R)
dp.callback_query_handler(text='other')(handlers.Category.buy_other)
dp.callback_query_handler(text='back_to_catalog')(handlers.Category.cmd_back_price)

dp.message_handler(Text(equals=['📝 Прайс-лист на услуги']))(handlers.Category.price_works)
dp.callback_query_handler(text='fanera_works')(handlers.Category.fanera_work)
dp.callback_query_handler(text='parquet_works')(handlers.Category.parquet_work)
dp.callback_query_handler(text='otdelka_works')(handlers.Category.otdelka_work)
dp.callback_query_handler(text='back_to_works')(handlers.Category.cmd_back_work)

dp.message_handler(Text(equals=['📝 Наши работы']))(handlers.Category.show_work)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
