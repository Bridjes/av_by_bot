from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from .app import dp, bot
from . import keyboards, messages
from .states import ClientRegisterStates
from .data_fetcher import *
from .service_functions import generate_password
from .local_settings import *


# согласие на обработку данных
@dp.message_handler(commands=['start'], state='*')
async def send_welcome(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        # получили код из аргумента в ссылке по которой перешёл пользак и нажал кнопку start
        # tg://resolve?domain=shajtanas_bot&start=12345
        # пытаемся сначала найти код в JSON-Storage, если там нет, то из аргумента
        code = data.get('user_id', message.get_args())

        if (not code):
            await message.answer(messages.WELCOME_ERROR,
                                 reply_markup=await keyboards.reply_kb_one(messages.START))
            return

        data["user_id"] = code

        # установили состояние welcome
        await ClientRegisterStates.welcome.set()

        await message.answer(messages.WELCOME_MESSAGE,
                             reply_markup=await keyboards.reply_kb_two(messages.AGREEMENT,
                                                                       messages.DENIAL))

# согласие на обработку данных (дубль для умников, нажавших кнопку НЕТ)
@dp.message_handler(Text(equals=messages.DENIAL), state=ClientRegisterStates.welcome)
async def denial(message: types, state: FSMContext):
    await message.answer(messages.AGREEMENT_NO,
                         reply_markup=await keyboards.reply_kb_one(messages.START))

# согласие на обработку данных и запрос контактных данных
@dp.message_handler(Text(equals=messages.AGREEMENT), state=ClientRegisterStates.welcome)
async def send_agreement_yes(message: types, state: FSMContext):
    # установили состояние register
    await ClientRegisterStates.phone.set()

    msg = await message.answer(messages.USER_PHONE,
                               reply_markup=await keyboards.reply_kb_contact(messages.USER_PHONE_SEND))

# считывание номера телефона и имена с карточки контакта
@dp.message_handler(content_types=['contact'], state=ClientRegisterStates.phone)
async def get_phone(message: types, state: FSMContext):
    async with state.proxy() as data:
        # Если присланный объект contact не равен None
        if message.contact is not None:
            phone = message.contact.phone_number
            telegram_id = message["from"]["id"]
            password = generate_password(8)
            username = message["from"]["username"]
            # если username не указан, берём имя пользователя
            username = username if username else message["from"]["first_name"]

            # получение токена доступа
            bot_user = {
                "username": f"{BOT_USERNAME}",
                "password": f"{BOT_PASSWORD}"
            }
            response = await get_access(bot_user)
            access = response["access"]     # access-token

            # упаковка инфы о пользаке для отправки на бекенд
            payload = {
                "phone": f"{phone}".replace("+", ""),     # вырезали + из номера
                "telegram_id": f"{telegram_id}",
                "password": f"{password}"
            }

            headers = {
                "Authorization": f"Bearer {access}"
            }

            user_id = data['user_id']

            # POST-запрос с получением статус-кода
            status_code = await user_update(payload,
                                            pk=user_id,
                                            headers=headers)

            url = f"{DOMAIN_FRONT}"

            msg = await message.answer(f"{messages.SUCCESS_AUTH}")
