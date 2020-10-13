from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import CommandStart
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text

import Config
import keyboard

bot = Bot(token=Config.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

balance = 1000
history = []

samsung_galaxy_m51_price = 17999
samsung_galaxy_m31s_price = 7499
apple_iphone_se_price = 14499
huawei_p_smart_price = 6499
samsung_galaxy_s20_price = 17999

samsung_galaxy_m51_description = f"Samsung Galaxy S20 FE 6/128GB Cloud Mint \nЦена: {samsung_galaxy_m51_price}"
samsung_galaxy_m31s_description = f"Samsung Galaxy M31s 6/128GB Blue\nЦена: {samsung_galaxy_m31s_price}"
apple_iphone_se_description = f"Apple iPhone SE 64GB\n Цена: {apple_iphone_se_price}"
huawei_p_smart_description = f"Huawei P Smart 2021 128GB Black\n Цена: {huawei_p_smart_price}"
samsung_galaxy_s20_description = f"Samsung Galaxy S20 FE 6/128GB Cloud Mint\n Цена: {samsung_galaxy_s20_price}"


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


@dp.message_handler(Text(equals="Баланс"))
async def show_balance(message: types.Message):
    await user_profile(message)


@dp.message_handler(Text(equals="История покупок"))
async def shopping_history(message: types.Message):
    await message.answer("Добро пожаловать в историю покупок", reply_markup=keyboard.history)
    if len(history) > 0:
        for i in history:
            await message.answer(f"{i}\n", reply_markup=keyboard.history)
    else:
        await message.answer("Вы еще ничего не купили", reply_markup=keyboard.history)


@dp.message_handler(Text(equals="Пополнить счет"))
async def replenish_account(message: types.Message):
    await message.answer("На сколько вы хотите пополниь счет?", reply_markup=keyboard.inline_replenish)


@dp.callback_query_handler(lambda c: c.data == 'replenish_1000')
async def replenish_1000(callback_query: types.CallbackQuery):
    global balance
    balance = balance + 1000


@dp.callback_query_handler(lambda c: c.data == 'replenish_2000')
async def replenish_2000(callback_query: types.CallbackQuery):
    global balance
    balance = balance + 2000


@dp.callback_query_handler(lambda c: c.data == 'replenish_5000')
async def replenish_5000(callback_query: types.CallbackQuery):
    global balance
    balance = balance + 5000


@dp.callback_query_handler(lambda c: c.data == 'replenish_10000')
async def replenish_10000(callback_query: types.CallbackQuery):
    global balance
    balance = balance + 10000


@dp.callback_query_handler(lambda c: c.data == 'replenish_20000')
async def replenish_20000(callback_query: types.CallbackQuery):
    global balance
    balance = balance + 20000


@dp.message_handler(Text(equals="Каталог"))
async def catalogue(message: types.Message):
    await message.answer("Добро пожаловать в каталог", reply_markup=keyboard.catalogue)

    # https://rozetka.com.ua/samsung_galaxy_m51_6_128gb_black/p249014389/
    samsung_galaxy_m51_media_group = types.MediaGroup()
    samsung_galaxy_m51_media_group.attach_photo(
        "https://i8.rozetka.ua/goods/19989802/samsung_sm_g780fzgdsek_images_19989802046.jpg")
    samsung_galaxy_m51_media_group.attach_photo(
        "https://i2.rozetka.ua/goods/19989802/samsung_sm_g780fzgdsek_images_19989802306.jpg")
    samsung_galaxy_m51_media_group.attach_photo(
        "https://i8.rozetka.ua/goods/19989802/samsung_sm_g780fzgdsek_images_19989802736.jpg")
    samsung_galaxy_m51_media_group.attach_photo(
        "https://i8.rozetka.ua/goods/19989801/samsung_sm_g780fzgdsek_images_19989801851.jpg")
    samsung_galaxy_m51_media_group.attach_photo(
        "https://i8.rozetka.ua/goods/19989802/samsung_sm_g780fzgdsek_images_19989802516.jpg")
    await message.answer_media_group(samsung_galaxy_m51_media_group)
    await message.answer(samsung_galaxy_m51_description, reply_markup=keyboard.inline_item0)

    # https://rozetka.com.ua/samsung_sm_m317fzbnsek/p244007101/
    samsung_galaxy_m31s_media_group = types.MediaGroup()
    samsung_galaxy_m31s_media_group.attach_photo(
        "https://i2.rozetka.ua/goods/19702495/samsung_sm_m317fzbnsek_images_19702495075.jpg")
    samsung_galaxy_m31s_media_group.attach_photo(
        "https://i2.rozetka.ua/goods/19702494/samsung_sm_m317fzbnsek_images_19702494115.jpg")
    samsung_galaxy_m31s_media_group.attach_photo(
        "https://i8.rozetka.ua/goods/19702492/samsung_sm_m317fzbnsek_images_19702492909.jpg")
    samsung_galaxy_m31s_media_group.attach_photo(
        "https://i8.rozetka.ua/goods/19702493/samsung_sm_m317fzbnsek_images_19702493341.jpg")
    await message.answer_media_group(samsung_galaxy_m31s_media_group)
    await message.answer(samsung_galaxy_m31s_description, reply_markup=keyboard.inline_item1)

    # https://rozetka.com.ua/apple_iphone_se_64gb_white/p205228429/
    apple_iphone_se_media_group = types.MediaGroup()
    apple_iphone_se_media_group.attach_photo(
        "https://i8.rozetka.ua/goods/17801797/apple_iphone_se_64gb_white_images_17801797603.png")
    apple_iphone_se_media_group.attach_photo(
        "https://i8.rozetka.ua/goods/17831432/apple_iphone_se_64gb_white_images_17831432701.jpg")
    apple_iphone_se_media_group.attach_photo(
        "https://i8.rozetka.ua/goods/17831434/apple_iphone_se_64gb_white_images_17831434045.jpg")
    apple_iphone_se_media_group.attach_photo(
        "https://i2.rozetka.ua/goods/17831429/apple_iphone_se_64gb_white_images_17831429131.jpg")
    apple_iphone_se_media_group.attach_photo(
        "https://i2.rozetka.ua/goods/17831436/apple_iphone_se_64gb_white_images_17831436709.jpg")
    apple_iphone_se_media_group.attach_photo(
        "https://i8.rozetka.ua/goods/17831427/apple_iphone_se_64gb_white_images_17831427877.jpg")
    apple_iphone_se_media_group.attach_photo(
        "https://i2.rozetka.ua/goods/17831432/apple_iphone_se_64gb_white_images_17831432125.jpg")
    await message.answer_media_group(apple_iphone_se_media_group)
    await message.answer(apple_iphone_se_description, reply_markup=keyboard.inline_item2)

    # https://rozetka.com.ua/huawei_p_smart_2021_128gb_black/p252147366/
    huawei_p_smart_media_group = types.MediaGroup()
    huawei_p_smart_media_group.attach_photo(
        "https://i2.rozetka.ua/goods/20187715/huawei_p_smart_2021_128gb_black_images_20187715121.jpg")
    huawei_p_smart_media_group.attach_photo(
        "https://i2.rozetka.ua/goods/20187743/huawei_p_smart_2021_128gb_black_images_20187743841.jpg")
    huawei_p_smart_media_group.attach_photo(
        "https://i2.rozetka.ua/goods/20187728/huawei_p_smart_2021_128gb_black_images_20187728886.jpg")
    huawei_p_smart_media_group.attach_photo(
        "https://i2.rozetka.ua/goods/20187752/huawei_p_smart_2021_128gb_black_images_20187752871.jpg")
    huawei_p_smart_media_group.attach_photo(
        "https://i8.rozetka.ua/goods/20187756/huawei_p_smart_2021_128gb_black_images_20187756911.jpg")
    huawei_p_smart_media_group.attach_photo(
        "https://i2.rozetka.ua/goods/20187709/huawei_p_smart_2021_128gb_black_images_20187709626.jpg")
    huawei_p_smart_media_group.attach_photo(
        "https://i2.rozetka.ua/goods/20187761/huawei_p_smart_2021_128gb_black_images_20187761041.jpg")
    huawei_p_smart_media_group.attach_photo(
        "https://i8.rozetka.ua/goods/20187733/huawei_p_smart_2021_128gb_black_images_20187733786.jpg")
    huawei_p_smart_media_group.attach_photo(
        "https://i2.rozetka.ua/goods/20187738/huawei_p_smart_2021_128gb_black_images_20187738896.jpg")
    await message.answer_media_group(huawei_p_smart_media_group)
    await message.answer(huawei_p_smart_description, reply_markup=keyboard.inline_item3)

    # https://rozetka.com.ua/samsung_sm_g780fzgdsek/p250212126/
    samsung_galaxy_s20_media_group = types.MediaGroup()
    samsung_galaxy_s20_media_group.attach_photo(
        "https://i8.rozetka.ua/goods/19989802/samsung_sm_g780fzgdsek_images_19989802046.jpg")
    samsung_galaxy_s20_media_group.attach_photo(
        "https://i2.rozetka.ua/goods/19989802/samsung_sm_g780fzgdsek_images_19989802306.jpg")
    samsung_galaxy_s20_media_group.attach_photo(
        "https://i8.rozetka.ua/goods/19989802/samsung_sm_g780fzgdsek_images_19989802736.jpg")
    samsung_galaxy_s20_media_group.attach_photo(
        "https://i8.rozetka.ua/goods/19989801/samsung_sm_g780fzgdsek_images_19989801851.jpg")
    samsung_galaxy_s20_media_group.attach_photo(
        "https://i8.rozetka.ua/goods/19989802/samsung_sm_g780fzgdsek_images_19989802516.jpg")
    await message.answer_media_group(samsung_galaxy_s20_media_group)
    await message.answer(samsung_galaxy_s20_description, reply_markup=keyboard.inline_item4)


@dp.callback_query_handler(lambda c: c.data == 'item0')
async def byu_item0(callback_query: types.CallbackQuery):
    global history, balance
    if balance > samsung_galaxy_m51_price:
        history.append(samsung_galaxy_m51_description)
        balance = balance - samsung_galaxy_m51_price
    else:
        await callback_query.answer("Недостаточно средств, пополните счет пожалуйста")


@dp.callback_query_handler(lambda c: c.data == 'item1')
async def byu_item1(callback_query: types.CallbackQuery):
    global history, balance
    if balance > samsung_galaxy_m31s_price:
        history.append(samsung_galaxy_m31s_description)
        balance = balance - samsung_galaxy_m31s_price
    else:
        await callback_query.answer("Недостаточно средств, пополните счет пожалуйста")


@dp.callback_query_handler(lambda c: c.data == 'item2')
async def byu_item2(callback_query: types.CallbackQuery):
    global history, balance
    if balance > apple_iphone_se_price:
        history.append(apple_iphone_se_description)
        balance = balance - apple_iphone_se_price
    else:
        await callback_query.answer("Недостаточно средств, пополните счет пожалуйста")


@dp.callback_query_handler(lambda c: c.data == 'item3')
async def byu_item3(callback_query: types.CallbackQuery):
    global history, balance
    if balance > huawei_p_smart_price:
        history.append(huawei_p_smart_description)
        balance = balance - huawei_p_smart_price
    else:
        await callback_query.answer("Недостаточно средств, пополните счет пожалуйста")


@dp.callback_query_handler(lambda c: c.data == 'item4')
async def byu_item4(callback_query: types.CallbackQuery):
    global history, balance
    if balance > samsung_galaxy_s20_price:
        history.append(samsung_galaxy_s20_description)
        balance = balance - samsung_galaxy_s20_price
    else:
        await callback_query.answer("Недостаточно средств, пополните счет пожалуйста")


if __name__ == '__main__':
    executor.start_polling(dp)
