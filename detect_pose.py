import cv2
import numpy as np
import mediapipe as mp
from PIL import Image

from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
"""
PoseDetector class is a wrapper around MediaPipe's Pose model.
The class provides a method to find the pose landmarks in an image.
The class also provides a method to draw the pose landmarks on an image.
"""
class PoseDetector:
    def __init__(self, static_image_mode=False, model_complexity=1, smooth_landmarks=True, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        base_options = python.BaseOptions(model_asset_path='pose_landmarker.task')
        options = vision.PoseLandmarkerOptions(
            base_options=base_options,
            output_segmentation_masks=True)
        self.detector = vision.PoseLandmarker.create_from_options(options)

    def find_pose(self, image, draw=True, convert_to_rgb=True):
        
        # Process the image and get the pose landmarks

        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)
        self.results = self.detector.detect(mp_image)

        # Draw the pose landmarks on the image if draw is True
        if draw:
            if self.results.pose_landmarks:
                image = self.draw_landmarks(image)

        
        return image

    """
    draw_landmarks method draws the pose landmarks on the image.
    """
    def draw_landmarks(self, rgb_image):
        pose_landmarks_list = self.results.pose_landmarks
        annotated_image = np.copy(rgb_image)

        # Loop through the detected poses to visualize.
        for idx in range(len(pose_landmarks_list)):
            pose_landmarks = pose_landmarks_list[idx]

            # Draw the pose landmarks.
            pose_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
            pose_landmarks_proto.landmark.extend([
            landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in pose_landmarks
            ])
            solutions.drawing_utils.draw_landmarks(
            annotated_image,
            pose_landmarks_proto,
            solutions.pose.POSE_CONNECTIONS,
            solutions.drawing_styles.get_default_pose_landmarks_style())
        return annotated_image