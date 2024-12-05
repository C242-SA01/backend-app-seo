from flask import Flask, request, jsonify
from flask_cors import CORS
from helper_functions import main_audit_process  # Mengimpor fungsi dari Streamlit script

app = Flask(__name__)
CORS(app, resources={r"/audit": {"origins": "http://localhost:3000"}})

@app.route('/audit', methods=['POST'])
def audit_url():
    try:
        # Ambil URL dari request body
        data = request.get_json()
        url = data.get('url')

        # Lakukan audit SEO dengan memanggil main_audit_process
        result = main_audit_process(url, maxpages=10)

        # Memeriksa apakah hasil mengandung error
        if 'error' in result:
            return jsonify({'error': result['error']}), 400

        # Konversi hasil ke dalam JSON dan return
        return jsonify(result), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
