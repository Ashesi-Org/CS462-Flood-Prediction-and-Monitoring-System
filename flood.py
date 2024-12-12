import requests,json
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY=os.getenv("ROBUST_API_KEY")
URL="https://payload.vextapp.com/hook/O0WKVBXQE4/catch/user"

headers={"Content-Type":"application/json","ApiKey":f"Api-Key {API_KEY}"}
data={
"payload":"Hey there I live in Kasoa nyanyano, tell me whether there would be flood today"
}

response=requests.post(URL,headers=headers,json=data)

print(response.text)