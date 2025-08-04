from aiogram.fsm.state import StatesGroup, State

class ChatStates(StatesGroup):
    prompt_gen = State()
    ai_dialog = State()
