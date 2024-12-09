import requests,json

API_KEY="FxlQqX8v.mqD9LbgmPpNThKMvi6aDmCjua1NiVl87"
URL="https://payload.vextapp.com/hook/O0WKVBXQE4/catch/user"

headers={"Content-Type":"application/json","ApiKey":f"Api-Key {API_KEY}"}
data={
"payload":"Hey there I live in Kasoa nyanyano, tell me whether there would be flood today"
}

response=requests.post(URL,headers=headers,json=data)

print(response.text)