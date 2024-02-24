import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


"""
PoseDetector class is a wrapper around MediaPipe's Pose model.
The class provides a method to find the pose landmarks in an image.
The class also provides a method to draw the pose landmarks on an image.
"""
class PoseDetector:
    def __init__(self, static_image_mode=False, model_complexity=1, smooth_landmarks=True, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(static_image_mode=static_image_mode, model_complexity=model_complexity, smooth_landmarks=smooth_landmarks, min_detection_confidence=min_detection_confidence, min_tracking_confidence=min_tracking_confidence)

    def find_pose(self, image, draw=True, convert_to_rgb=True):
        
        # Process the image and get the pose landmarks
        self.results = self.pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        # Draw the pose landmarks on the image if draw is True
        if draw:
            if self.results.pose_landmarks:
                image = self.draw_landmarks(image)

        
        return image

    """
    draw_landmarks method draws the pose landmarks on the image.
    """
    def draw_landmarks(self, image):
        pose_landmarks_list = self.results.pose_landmarks.landmark
        annotated_image = np.copy(image)

        # Draw the pose landmarks.
        for landmark in pose_landmarks_list:
            x = int(landmark.x * annotated_image.shape[1])
            y = int(landmark.y * annotated_image.shape[0])
            cv2.circle(annotated_image, (x, y), 5, (255, 0, 0), -1)

        return annotated_image

    def __del__(self):
        self.pose.close()