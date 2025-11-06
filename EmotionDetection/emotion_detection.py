import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/Analyze'
    header = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock" }
    input = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=input, headers=header)
 
    try:
        response = requests.post(url, json=input_data, headers=header)
        json_response = response.json()
    except Exception as e:
        # In case of network error or invalid JSON
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Default output
    output = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }

    if response.status_code == 200:
        emotion_scores = json_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        output = {
            'anger': emotion_scores.get('anger'),
            'disgust': emotion_scores.get('disgust'),
            'fear': emotion_scores.get('fear'),
            'joy': emotion_scores.get('joy'),
            'sadness': emotion_scores.get('sadness'),
            'dominant_emotion': dominant_emotion
        }

    # if response in not 200, return default output else updated output
    return output