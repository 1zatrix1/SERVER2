from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def handle_post():
    data = request.get_json()
    return jsonify({
        'status': 'успешно получено',
        'ваши_данные': data
    })

if __name__ == '__main__':
    app.run()
