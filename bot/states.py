from aiogram.fsm.state import State, StatesGroup

class AIChat(StatesGroup):
    dialog = State()
