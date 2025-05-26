import requests
import csv

PHONE_NUMBER_ID = "**"
ACCESS_TOKEN = "**"
API_VERSION = "v22.0"
CSV_FILE = "csv_file_location"

recipients = []
with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row['Name'].strip()
        number = row['Number'].replace("+", "").replace(" ", "").strip()
        recipients.append((number, name))


url = f"https://graph.facebook.com/v22.0/{PHONE_NUMBER_ID}/messages"
for number, name in recipients:
    image_1 = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "image",
        "image": {
            "link": "https://postimage.me/images/2025/05/16/WhatsApp-Image-2025-05-16-at-21.44.02.jpeg"
        }
    }

    image_2 = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "image",
        "image": {
            "link": "https://postimage.me/images/2025/05/16/WhatsApp-Image-2025-05-16-at-21.44.52.jpeg"
        }
    }

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    response1 = requests.post(url, headers=headers, json=image_1)
    print("Image 1:",response1.status_code, response1.json())
    if response1.status_code != 200:
        print("Error:", response1.json())

    response2 = requests.post(url, headers=headers, json=image_2)
    print("Image 2:",response2.status_code, response2.json())
    if response2.status_code != 200:
        print("Error:", response2.json())
