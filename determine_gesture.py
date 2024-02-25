import mediapipe as mp


class gestureDetector:
    ROI = (100, 100, 300, 300) 
    def detect_gesture(self, hand_landmarks):
        # Extract relevant landmarks (e.g., fingertips)
        mp_hands = mp.solutions.hands
        thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
        index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
        ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
        pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

        # Calculate centroid of the hand (average of all landmark positions)
        centroid_x = (thumb_tip.x + index_tip.x + middle_tip.x + ring_tip.x + pinky_tip.x) / 5
        centroid_y = (thumb_tip.y + index_tip.y + middle_tip.y + ring_tip.y + pinky_tip.y) / 5

        # Check if centroid is within the ROI
        if self.ROI[0] < centroid_x < self.ROI[0] + self.ROI[2] and self.ROI[1] < centroid_y < self.ROI[1] + self.ROI[3]:
            # Check for a simple gesture (e.g., thumb and index finger pinched)
            if thumb_tip.y < index_tip.y:
                return "Pinch"

        return None
    
    
    def printHandLandmarksArray(self, results, hands=[0, 1]):
        for hand_idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
            if hand_idx not in hands:
                continue
            
            print(f"Hand {hand_idx}:\n")
            print("[")
            for idx, landmark in enumerate(hand_landmarks.landmark):
                print(f"({landmark.x}, {landmark.y}),")
            print("]")
            