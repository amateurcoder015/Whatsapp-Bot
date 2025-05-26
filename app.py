from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

ACCESS_TOKEN = "EAAe3sxY0tmQBO7j6HQmWaMtwhbbmGsu2KUleL77uD6nt2Gz1V5d534YZBtsSDZAHmR7z5Yqe4TSGqBBM8C6m8Sg7dpRqlZCZBYdeUfZCjCRCyrMOHzZAKR8kXSDdFxKZAnUxoevP3jlBS8IjinHZAmN9u5XJr5R5A3EGZBlxS76hlmICZBkXM8V82ESflANVVysMYSxZCbpLOkQZCMVUIkGhDnRFKAmVmYMZD"
PHONE_NUMBER_ID = "616020401598082"
VERIFY_TOKEN = "hello"  # You can make this up

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # Verify webhook
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if mode == 'subscribe' and token == VERIFY_TOKEN:
            return challenge, 200
        return 'Verification failed', 403

    elif request.method == 'POST':
        data = request.get_json()
        print("Received webhook:", data)

        # ✅ Handle message
        if data.get("entry"):
            for entry in data["entry"]:
                for change in entry["changes"]:
                    value = change["value"]
                    messages = value.get("messages")
                    if messages:
                        for msg in messages:
                            from_number = msg["from"]
                            msg_body = msg.get("text", {}).get("body", "")
                            print(f"Received from {from_number}: {msg_body}")
                            send_auto_reply(from_number)
        return "OK", 200

def send_auto_reply(recipient_number):
    url = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "messaging_product": "whatsapp",
        "to": recipient_number,
        "text": {
            "body": "Please Message on +91 9372457081 for any deatils regarding pricing, stock or orders."
        }
    }
    res = requests.post(url, headers=headers, json=data)
    print("Reply sent:", res.status_code, res.text)

if __name__ == "__main__":
    app.run(port=5000)
