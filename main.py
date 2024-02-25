import cv2
import numpy as np
import mediapipe as mp
from time import sleep
import threading

import detect_pose
import detect_hands
import mode_switch_gui


def main():
    # Define a video capture object 
    vid = cv2.VideoCapture(0) 

    # Initialize MediaPipe Pose Landmark Model
    poseDetector = detect_pose.PoseDetector()
    handsDetector = detect_hands.HandDetector()

    isGuiOpen = False
    guiThread = None
    
    detected_landmarks = {}
    
    while True: 
        # Capture the video frame by frame 
        ret, frame = vid.read() 

        if not ret:
            break
        
        frame = cv2.flip(frame, 1)
        
        frame = poseDetector.find_pose(frame)
        frame = handsDetector.find_hands(frame)
        
        detected_landmarks = {"body": handsDetector.results,
                              "hands": handsDetector.results
                            }
        
        cv2.imshow('MediaPipe Pose Detection', frame)

        # Check if the user pressed the 'q' key, if so quit.
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break

        if cv2.waitKey(1) & 0xFF == ord('w'): 
            if not isGuiOpen:
                isGuiOpen = True
                guiThread = threading.Thread(target=mode_switch_gui.ModeSwitchGui)
                guiThread.start()

        if guiThread is not None and not guiThread.is_alive():
            isGuiOpen = False
            guiThread = None
        
        # sleep(0.1)

    # Release the video capture object
    vid.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
