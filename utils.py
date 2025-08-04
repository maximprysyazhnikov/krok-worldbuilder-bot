from aiogram.fsm.state import StatesGroup, State

class ChatStates(StatesGroup):
    ai_dialog = State()
    prompt_gen = State()
