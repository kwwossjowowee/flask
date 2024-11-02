from flask import *
import requests 
from deep_translator import GoogleTranslator
app = Flask(__name__)
token = "7739744719:AAHQYcZCyMwO9rikqK8DSlz3FX_P6mIiUVQ"
api = f"https://api.telegram.org/bot{token}"
@app.route('/', methods=["POST"])
def home():
  data = request.get_json()
  try:
    message = data["message"]
    chat = message["chat"]
    from_user = message["from"]
  except:
    return "False"
  if message["text"] == "/start":
    requests.get(f"{api}/sendMessage", data={"chat_id": chat["id"], "text": "Welcome:)"})
  else:
    translated = GoogleTranslator(source='auto', target=from_user["language_code"]).translate(message["text"])
    requests.get(f"{api}/sendChatAction", data={"chat_id": chat["id"], "action": "typing"})
    requests.get(f"{api}/sendMessage", data={"chat_id": chat["id"], "text": translated})
  return "True"
