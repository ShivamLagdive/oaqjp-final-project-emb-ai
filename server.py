"""
server.py file 
used to process the emotiondetector
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """
    Processes data and finds emotion.

    Returns:
        str: Emotion percentage as well as dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response
    dominant_emotion=response['dominant_emotion']
    # Return a formatted string with the sentiment label and score
    if dominant_emotion is None:
        return "Invalid text! Please try again."

    return (
    f"For the given statement, the system response is {response}. "
    f"The dominant emotion is {response['dominant_emotion']}"
)


@app.route("/")
def render_index_page():
    """
    Renders home HTML
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
