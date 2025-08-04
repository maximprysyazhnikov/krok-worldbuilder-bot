from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from bot.keyboards import (
    get_main_menu_keyboard,
    get_back_keyboard,
    get_exit_dialog_keyboard,
    get_lang_keyboard,
)
from utils import ChatStates
from prompts.ai import ask_gpt
from prompts.system import SYSTEM_PROMPT, PROMPT_SYSTEM

router = Router()

def register_handlers(dp):
    dp.include_router(router)

# --- HELPERS ---
def btn(text, *variants):
    if not text:
        return False
    t = text.strip().lower()
    return any(t == v.strip().lower() for v in variants)

# --- Вибір мови ---
@router.message(Command("start"))
async def start_handler(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Оберіть мову / Choose language:",
        reply_markup=get_lang_keyboard()
    )

@router.message(lambda m: btn(m.text, "українська"))
async def set_language_uk(message: Message, state: FSMContext):
    lang = "uk"
    await state.set_data({"lang": lang})
    await message.answer(
        "Вітаємо у світі KROK!\n\n"
        "Тут ти можеш дослідити фракції, континенти, персонажів, генерувати промти, обговорювати світ з AI.",
        reply_markup=get_main_menu_keyboard(lang)
    )

@router.message(lambda m: btn(m.text, "english"))
async def set_language_en(message: Message, state: FSMContext):
    lang = "en"
    await state.set_data({"lang": lang})
    await message.answer(
        "Welcome to the world of KROK!\n\n"
        "Here you can explore factions, continents, characters, generate AI prompts, and chat with an AI about the world.",
        reply_markup=get_main_menu_keyboard(lang)
    )

# --- Універсальний рестарт / Back ---
@router.message(lambda m: btn(m.text,
    "рестарт", "restart",
    "повернутись", "back"
))
async def universal_restart_handler(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Оберіть мову / Choose language:",
        reply_markup=get_lang_keyboard()
    )

# --- Фракції ---
@router.message(lambda m: btn(m.text, "фракції", "factions"))
async def factions_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get("lang", "uk")
    from bible.factions import FACTIONS
    await message.answer(
        "\n\n".join([f"<b>{f['name'][lang]}</b>: {f['description'][lang]}" for f in FACTIONS]),
        parse_mode="HTML",
        reply_markup=get_main_menu_keyboard(lang)
    )

# --- Континенти ---
@router.message(lambda m: btn(m.text, "континенти", "continents"))
async def continents_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get("lang", "uk")
    from bible.continents import CONTINENTS
    await message.answer(
        "\n\n".join([f"<b>{c['name'][lang]}</b>: {c['description'][lang]}" for c in CONTINENTS]),
        parse_mode="HTML",
        reply_markup=get_main_menu_keyboard(lang)
    )

# --- Персонажі ---
@router.message(lambda m: btn(m.text, "персонажі", "characters"))
async def characters_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get("lang", "uk")
    from bible.characters import CHARACTERS
    await message.answer(
        "\n\n".join([f"<b>{c['name'][lang]}</b>: {c['description'][lang]}" for c in CHARACTERS]),
        parse_mode="HTML",
        reply_markup=get_main_menu_keyboard(lang)
    )

# --- Генерація промта ---
@router.message(lambda m: btn(m.text, "генерувати промт", "create prompt"))
async def start_prompt_gen(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get("lang", "uk")
    await state.set_state(ChatStates.prompt_gen)
    await message.answer(
        "Введи короткий опис (UA/EN) — я згенерую англомовний промт для AI-генерації картинки!" if lang == "uk"
        else "Enter a short description (UA/EN) — I will generate an English AI prompt for image creation!",
        reply_markup=get_back_keyboard(lang)
    )

@router.message(StateFilter(ChatStates.prompt_gen))
async def prompt_gen_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get("lang", "uk")
    text = message.text
    prompt = await ask_gpt(PROMPT_SYSTEM, text)
    await message.answer(
        f"Ось англійський промт для AI: <b>{prompt}</b>" if lang == "uk"
        else f"Here is the English prompt for AI: <b>{prompt}</b>",
        parse_mode="HTML",
        reply_markup=get_back_keyboard(lang)
    )

# --- Вхід у AI-діалог ---
@router.message(lambda m: btn(m.text,
    "обговорити світ з ai", "discuss the world with ai"
))
async def start_ai_dialog(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get("lang", "uk")
    await state.set_state(ChatStates.ai_dialog)
    await message.answer(
        "Ти увійшов у режим AI-діалогу. Задавай питання по світу KROK!\nЩоб вийти — натисни кнопку нижче." if lang == "uk"
        else "You have entered AI-dialog mode. Ask any question about the world of KROK! To exit, press the button below.",
        reply_markup=get_exit_dialog_keyboard(lang)
    )

# --- Вихід із AI-діалогу --- (має бути вище загального ChatStates.ai_dialog!)
@router.message(StateFilter(ChatStates.ai_dialog), lambda m: btn(m.text, "вийти з діалогу", "exit dialog"))
async def exit_ai_dialog(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get("lang", "uk")
    await state.clear()
    await message.answer(
        "Ти повернувся до головного меню!" if lang == "uk"
        else "You are back to the main menu!",
        reply_markup=get_main_menu_keyboard(lang)
    )

# --- AI-діалог ---
@router.message(StateFilter(ChatStates.ai_dialog))
async def ai_dialog_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get("lang", "uk")
    user_input = message.text
    answer = await ask_gpt(SYSTEM_PROMPT, user_input)
    await message.answer(answer, reply_markup=get_exit_dialog_keyboard(lang))

# --- Про бота ---
@router.message(lambda m: btn(m.text, "про бота", "about bot", "about"))
async def about_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get("lang", "uk")
    about_text_uk = (
        "<b>KROK Worldbuilder Bot</b>\n"
        "Бот-хроніст всесвіту KROK.\n\n"
        "Можливості:\n"
        "• Дізнатися про фракції, континенти, персонажів світу\n"
        "• Генерувати промти для AI-картинок\n"
        "• Поспілкуватися з AI-експертом по лору\n\n"
        "Розробник: <a href='https://github.com/maximprysyazhnikov'>Maksym Prysyazhnikov</a>"
    )
    about_text_en = (
        "<b>KROK Worldbuilder Bot</b>\n"
        "The AI chronicler of the KROK universe.\n\n"
        "Features:\n"
        "• Learn about factions, continents, and characters\n"
        "• Generate prompts for AI images\n"
        "• Chat with a lore AI expert\n\n"
        "Developer: <a href='https://github.com/maximprysyazhnikov'>Maksym Prysyazhnikov</a>"
    )
    await message.answer(
        about_text_uk if lang == "uk" else about_text_en,
        parse_mode="HTML",
        disable_web_page_preview=True,
        reply_markup=get_main_menu_keyboard(lang)
    )
