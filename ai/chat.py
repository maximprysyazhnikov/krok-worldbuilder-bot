import os
import requests
from dotenv import load_dotenv
from prompts.system import SYSTEM_PROMPT

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_KEY")
MODEL = os.getenv("OPENROUTER_MODEL", "openai/gpt-3.5-turbo")

def get_ai_lore_answer(prompt: str, lang: str = "uk") -> str:
    if not OPENROUTER_API_KEY:
        return "(Помилка: Не задано OPENROUTER_KEY)"
    system = SYSTEM_PROMPT.get(lang, SYSTEM_PROMPT["uk"])
    headers = {
        "Authorization": f"Bearer {OPENROUTER_KEY}",
        "HTTP-Referer": "https://openrouter.ai/",
        "X-Title": "KROK Worldbuilder AI"
    }
    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 500,
        "temperature": 0.8
    }
    r = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data, timeout=30)
    if r.status_code == 200:
        return r.json()["choices"][0]["message"]["content"].strip()
    return f"(Помилка: {r.status_code} {r.text})"
