import json
import requests
import os
import dotenv

dotenv = dotenv.load_dotenv()
plantnet_API_KEY = os.getenv("plantnet_API_KEY")