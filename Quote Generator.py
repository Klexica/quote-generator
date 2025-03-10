import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")
api_url = 'https://api.api-ninjas.com/v1/quotes'
response = requests.get(api_url, headers={'X-Api-Key': api_key})
if response.status_code == requests.codes.ok:
    data = json.loads(response.text)
    data_resp = data[0]
    quote = data_resp["quote"]
    author = data_resp["author"]
    category = data_resp["category"]
    print("quote: " + quote)
    print("author: " + author)
    print("category: " + category)

else:
    print("Error:", response.status_code, response.text)
