import requests
import json
from typing import Dict

def get_dominant_emotion(emotion_dict: Dict[str, float]) -> str:
    max_value = -1
    dominant_emotion = ""
    for senti, value in emotion_dict.items():
        if value > max_value:
            max_value = value
            dominant_emotion = senti
    return dominant_emotion

def emotion_detector(text_to_analyze: str):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    inputs = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=inputs, headers=headers)

    print(f"response: {response.status_code}\n")

    if response.status_code == 200:
        json_obj = json.loads(response.text)    
        emotion_dict = json_obj["emotionPredictions"][0]["emotion"]    
        emotion_dict["dominant_emotion"] = get_dominant_emotion(emotion_dict=emotion_dict)
        return emotion_dict
    
    else:
        return {
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None, 
            "dominant_emotion": None
        }

def main():
    text_to_analyze = "I love this new technology."
    resp = emotion_detector(text_to_analyze=text_to_analyze)
    print(resp)

if __name__ == "__main__":
    main()
