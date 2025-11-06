"""
server.py

This module runs a Flask web server for emotion detection. It provides
endpoints to analyze emotions in user-submitted text and render the
index page.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emo_detector():
    """
    Endpoint to detect emotions from the provided text query parameter.

    Returns:
        str: A formatted string displaying emotion scores and dominant emotion,
        or an error message if the input text is invalid.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    # Create OUTPUT string
    output = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}.")

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    return output

@app.route("/")
def render_index_page():
    """
    Endpoint to render the main index page.

    Returns:
        str: The rendered HTML page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
