from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from . import messages

# нижняя клавиатура с одной кнопкой
async def reply_kb_one(name):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                   one_time_keyboard=True)
    keyboard.add(name)
    return keyboard

# нижняя клавиатура с двумя кнопками
async def reply_kb_two(name_1, name_2):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                   one_time_keyboard=True)
    buttons = [name_1, name_2]
    keyboard.add(*buttons)
    return keyboard

# нижняя клавиатура, принимающая список кнопок
async def reply_kb_many(list_names: list):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                   one_time_keyboard=True)
    for name in list_names:
        keyboard.add(name)
    return keyboard

# нижняя клавиатура с кнопкой отправки контакта
async def reply_kb_contact(name):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                   one_time_keyboard=True)
    keyboard.add(KeyboardButton(text=name, request_contact=True))
    return keyboard

# нижняя клавиатура со списком городов
async def reply_kb_city(lang):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                   one_time_keyboard=True)
    if lang == "ru":
        for city in messages.CITIES_RU:
            keyboard.add(city)
    elif lang == "kz":
        for city in messages.CITIES_KZ:
            keyboard.add(city)
    return keyboard

# нижняя клавиатура со списком городов (с кнопкой "Назад")
async def reply_kb_city_change(lang):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                   one_time_keyboard=True)
    if lang == "ru":
        for city in messages.CITIES_RU:
            keyboard.add(city)
        keyboard.add(messages.BACK_RU)
    elif lang == "kz":
        for city in messages.CITIES_KZ:
            keyboard.add(city)
        keyboard.add(messages.BACK_KZ)
    return keyboard

# нижняя клавиатура с кнопками изменения пунктов каточки пользователя
async def reply_kb_change_info(names: list):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                   one_time_keyboard=True)
    for name in names:
        keyboard.add(name)
    return keyboard

# нижняя клавиатура с номерами элементов списка (начиная с 1)
# (pls нужен на случай использования метода single_lang в одном
# хендлере с double_lang)
async def reply_kb_list_numbers(names: list, pls: int = 0):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                   one_time_keyboard=True)
    for i in range(len(names) + pls):
        keyboard.add(f"{i+1}")
    keyboard.add(messages.BACK_RU)
    return keyboard

# инлайн клавиатура с одной кнопкой
async def inline_kb_one(name, callback):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(name, callback_data=callback))
    return keyboard

# инлайн клавиатура с двумя кнопками
async def inline_kb_two(name_1, name_2, callback1, callback2):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(name_1, callback_data=callback1))
    keyboard.add(InlineKeyboardButton(name_2, callback_data=callback2))
    return keyboard

# кнопка перехода по ссылке
async def inline_url_kb_one(name, url):
    button = InlineKeyboardButton(text=name, url=url)
    keyboard = InlineKeyboardMarkup()
    keyboard.add(button)
    return keyboard