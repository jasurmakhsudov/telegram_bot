from aiogram.dispatcher.filters.state import StatesGroup, State


class States(StatesGroup):
    Language = State()
    Number = State()
    Region = State()
    Money = State()
    Feedback = State()
