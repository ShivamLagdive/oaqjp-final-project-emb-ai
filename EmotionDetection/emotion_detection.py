import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):  # Define a function named sentiment_analyzer that takes a string input (text>
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL o>
    myobj = { "raw_document": { "text": text_to_analyse } } #Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and >
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        anger_score=emotions['anger']
        disgust_score=emotions['disgust']
        fear_score=emotions['fear']
        joy_score=emotions['joy']
        sadness_score=emotions['sadness']
        dominant_score = max(emotions, key=emotions.get)

    elif response.status_code == 400:
        anger_score=None
        disgust_score=None
        fear_score=None
        joy_score=None
        sadness_score=None
        dominant_score = None

    return {'anger': anger_score,'disgust': disgust_score,'fear': fear_score,'joy': joy_score,'sadness': sadness_score, 'dominant_emotion':dominant_score}
