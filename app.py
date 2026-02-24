from flask import Flask, jsonify

app = Flask(__name__)

# Data: Destinations for your tourism project
tourist_spots = [
    {"city": "Paris", "attraction": "Eiffel Tower", "type": "History"},
    {"city": "Bali", "attraction": "Uluwatu Temple", "type": "Nature"},
    {"city": "New York", "attraction": "Times Square", "type": "Urban"},
    {"city": "Rome", "attraction": "Colosseum", "type": "History"}
]

@app.route('/')
def home():
    return "<h1>New Tourism Dashboard API</h1><p>Visit /api/destinations to see spots.</p>"

@app.route('/api/destinations')
def get_spots():
    return jsonify(tourist_spots)

if __name__ == "__main__":
    # Must use 0.0.0.0 for Docker access
    app.run(host='0.0.0.0', port=5000)