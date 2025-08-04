import aiohttp
import os

OPENROUTER_KEY = os.getenv("OPENROUTER_KEY")
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "openai/gpt-3.5-turbo"

async def ask_gpt(system_prompt, user_message):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_KEY}",
        "Content-Type": "application/json"
    }
    json_data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ],
        "max_tokens": 400,
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(OPENROUTER_API_URL, headers=headers, json=json_data) as resp:
            data = await resp.json()
            print("DEBUG OpenRouter Response:", data)  # для дебагу
            if "choices" in data:
                return data["choices"][0]["message"]["content"]
            elif "error" in data:
                raise Exception(f"OpenRouter error: {data['error'].get('message')}")
            else:
                raise Exception(f"OpenRouter unknown error: {data}")
