from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    # X-Forwarded-For başlığını al
    forwarded_for = request.headers.get('X-Forwarded-For')
    if forwarded_for:
        ip_address = forwarded_for.split(',')[0]  # İlk IP adresini al
    else:
        ip_address = request.remote_addr  # Doğrudan IP adresini al
    return f"IP Address: {ip_address}"
