import requests

API_link = """https://api.telegram.org/bot1565175331:AAG2wfXyPKDG9_9MNIBsm8m7cqTn23SdEkA/"""

updates = requests.get( API_link + "getUpdates?offset=-1").json()

print(updates)

# 0 - первый элемент массива
message = updates["result"][0]["message"]

chat_id = message["from"]["id"]
text = message["text"]

sent_message = requests.get(API_link + f"sendMessage?chat_id={chat_id}&text=You sent me {text}")