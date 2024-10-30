import os
import requests
import dotenv

def fal(prompt):

    url = "https://54285744-illusion-diffusion.gateway.alpha.fal.ai/"
    dotenv.load_dotenv()
    fal_API_KEY = os.getenv("fal_API_KEY")

    headers = {
        "Authorization": "Key " + fal_API_KEY,
        "Content-type": "application/json"
    }
    payload = {
        "prompt": f"(masterpiece:1.4), (best quality), (detailed), {prompt}"
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json()["image"]["url"]