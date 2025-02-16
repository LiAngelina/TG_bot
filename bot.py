import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import(ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from api import TOKEN

#Создание объектов: бот и диспетчер
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()

#Основная клавиатура
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Hi!🖐"), KeyboardButton(text="Помощь")]
    ],
    resize_keyboard=True
)

#Инлайн клавиатура
inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Перейти на сайт", url="http://example.com")],
        [InlineKeyboardButton(text="Нажми", callback_data="button_click")]
    ]
)

@dp.message(Command("start"))
async def start(message: types.Message):
        await message.answer("Hi! Я тестовый бот <b>тест</b>", reply_markup=main_keyboard)

@dp.message(lambda message: message.text == "Привет!")
async def hello(message: types.Message):
        await message.answer("Hi! Как дела? 🤭", reply_markup=inline_keyboard)

async def main():
        await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
