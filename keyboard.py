from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

# Главное меню
key_profile = KeyboardButton("Мой кабинет")
key_catalogue = KeyboardButton("Каталог")

key_back_main_menu = KeyboardButton("Назад в главное меню")
# Мой кабинет
key_history = KeyboardButton("История покупок")
key_replenish = KeyboardButton("Пополнить счет")
key_balance = KeyboardButton("Баланс")

inline_key_replenish_1000 = InlineKeyboardButton("1000", callback_data="replenish_1000")
inline_key_replenish_2000 = InlineKeyboardButton("2000", callback_data="replenish_2000")
inline_key_replenish_5000 = InlineKeyboardButton("5000", callback_data="replenish_5000")
inline_key_replenish_10000 = InlineKeyboardButton("10000", callback_data="replenish_10000")
inline_key_replenish_20000 = InlineKeyboardButton("20000", callback_data="replenish_20000")

key_back_profile = KeyboardButton("Назад в мой кабинет")
# Каталог
inline_key_item0 = InlineKeyboardButton("Купить", callback_data="item0")
inline_key_item1 = InlineKeyboardButton("Купить", callback_data="item1")
inline_key_item2 = InlineKeyboardButton("Купить", callback_data="item2")
inline_key_item3 = InlineKeyboardButton("Купить", callback_data="item3")
inline_key_item4 = InlineKeyboardButton("Купить", callback_data="item4")


start = ReplyKeyboardMarkup(resize_keyboard=True).row(key_catalogue, key_profile)

profile = ReplyKeyboardMarkup(resize_keyboard=True).row(key_balance, key_history, key_replenish, key_back_main_menu)

history = ReplyKeyboardMarkup(resize_keyboard=True).row(key_back_profile)

replenish = ReplyKeyboardMarkup(resize_keyboard=True).row(key_back_profile)

catalogue = ReplyKeyboardMarkup(resize_keyboard=True).row(key_back_main_menu)

inline_replenish = InlineKeyboardMarkup(row_width=1).add(inline_key_replenish_1000, inline_key_replenish_2000,
                                                         inline_key_replenish_5000, inline_key_replenish_10000,
                                                         inline_key_replenish_20000)

inline_item0 = InlineKeyboardMarkup(row_width=1).add(inline_key_item0)
inline_item1 = InlineKeyboardMarkup(row_width=1).add(inline_key_item1)
inline_item2 = InlineKeyboardMarkup(row_width=1).add(inline_key_item2)
inline_item3 = InlineKeyboardMarkup(row_width=1).add(inline_key_item3)
inline_item4 = InlineKeyboardMarkup(row_width=1).add(inline_key_item4)



