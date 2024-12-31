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
import hand.keyboard1 as kb


router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(f"Привет,{html.bold(html.quote(message.from_user.full_name))}. Рады тебя видеть. И сразу 300 бонусов за регистрацию карты Друга P2P. Круто? Круто!", 
                         parse_mode = ParseMode.HTML)

@router.message(Command('home'))
async def cmd_home(message:types.Message):
    await message.answer("Привет, это Ровесник! Меню управления ⬇️",reply_markup=kb.builder.as_markup)

@router.message(F.text.lower() == "меню")
async def menu(message: types.Message):
    await message.answer("Отличный выбор!")

@router.message(F.text.lower() == "написать отзыв")
async def review(message: types.Message):
    await message.answer("Вы уже оставили максимальное количество отзывов за период")

@router.message(F.text.lower() == 'faq')
async def faq(message: types.Message):
    await message.answer("FAQ")
    await message.answer("Мы находимся по адресу:"
+"\n" +

"Малый Гнездниковский переулок, 9с2" +"\n" + "\n" +

"Время работы:" +"\n" +
"вс-чт 12:00–00:00" +"\n" +
"пт-сб 12:00–06:00"+ "\n" +"\n" + 

"Узнать о ближайших ивентах и вечеринках можно в разделе «Мероприятия», а более подробной информацией делимся в нашем телеграм-канале <a href='https://t.me/rovesnikbar'>ссылку</a> и <a href='https://www.instagram.com/rovesnik.bar/'>ссылку</a>инстаграме *."+ "\n" +"\n" +

"А если хотите связаться с нами, позвоните нам по номеру телефона — +7 (999) 912-72-85."+ "\n"+"\n" +

"*признан в России экстремистской организацией 🤠")

@router.message(F.text.lower() == "забронировать")
async def bron(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="Да"),types.KeyboardButton(text = "Нет"))
    builder.row(types.KeyboardButton(text="Назад"))
    await message.answer("",reply_markup=builder.as_markup(resize_keyboard=True))

@router.message(F.text.lower() == "программа лояльности")
async def loyal(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Моя карта",
        callback_data="random_value")
    )
    await message.answer(
        "Чтобы воспользоваться картой лояльности, нажмите здесь",
        reply_markup=builder.as_markup()
    )

@router.message(F.text.lower() == 'вакансии')
async def vocancy(message: types.message):
    await message.answer("Вакансии",reply_markup = kb.settings)

@router.message(F.text.lower() == 'вк')
async def vocancy(message: types.message):
    await message.answer("ВК",reply_markup = kb.vkapp)