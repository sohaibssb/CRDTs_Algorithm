from flask import Flask, request, jsonify

app = Flask(__name__)

chat_history = []

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    user_id = data['user_id']
    message = data['message']
    
    #Generate a unique timestamp for each message (simulating Lamport timestamps)
    timestamp = len(chat_history)
    
    chat_history.append({"user_id": user_id, "message": message, "timestamp": timestamp})

    print(f"Received Message: {user_id}: {message}")
    
    return "Message sent successfully", 200

@app.route('/get_chat_history', methods=['GET'])
def get_chat_history():
    user_id = request.args.get('user_id')
    
    filtered_history = sorted(
        [message for message in chat_history if message["user_id"] == user_id],
        key=lambda x: x["timestamp"]
    )
    
    return jsonify(filtered_history), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 
