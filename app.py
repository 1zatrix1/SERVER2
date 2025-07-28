from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def handle_post():
    data = request.get_json()
    return jsonify({
        'status': 'успешно получено',
        'ваши_данные': data
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Получаем порт от Render
    app.run(host='0.0.0.0', port=port)        # Слушаем внешний адрес
