import requests
import csv

# 🔵 Replace with your actual data
PHONE_NUMBER_ID = "**"
ACCESS_TOKEN = "**"
TEMPLATE_NAME = "fabric1image"  # should be approved in WhatsApp Manager
API_VERSION = "v22.0"
CSV_FILE = "CSV_file_location"

# 🔵 List of recipients: (phone number, name)
recipients = []
with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row['Name'].strip()
        number = row['Number'].replace("+", "").replace(" ", "").strip()
        recipients.append((number, name))

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
            "language": {"code": "en"},
            "components": [
                {
                "type": "header",
                "parameters": [
                    { "type": "image", "image": { "link": "https://nakodatextilesmills.com/wp-content/uploads/2024/08/Untitled-design-2024-08-12T010945.850.png" } }
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
