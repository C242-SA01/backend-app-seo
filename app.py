from flask import Flask, jsonify
from flask_cors import CORS
from login import auth_blueprint
from history import history_blueprint
from register import register_blueprint

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}},
    supports_credentials=True,
    expose_headers=["Content-Type"],
    allow_headers=["Content-Type", "Authorization"],
    methods=["POST", "OPTIONS"])

# Menambahkan route untuk halaman utama
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the SEO Audit API"}), 200

# Mendaftarkan blueprints untuk rute autentikasi, history, dan registrasi
app.register_blueprint(auth_blueprint, url_prefix="/login")
app.register_blueprint(history_blueprint, url_prefix="/history")
app.register_blueprint(register_blueprint, url_prefix="/register")

if __name__ == "__main__":
    app.run(debug=True)
