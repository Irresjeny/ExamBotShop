from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import CommandStart
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text

import Config
import keyboard

balance = 1000

bot = Bot(token=Config.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Здравствуйте, {message.from_user.first_name}", reply_markup=keyboard.start)


@dp.message_handler(Text(equals="Назад в главное меню"))
async def back_main_menu(message: types.Message):
    await bot_start(message)


@dp.message_handler(Text(equals="Мой кабинет"))
async def user_profile(message: types.Message):
    await message.answer(f"Ваш баланс: {balance}", reply_markup=keyboard.profile)


@dp.message_handler(Text(equals="Назад в мой кабинет"))
async def back_profile(message: types.Message):
    await user_profile(message)


@dp.message_handler(Text(equals="История покупок"))
async def shopping_history(message: types.Message):
    await message.answer("!", reply_markup=keyboard.history)


@dp.message_handler(Text(equals="Пополнить счет"))
async def replenish_account(message: types.Message):
    await message.answer("!", reply_markup=keyboard.replenish)


if __name__ == '__main__':
    executor.start_polling(dp)
