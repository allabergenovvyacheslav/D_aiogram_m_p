# -*- coding: utf-8 -*-

from aiogram.types import InputMediaPhoto

import texts.category
from keyboards import *


async def price_parquet(message):
    with open('files/media/category.png', "rb") as img:
        await message.answer_photo(img, '<b>Выберите позицию из прайса</b>', parse_mode='HTML', reply_markup=catalog_kb)


async def buy_parquet_flooring_RS(call):
    with open('files/media/radial.jpeg', 'rb') as img:
        mes = InputMediaPhoto(media=img, caption=texts.category.parquet_flooring_RS, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=buy_kb)
    await call.answer()


async def buy_large_format_parquet_RS(call):
    with open('files/media/radial.jpeg', 'rb') as img:
        mes = InputMediaPhoto(media=img, caption=texts.category.large_format_parquet_RS, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=buy_kb)
    await call.answer()


async def buy_parquet_flooring_S(call):
    with open('files/media/select.jpeg', 'rb') as img:
        mes = InputMediaPhoto(media=img, caption=texts.category.parquet_flooring_S, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=buy_kb)
    await call.answer()


async def buy_large_format_parquet_S(call):
    with open('files/media/large_S.jpg', 'rb') as img:
        mes = InputMediaPhoto(media=img, caption=texts.category.large_format_parquet_S, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=buy_kb)
    await call.answer()


async def buy_solid_wood_parquet_S(call):
    with open('files/media/solid_S.jpg', 'rb') as img:
        mes = InputMediaPhoto(media=img, caption=texts.category.solid_wood_parquet_S, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=buy_kb)
    await call.answer()


async def buy_parquet_flooring_N(call):
    with open('files/media/natur.jpeg', 'rb') as img:
        mes = InputMediaPhoto(media=img, caption=texts.category.parquet_flooring_N, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=buy_kb)
    await call.answer()


async def buy_large_format_parquet_N(call):
    with open('files/media/large_N.jpg', 'rb') as img:
        mes = InputMediaPhoto(media=img, caption=texts.category.large_format_parquet_N, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=buy_kb)
    await call.answer()


async def buy_solid_wood_parquet_N(call):
    with open('files/media/solid_N.jpg', 'rb') as img:
        mes = InputMediaPhoto(media=img, caption=texts.category.solid_wood_parquet_N, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=buy_kb)
    await call.answer()


async def buy_parquet_flooring_R(call):
    with open('files/media/rustic.jpeg', 'rb') as img:
        mes = InputMediaPhoto(media=img, caption=texts.category.parquet_flooring_R, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=buy_kb)
    await call.answer()


async def buy_large_format_parquet_R(call):
    with open('files/media/large_Rust.jpg', 'rb') as img:
        mes = InputMediaPhoto(media=img, caption=texts.category.large_format_parquet_R, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=buy_kb)
    await call.answer()


async def buy_solid_wood_parquet_R(call):
    with open('files/media/solid_Rust.jpg', 'rb') as img:
        mes = InputMediaPhoto(media=img, caption=texts.category.solid_wood_parquet_R, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=buy_kb)
    await call.answer()


async def buy_other(call):
    with open('files/media/other.jpg', 'rb') as img:
        mes = InputMediaPhoto(media=img, caption=texts.category.other, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=buy_kb)
    await call.answer()


async def cmd_back_price(call):
    with open('files/media/category.png', "rb") as img:
        mes = InputMediaPhoto(media=img, caption='<b>Выберите позицию из прайса</b>', parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=catalog_kb)
    await call.answer()


async def price_works(message):
    with open('files/media/rabota.png', 'rb') as img:
        await message.answer_photo(img, '<b>Основные этапы комплекса работ</b>', parse_mode='HTML',
                                   reply_markup=works_kb)


async def fanera_work(call):
    with open("files/media/fanera.jpg", "rb") as img:
        mes = InputMediaPhoto(media=img, caption=texts.category.fanera_works, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=order_work_kb)


async def parquet_work(call):
    with open("files/media/parquet_works.jpg", "rb") as img:
        mes = InputMediaPhoto(media=img, caption=texts.category.parquet_works, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=order_work_kb)


async def otdelka_work(call):
    with open("files/media/otdelka_works.jpg", "rb") as img:
        mes = InputMediaPhoto(media=img, caption=texts.category.otdelka_works, parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=order_work_kb)


async def cmd_back_work(call):
    with open('files/media/rabota.png', 'rb') as img:
        mes = InputMediaPhoto(media=img, caption='<b>Основные этапы комплекса работ</b>', parse_mode='HTML')
        await call.message.edit_media(mes, reply_markup=works_kb)
    await call.answer()


async def show_work(message):
    for x in range(1, 14):
        with open(f'files_2/{x}.jpg', 'rb') as img:
            await message.answer_photo(img, texts.category.show_work, reply_markup=start_kb)
