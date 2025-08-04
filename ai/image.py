import os
import replicate
from dotenv import load_dotenv

load_dotenv()
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")
replicate_client = replicate.Client(api_token=REPLICATE_API_TOKEN)

def generate_image(prompt: str):
    output = replicate_client.run(
        "stability-ai/stable-diffusion",
        input={"prompt": prompt}
    )
    return output  # список лінків
