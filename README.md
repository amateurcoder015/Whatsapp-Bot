# WhatsApp Business Bot using Meta Cloud API

This project is a fully functional WhatsApp bot built using Meta's Cloud API and Python. It allows businesses to:

- Send approved WhatsApp message templates (text & image)
- Read user responses via webhook events
- Handle large contact lists from CSV files
- Monitor delivery/read statuses
- Respond with fallback messages (e.g. "Please call us at...")

## Features

- Bulk messaging with image support
- Flask-based webhook for real-time response tracking
- CSV integration for dynamic contact input
- Session and message error handling
- Ready for deployment via Render or Ngrok

## Requirements

- Python 3.x
- Flask
- Requests
- Meta WhatsApp Business Account with Cloud API access
- Approved message templates

## Deployment Options

- **Development:** Use Ngrok to expose Flask app
- **Production:** Deploy on Render or similar platforms

## License

MIT License
