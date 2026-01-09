"""
Server main code
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyze text with emotion detector
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze=text_to_analyze)
    # Return a formatted string with the sentiment label and score
    if not response['dominant_emotion']:
        return "Invalid text! Please try again!."
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']}, 'sadness': {response['sadness']}, "
        f"'dominant_emotion': {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Render home page
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
