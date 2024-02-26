import numpy as np
import mediapipe as mp

from mediapipe.framework.formats import landmark_pb2
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

"""
PoseDetector class is a wrapper around MediaPipe's Pose model.
The class provides a method to find the pose landmarks in an image.
"""
class PoseDetector:
    def __init__(self):
        base_options = python.BaseOptions(model_asset_path='pose_landmarker.task')
        options = vision.PoseLandmarkerOptions(
            base_options=base_options,
            output_segmentation_masks=True)
        self.detector = vision.PoseLandmarker.create_from_options(options)

    def find_pose(self, image):
        
        # Process the image and get the pose landmarks

        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image)
        self.results = self.detector.detect(mp_image)
        
        return image