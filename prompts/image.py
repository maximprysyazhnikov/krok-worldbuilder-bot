def make_image_prompt(description: str, lang: str = "uk") -> str:
    # (Розширюй під власний стиль!)
    if lang == "uk":
        return f"Промт для нейромалювання: {description}, деталізований, атмосферний, концепт-арт, ілюстрація, high quality"
    return f"{description}, detailed, atmospheric, concept art, illustration, high quality"
