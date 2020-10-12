from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Главное меню
key_profile = KeyboardButton("Мой кабинет")
key_categories = KeyboardButton("Категории")

key_back_main_menu = KeyboardButton("Назад в главное меню")
# Мой кабинет
key_history = KeyboardButton("История покупок")
key_replenish = KeyboardButton("Пополнить счет")

key_back_profile = KeyboardButton("Назад в мой кабинет")
# Категории
key_smart = KeyboardButton("Смартфоны")
key_tv = KeyboardButton("Телевизоры")

key_back_categories = KeyboardButton("Назад в категории")
# Смартфоны
key_item0 = KeyboardButton("!")
key_item1 = KeyboardButton("!")
key_item2 = KeyboardButton("!")
key_item3 = KeyboardButton("!")
key_item4 = KeyboardButton("!")

key_back_smart = KeyboardButton("Назад в смартфоны")
# Телевизоры
key_item5 = KeyboardButton("!")
key_item6 = KeyboardButton("!")
key_item7 = KeyboardButton("!")
key_item8 = KeyboardButton("!")
key_item9 = KeyboardButton("!")

key_back_tv = KeyboardButton("Назад в телевизоры")

key_buy = KeyboardButton("Купить")

start = ReplyKeyboardMarkup(resize_keyboard=True).row(key_categories, key_profile)

profile = ReplyKeyboardMarkup(resize_keyboard=True).row(key_history, key_replenish, key_back_main_menu)

history = ReplyKeyboardMarkup(resize_keyboard=True).row(key_back_profile)

replenish = ReplyKeyboardMarkup(resize_keyboard=True).row(key_back_profile)

categories = ReplyKeyboardMarkup(resize_keyboard=True).row(key_smart, key_tv, key_back_main_menu)
