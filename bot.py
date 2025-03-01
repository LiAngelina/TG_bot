import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
)
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from weather import get_weather, get_available_cities
from api import TOKEN

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Начать"), KeyboardButton(text="Помощь")],
        [KeyboardButton(text="Погода"), KeyboardButton(text="Рандомное число")],
        [KeyboardButton(text="🇰🇿 Казахстан"), KeyboardButton(text="🇷🇺 Россия")]
    ],
    resize_keyboard=True
)

inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Начать", callback_data="start")],
        [InlineKeyboardButton(text="Помощь", callback_data="help")],
        [InlineKeyboardButton(text="Рандомное число", callback_data="random")],
        [InlineKeyboardButton(text="Погода", callback_data="weather")]
    ]
)

@dp.callback_query()
async def callback_handler(callback: types.CallbackQuery):
    if callback.data == "start":
        await start(callback.message)  
    elif callback.data == "help":
        await help_command(callback.message)  
    elif callback.data == "random":
        await random_command(callback.message)  
    elif callback.data == "weather":
        await weather_command(callback.message)  

cities = get_available_cities()
@dp.message(lambda message: message.text in sum(cities.values(), []))
async def send_weather(message: types.Message):
    city = message.text
    weather_info = await get_weather(city)
    await message.answer(weather_info)

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Я тестовый бот <b>test</b>", reply_markup=main_keyboard)

@dp.message(Command("random"))
async def random_command(message: types.Message):
    number = random.randint(1, 100)
    await message.answer(f"🎲 Случайное число: {number}")

@dp.message(Command("help"))
async def help_command(message: types.Message):
    command_text = (
        "📌 <b>Доступные команды:</b>\n"
        "/start - Начать работу с ботом\n"
        "/help - Показывает список команд\n"
        "/random - Случайное число\n"
        "/weather - Узнать погоду"
    )
    await message.answer(command_text)

@dp.message(Command("weather"))
async def weather_command(message: types.Message):
    weather_info = await get_weather()
    await message.answer(weather_info)

@dp.message(lambda message: message.text == "Начать")
async def start_button(message: types.Message):
    await start(message)

@dp.message(lambda message: message.text == "Помощь")
async def help_button(message: types.Message):
    await help_command(message)

@dp.message(lambda message: message.text == "Рандомное число")
async def random_button(message: types.Message):
    await random_command(message)

@dp.message(lambda message: message.text == "Погода")
async def weather_button(message: types.Message):
    await weather_command(message)

async def main():
    await dp.start_polling(bot)

# 📌 Клавиатуры для выбора города
cities = get_available_cities()

country_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🇰🇿 Казахстан"), KeyboardButton(text="🇷🇺 Россия")]
    ],
    resize_keyboard=True
)

kazakhstan_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=city) for city in cities["Казахстан"]],
        [KeyboardButton(text="⬅ Назад")]
    ],
    resize_keyboard=True
)

russia_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=city) for city in cities["Россия"]],
        [KeyboardButton(text="⬅ Назад")]
    ],
    resize_keyboard=True
)

# 📌 Обработчик выбора страны
@dp.message(lambda message: message.text in ["🇰🇿 Казахстан", "🇷🇺 Россия"])
async def select_country(message: types.Message):
    if message.text == "🇰🇿 Казахстан":
        await message.answer("🏙 Выберите город в Казахстане:", reply_markup=kazakhstan_keyboard)
    elif message.text == "🇷🇺 Россия":
        await message.answer("🏙 Выберите город в России:", reply_markup=russia_keyboard)

# 📌 Обработчик выбора города
@dp.message(lambda message: message.text in sum(cities.values(), []))
async def select_city(message: types.Message):
    city = message.text
    weather_info = await get_weather(city)
    await message.answer(weather_info, reply_markup=country_keyboard)

# 📌 Обработчик кнопки "⬅ Назад"
@dp.message(lambda message: message.text == "⬅ Назад")
async def go_back(message: types.Message):
    await message.answer("🔙 Выберите страну:", reply_markup=country_keyboard)

if __name__ == "__main__":
    asyncio.run(main())