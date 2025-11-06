from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionalDetection(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case of dominant emotion joy
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        # Test case of dominant emotion anger
        result_1 = emotion_detector('I am really mad about this')
        self.assertEqual(result_1['dominant_emotion'], 'anger')

         # Test case of dominant emotion disgust
        result_1 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_1['dominant_emotion'], 'disgust')

        # Test case of dominant emotion sadness
        result_1 = emotion_detector('I am so sad about this')
        self.assertEqual(result_1['dominant_emotion'], 'sadness')

        # Test case of dominant emotion fear
        result_1 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_1['dominant_emotion'], 'fear')

unittest.main()