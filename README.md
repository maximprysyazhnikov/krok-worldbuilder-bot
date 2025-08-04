# 🤖 KROK Worldbuilder Bot

**KROK Worldbuilder Bot** is a Telegram AI assistant that helps explore the universe of the game **KROK: Shadow of Unity**.  
The bot acts as a **lore chronicler**, allowing users to browse factions, continents, characters, generate prompts, and talk to a lore-aware AI.

---

## 🌍 Features

- View rich descriptions of:
  - 📜 Factions
  - 🌐 Continents
  - 🧙 Characters
- 🧠 Generate image prompts in English based on short descriptions (UA/EN)
- 🤖 Chat with a lore-aware AI about the KROK universe
- 🌐 Multilingual support: English & Ukrainian
- 🔄 Easy restart with language selection

---

## 🛠 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/krok-worldbuilder-bot.git
cd krok-worldbuilder-bot

python -m venv venv
source venv/bin/activate        # On Linux/macOS
venv\Scripts\activate.bat       # On Windows

pip install -r requirements.txt


BOT_TOKEN=your_telegram_BOT_TOKEN
OPENAI_API_KEY=your_OPENAI_API_KEY
OPENROUTER_MODEL=openai/gpt-3.5-turbo
OPENROUTER_KEY=your_OPENROUTER_KEY


▶️ Running the Bot

python main.py


✨ Credits

Developed by [Maksym Prysyazhnikov](https://github.com/maximprysyazhnikov)

Powered by aiogram v3

GPT responses via OpenAI API

📢 Coming Soon
Lore search 🔍

Image generation with preview 🎨

World map rendering 🗺

Faction leaderboards & interactive missions 💥

📬 Feedback
Feel free to open issues or contribute via Pull Requests.
Let's build the KROK universe together!