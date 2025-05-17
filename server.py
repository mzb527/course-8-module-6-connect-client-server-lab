from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock event data
events = [
    {"id": 1, "title": "Tech Meetup"},
    {"id": 2, "title": "Python Workshop"}
]

# Serve homepage
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Event Catalog API!"}), 200

# GET /events - Retrieve all events
@app.route("/events", methods=["GET"])
def get_events():
    return jsonify(events), 200

# POST /events - Add a new event
@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "Missing event title"}), 400

    new_id = max(event["id"] for event in events) + 1 if events else 1
    new_event = {"id": new_id, "title": data["title"]}
    events.append(new_event)

    return jsonify(new_event), 201

if __name__ == "__main__":
    app.run(debug=True)