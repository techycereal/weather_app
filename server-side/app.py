from flask import Flask, request, jsonify
from flask_cors import CORS
from scrape import get_weather  # Import the complete function from your auto_complete module

app = Flask(__name__)

# Enable CORS for specific origin (http://localhost:5173)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

@app.route('/', methods=['POST', 'OPTIONS'])
def hello_world():
    if request.method == 'OPTIONS':
        # Handle CORS preflight request
        response = jsonify()
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response

    # Extract JSON data from the POST request
    r = request.get_json()

    # Call the complete function from your auto_complete module with the 'msg' data
    weather = get_weather(r['code'], r['city'])

    # Return the autocompletion results as a JSON response
    return weather

if __name__ == '__main__':
    app.run()