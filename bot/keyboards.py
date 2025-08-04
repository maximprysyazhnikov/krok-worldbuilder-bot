from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_lang_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Українська"), KeyboardButton(text="English")]
        ],
        resize_keyboard=True
    )

def get_main_menu_keyboard(lang="uk"):
    if lang == "en":
        return ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Factions"), KeyboardButton(text="Continents")],
                [KeyboardButton(text="Characters")],
                [KeyboardButton(text="Create prompt")],
                [KeyboardButton(text="Discuss the world with AI")],
                [KeyboardButton(text="About bot")],
                [KeyboardButton(text="Restart")],
            ],
            resize_keyboard=True
        )
    else:
        return ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Фракції"), KeyboardButton(text="Континенти")],
                [KeyboardButton(text="Персонажі")],
                [KeyboardButton(text="Генерувати промт")],
                [KeyboardButton(text="Обговорити світ з AI")],
                [KeyboardButton(text="Про бота")],
                [KeyboardButton(text="Рестарт")],
            ],
            resize_keyboard=True
        )

def get_back_keyboard(lang="uk"):
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Back" if lang == "en" else "Повернутись")]],
        resize_keyboard=True
    )

def get_exit_dialog_keyboard(lang="uk"):
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Exit dialog" if lang == "en" else "Вийти з діалогу")]],
        resize_keyboard=True
    )
