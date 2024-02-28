from aiogram.dispatcher.filters.state import State, StatesGroup

# состояния регистрации пользователей
class ClientRegisterStates(StatesGroup):
    welcome = State()   # согласие на обработку
    name = State()      # ввод имени
    phone = State()     # передача контактных данных