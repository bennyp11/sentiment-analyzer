from flask import Flask, request, jsonify
from nrclex import NRCLex

# Initialize the Flask app
app = Flask(__name__)

# Define the /sentiment route
@app.route('/sentiment', methods=['POST'])
def sentiment():
    # Get the text data from the request body
    data = request.get_json()

    # Get the text from the data
    text = data.get('text', '')

    # Analyze the emotions of the text using the NRCLex
    emotion_analyzer = NRCLex(text)

    # Get the emotions from the emotion_analyzer
    emotions = emotion_analyzer.affect_frequencies

    # Create the response data as a dictionary
    response_data = {
        'emotions': emotions
    }

    # Return the response data as JSON
    return jsonify(response_data)

# Start the app on port 3008
if __name__ == '__main__':
    app.run(port=3008)
