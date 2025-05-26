import requests

# 🔵 Replace with your actual data
PHONE_NUMBER_ID = "**"
ACCESS_TOKEN = "**"
TEMPLATE_NAME = "hello_world"  # should be approved in WhatsApp Manager
API_VERSION = "v22.0"

# 🔵 List of recipients: (phone number, name)
recipients = [
    ("**", "Shashank"),
    ("**", "Ravi"),
    ("**", "Aarti"),
    ("**", "Nikhil"),
    ("**", "Meera")
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
