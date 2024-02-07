from aiogram.dispatcher.filters.state import StatesGroup, State


class LidsStates(StatesGroup):
    INPUT_NAME = State()
    INPUT_EMAIL = State()
    INPUT_PHONE = State()
    INPUT_AREA = State()
    INPUT_DESCRIPTION = State()
    INPUT_SOURCE = State()
    INPUT_CITY = State()
    INPUT_SERVICE = State()
    INPUT_PRICE = State()
    INPUT_IS_NEW = State()
    FINAL = State()
