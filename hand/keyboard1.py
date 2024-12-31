from aiogram.types.web_app_info import WebAppInfo
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandStart
from aiogram import html
from aiogram import F
from aiohttp.web import run_app
from aiohttp.web_app import Application
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Router
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

builder = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Меню"),
            KeyboardButton(text="Программа лояльности")],[KeyboardButton(text="Написать отзыв"),
            KeyboardButton(text="Забронировать")],[KeyboardButton(text="Мои купоны"),
            KeyboardButton(text="Мои брони"),
            KeyboardButton(text="Мои билеты")],[KeyboardButton(text="Мероприятия"),
            KeyboardButton(text="Вакансии"),
            KeyboardButton(text="FAQ")]],resize_keyboard=True)

settings = InlineKeyboardMarkup (inline_keyboard=[[InlineKeyboardButton(text ='воу воу воу', url = 'https://vk.com/soebre')]])

vkapp = InlineKeyboardMarkup (inline_keyboard=[[InlineKeyboardButton(text ='магазин', web_app =WebAppInfo(url =f'https://mech.moscow'))]])