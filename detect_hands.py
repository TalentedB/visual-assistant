import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision




class HandDetector:
    def __init__(self, static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode=static_image_mode, max_num_hands=max_num_hands, min_detection_confidence=min_detection_confidence, min_tracking_confidence=min_tracking_confidence)

    def find_hands(self, image, draw=True, convert_to_rgb=True):
        # Process the image and get the hand landmarks
        self.results = self.hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        # Draw the hand landmarks on the image if draw is True
        if draw:
            if self.results.multi_hand_landmarks:
                image = self.draw_landmarks(image)

        return image

    def draw_landmarks(self, image):
        for hand_landmarks in self.results.multi_hand_landmarks:
            for landmark in hand_landmarks.landmark:
                x = int(landmark.x * image.shape[1])
                y = int(landmark.y * image.shape[0])
                cv2.circle(image, (x, y), 5, (255, 0, 0), -1)

        return image

    def __del__(self):
        self.hands.close()