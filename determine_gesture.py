import mediapipe as mp
from math import dist
import json

class gestureDetector:
    ROI = (100, 100, 300, 300) 
    ignored_points = [9, 10, 11, 12, 13, 14, 15, 16]
    threshold = 0.2
    
    def __init__(self):
        with open('gestures.json', 'r') as file:
            self.gestures = json.load(file)
        
    def detect_gesture(self, hand_landmarks):
        if hand_landmarks is None:
            return None
        
        cur_distances = self.createHandDistanceArray(hand_landmarks)
        
        for gesture_name, gesture_distances in self.gestures.items():
            if len(gesture_distances) != len(cur_distances):
                continue
            
            is_gesture = True
            for idx, distance in enumerate(cur_distances):
                if not self.within_threshold(distance, gesture_distances[idx], self.threshold):
                    is_gesture = False
                    break
            
            if is_gesture:
                return gesture_name
        
        return None
    
    
    def printHandLandmarksArray(self, results, hands=[0, 1]):
        for hand_idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
            if hand_idx not in hands:
                continue
            
            print(f"Hand {hand_idx}:\n")
            print("[")
            for landmark in hand_landmarks.landmark:
                print(f"({landmark.x}, {landmark.y}),")
            print("]")
            
    def createHandDistanceArray(self, hand_landmarks, relative=True):
        output = []
        for idx1, landmark1 in enumerate(hand_landmarks.landmark):
            if idx1 in self.ignored_points:
                continue
            for idx2, landmark2 in enumerate(hand_landmarks.landmark):
                if idx2 in self.ignored_points or idx1 == idx2:
                    continue
                if relative:
                    output.append([dist([landmark1.x], [landmark2.x]), dist([landmark1.y], [landmark2.y])])
                else:
                    output.append(dist((landmark1.x, landmark1.y), (landmark2.x, landmark2.y)))
        return output
    
    def within_threshold(self, value1, value2, threshold, relative=True):
        if relative:
            return abs(value1[0] - value2[0]) < threshold and abs(value1[1] - value2[1]) < threshold
        return abs(value1 - value2) < threshold
        
