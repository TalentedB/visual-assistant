import mediapipe as mp
from math import dist
import json

class gestureDetector:
    ROI = (100, 100, 300, 300) 
    ignored_points = []
    threshold = 0.1
    last_gesture_name = None
    last_gesture_distances = None
    
    def __init__(self):
        
        # Load the gestures from the JSON file
        with open('gestures.json', 'r') as file:
            self.gestures = json.load(file)
    
    def detect_gesture(self, hand_landmarks):
        """
        Detects the gesture of a hand based on the landmarks provided.

        Parameters:
        hand_landmarks (list): The landmarks of the hand to detect the gesture of.

        Returns:
        str: The name of the gesture detected
        """
        
        if hand_landmarks is None:
            return None
        
        # Create an array of distances between each landmark for both relative and absolute distances
        cur_distances = {
                         "relative": self.createHandDistanceArray(hand_landmarks),
                         "absolute": self.createHandDistanceArray(hand_landmarks, False),
                         }
        
        
        for gesture_type, gestures in self.gestures.items():
            for gesture_name, gesture_distances in gestures.items():
                if len(gesture_distances) != len(cur_distances[gesture_type]):
                    continue
                
                is_gesture = True
                for idx, distance in enumerate(cur_distances[gesture_type]):
                    if not self.within_threshold(distance, gesture_distances[idx], self.threshold):
                        is_gesture = False
                        break
                
                if is_gesture:
                    return gesture_name
        
        return None
    
    def printHandLandmarksArray(self, results, hands=[0, 1]):
        """
        Prints the landmarks of the hands provided in the results.
        
        Parameters:
        results (mediapipe.python.solution_base.SolutionOutputs): The results of the hand detection model.
        hands (list): The indices of the hands to print the landmarks of.
        
        Returns:
        None
        """
        
        for hand_idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
            if hand_idx not in hands:
                continue
            
            print(f"Hand {hand_idx}:\n")
            print("[")
            for landmark in hand_landmarks.landmark:
                print(f"({landmark.x}, {landmark.y}),")
            print("]")
            
    def createHandDistanceArray(self, hand_landmarks, relative=True):
        """
        Creates an array of distances between each landmark of the hand provided.
        
        Parameters:
        hand_landmarks (mediapipe.python.solution_base.SolutionOutputs): The landmarks of the hand to create the distance array of.
        relative (bool): Whether to create the distance array based on relative or absolute distances.
        
        Returns:
        list: An array of distances between each landmark of the hand.
        """
        
        output = []
        # TODO: Optimize checking for ignored points 
        for idx1, landmark1 in enumerate(hand_landmarks.landmark):
            if idx1 in self.ignored_points:
                continue
            for idx2, landmark2 in enumerate(hand_landmarks.landmark):
                if idx2 in self.ignored_points or idx1 == idx2:
                    continue
                
                if relative:
                    output.append([dist([landmark1.x], [landmark2.x]), dist([landmark1.y], [landmark2.y])])
                else:
                    # Setting second field to -1 to allow for same function use in relative and absolute mode
                    output.append([dist([landmark1.x, landmark1.y], [landmark2.x, landmark1.y]), -1])
        return output
    
    def within_threshold(self, value1, value2, threshold, relative=True):
        """
        Determines if the two values are within the threshold provided.
        
        Parameters:
        value1 (list or float): The first value to compare.
        value2 (list or float): The second value to compare.
        threshold (float): The threshold to compare the values to.
        relative (bool): Whether the values are relative or absolute.
        
        Returns:
        bool: Whether the two values are within the threshold provided.
        """
        
        if relative:
            return abs(value1[0] - value2[0]) < threshold and abs(value1[1] - value2[1]) < threshold
        return abs(value1 - value2) < threshold
        
