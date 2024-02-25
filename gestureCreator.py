"""
This file is used to create new gestures and add them to the gestures.json file.

The user can create a new gesture by pressing the 'e' key and then entering the name of the gesture and if it is a relative or absolute distance.
"""

import cv2
from time import sleep
import json

import detect_hands
import determine_gesture


def main():
    vid = cv2.VideoCapture(0) 

    # Initialize MediaPipe Pose Landmark Model
    handsDetector = detect_hands.HandDetector()
    gestureDetector = determine_gesture.gestureDetector()
    
    while True: 
        # Capture the video frame by frame 
        ret, frame = vid.read() 

        if not ret:
            break
    
        frame = cv2.flip(frame, 1)

        frame = handsDetector.find_hands(frame, True)
        
        
        cv2.imshow('MediaPipe Pose Detection', frame)

        # Check if the user pressed the 'q' key, if so quit.
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
                
        if cv2.waitKey(1) & 0xFF == ord('e'):
            print("Enter the name of the gesture: ")
            name = input()
            print("Enter if it is a relative or absolute distance: ")
            relative = input()
            distanceArray = gestureDetector.createHandDistanceArray(handsDetector.results.multi_hand_landmarks[0], relative == "relative")
            with open('gestures.json', 'r') as file:
                gestures = json.load(file)
                
            gestures[relative][name] = distanceArray
            
            with open('gestures.json', 'w') as file:
                json.dump(gestures, file)
            

    # Release the video capture object
    vid.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()

# This is a script, so we call the main function
if __name__ == "__main__":
    main()
