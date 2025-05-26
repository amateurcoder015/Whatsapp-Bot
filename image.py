import requests
import csv

PHONE_NUMBER_ID = "616020401598082"
ACCESS_TOKEN = "EAAe3sxY0tmQBO7j6HQmWaMtwhbbmGsu2KUleL77uD6nt2Gz1V5d534YZBtsSDZAHmR7z5Yqe4TSGqBBM8C6m8Sg7dpRqlZCZBYdeUfZCjCRCyrMOHzZAKR8kXSDdFxKZAnUxoevP3jlBS8IjinHZAmN9u5XJr5R5A3EGZBlxS76hlmICZBkXM8V82ESflANVVysMYSxZCbpLOkQZCMVUIkGhDnRFKAmVmYMZD"
API_VERSION = "v22.0"
CSV_FILE = "/Users/TonyStark/Desktop/vsc/bot/list2final.csv"

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