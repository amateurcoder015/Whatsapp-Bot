import requests

# 🔵 Replace with your actual data
PHONE_NUMBER_ID = "616020401598082"
ACCESS_TOKEN = "EAAe3sxY0tmQBO0tcqdBCoLnWUUS8D9hCBZB7p7S1Mn8YSvnPNoGN64iZAupKrIxS54pNWl881gcj7zfBcyZAZBxhqUoKnY9HybdZAPYUC85woZAiQZC8f3jrvRrpeOKw1qd6KHqrACDgvIw2nxdUgJAxQOggU58FrLdMRNF7fYapgnP3AIkaRj8pZBN0Adjdp7QHa8pxAPbFGMbsYfhWSKS5NAjn220ZD"
TEMPLATE_NAME = "hello_world"  # should be approved in WhatsApp Manager
API_VERSION = "v22.0"

# 🔵 List of recipients: (phone number, name)
recipients = [
    ("919323180023", "Shashank"),
    ("919619141433", "Ravi"),
    ("919152054089", "Aarti"),
    ("919619941726", "Nikhil"),
    ("919372457081", "Meera")
]

# URL
url = f"https://graph.facebook.com/{API_VERSION}/{PHONE_NUMBER_ID}/messages"

# Send messages
for number, name in recipients:
    payload = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "template",
        "template": {
            "name": TEMPLATE_NAME,
            "language": {"code": "en_US"},
            "components": [
                {
                    "type": "body",
                    "parameters": [
                        {"type": "text", "text": name}  # This fills in {{1}} in template
                    ]
                }
            ]
        }
    }

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, json=payload)

    print(f"Sending to {name} ({number}) - Status: {response.status_code}")
    if response.status_code != 200:
        print("Error:", response.json())
