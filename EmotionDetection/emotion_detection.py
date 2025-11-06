import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = input, headers=header)

    # Parse JSON string to Python dictionary
    json_response = json.loads(response.text)

    # Extract emotion scores
    emotion_scores = json_response['emotionPredictions'][0]['emotion']

    # Find the dominant emotion (max value)
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Append dominant_emotion
    emotion_scores["dominant_emotion"] = dominant_emotion

    # Return the output
    return emotion_scores
