import cv2
import time
import numpy as np
import mediapipe as mp

from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

VisionRunningMode = mp.tasks.vision.RunningMode

class HandDetector:
    def __init__(self):
        base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
        options = vision.HandLandmarkerOptions (
            base_options=base_options,
            running_mode=VisionRunningMode.LIVE_STREAM,
            result_callback=self.draw_landmarks
            )
        self.detector = vision.HandLandmarker.create_from_options(options)
        
    def find_hands(self, image, draw=True, convert_to_rgb=True):
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)

        timestamp = int(round(time.time()*1000))
        self.results = self.detector.detect_async(mp_image, timestamp)

        # Draw the hand landmarks on the image if draw is True
        if draw:
            if self.results.pose_landmarks:
                image = self.draw_landmarks(image)

        return image

    def draw_landmarks(self, rgb_image):
        hand_landmarks_list = self.results.hand_landmarks
        annotated_image = np.copy(rgb_image)

        for idx in range(len(hand_landmarks_list)):
            hand_landmarks = hand_landmarks_list[idx]


            hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
            hand_landmarks_proto.landmark.extend([
            landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in hand_landmarks
            ])

            solutions.drawing_utils.draw_landmarks(
                annotated_image,
                hand_landmarks_proto,
                solutions.hands.HAND_CONNECTIONS,
                solutions.drawing_styles.get_default_hand_landmarks_style())
        return annotated_image

            

'''''
class HandDetector:
    def __init__(self, static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode=static_image_mode, max_num_hands=max_num_hands, min_detection_confidence=min_detection_confidence, min_tracking_confidence=min_tracking_confidence)

    def find_hands(self, image, draw=True):
        """
        Finds the hands in the image and draws the landmarks on the image if draw is True.
        
        Parameters:
        image (np.ndarray): The image to find the hands in.
        draw (bool): Whether to draw the landmarks on the image.
        """
        # Process the image and get the hand landmarks
        self.results = self.hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        # Draw the hand landmarks on the image if draw is True
        if draw:
            if self.results.multi_hand_landmarks:
                image = self.draw_landmarks(image)

        return image

    def draw_landmarks(self, image):
        """
        Draws the landmarks on the image.
        
        Parameters:
        image (np.ndarray): The image to draw the landmarks on.
        """
        for hand_landmarks in self.results.multi_hand_landmarks:
            for landmark in hand_landmarks.landmark:
                x = int(landmark.x * image.shape[1])
                y = int(landmark.y * image.shape[0])
                cv2.circle(image, (x, y), 5, (255, 0, 0), -1)

        return image

    def __del__(self):
        """
        Closes the hands object. (Cleanup)
        """
        self.hands.close()
'''