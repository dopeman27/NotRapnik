from flask import Flask, request, jsonify
import jinja2



app = Flask(__name__)

@app.route('/')

def home():
    return "<html><body><h1>Welcome to NotRapnik!</h1><p>This is a simple Flask application.</p></body></html>"

@app.route('/api/data', methods=['GET'])

def get_data():
    data = {
        "message": "This is some sample data",
        "status": "success"
    }
    return jsonify(data)

@app.route('/api/data', methods=['POST'])

def post_data():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    return jsonify({"received": data, "status": "success"}), 201


if __name__ == '__main__':
    app.run(debug=True)
