"""
This module contains the Flask application that detects emotions
from text using the emotion_detector function.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyzes the sentiment of the provided text.
    If the dominant emotion is None, returns an error message.
    Otherwise, it returns the detected emotion scores.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the emotions and dominant emotion from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Handle case where dominant_emotion is None (invalid input)
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Format the output according to the customer request
    formatted_output = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    # Return the formatted response
    return formatted_output


@app.route("/")
def render_index_page():
    """
    Renders the index page of the web application.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
