import requests
import dotenv
import os

def plant(plant_name):

    url = "https://my-api.plantnet.org/v2/identify/all"
    dotenv.load_dotenv()
    plantnet_API_KEY = os.getenv("plantnet_API_KEY")

    headers = {
    }
    payload = {
        "api-key": plantnet_API_KEY
    }
    files = {
        "images": open(plant_name, "rb"),
    }

    response = requests.post(url, headers=headers, params=payload, files=files)
    print(response.status_code)
    print(response.json())

    try:
        plant_name = response.json()["results"][0]["species"]["family"]["scientificName"]
    except:
        plant_name = "Not defined"

    return plant_name
