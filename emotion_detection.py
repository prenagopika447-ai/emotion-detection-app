import requests
import json

def emotion_detector(text_to_analyze):
    # Watson NLP Emotion Detection endpoint
    url = 'https://sn-watson-emotion.labs.skills.network'
    
    # Headers specifying the model to use
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_en_stock"}
    
    # JSON payload with the text to analyze
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Send POST request
    response = requests.post(url, json=myobj, headers=header)
    
    # Parse response
    formatted_response = json.loads(response.text)
    
    # Extract specific emotions and dominant emotion
    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        anger = emotions['anger']
        disgust = emotions['disgust']
        fear = emotions['fear']
        joy = emotions['joy']
        sadness = emotions['sadness']
        dominant_emotion = max(emotions, key=emotions.get)
        
        return {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }
    else:
        return None

