import cv2
import numpy as np
import mediapipe as mp
from time import sleep
import threading
import pyautogui

import detect_pose
import detect_hands
from mode_switch_gui import ModeSwitchGui
import determine_gesture


def main():
    isGuiOpen = False
    guiThread = None
    current_mode = 0
    lastFrameGesture = None
    
    # Define a video capture object 
    vid = cv2.VideoCapture(0) 

    # Initialize MediaPipe Pose Landmark Model
    poseDetector = detect_pose.PoseDetector()
    handsDetector = detect_hands.HandDetector()
    gestureDetector = determine_gesture.gestureDetector()
    
    detected_landmarks = {}
    
    while True: 
        # Capture the video frame by frame 
        ret, frame = vid.read() 

        if not ret:
            break
        
        frame = cv2.flip(frame, 1)
        
        # frame = poseDetector.find_pose(frame, False)
        frame = handsDetector.find_hands(frame, True)
        
        detected_landmarks = {"body": handsDetector.results,
                              "hands": handsDetector.results
                            }
        
        cv2.imshow('MediaPipe Pose Detection', frame)

        # Check if the user pressed the 'q' key, if so quit.
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
            
        if detected_landmarks["hands"].multi_hand_landmarks is not None:
            gesture = gestureDetector.detect_gesture(detected_landmarks["hands"].multi_hand_landmarks[0])
            print(gesture)
            if gesture is not None:
                if gesture == "fist" and lastFrameGesture != "fist":
                    if not isGuiOpen:
                        isGuiOpen = True
                        # Tkinter hates threading TODO: Figure out how to fix this
                        guiThread = threading.Thread(target=ModeSwitchGui, daemon=True)
                        guiThread.start()
                    else:
                        pyautogui.press('esc')
                        
                elif gesture == "pinch":
                    pyautogui.press('tab')
                
            lastFrameGesture = gesture
        
        if guiThread is not None and not guiThread.is_alive():
            isGuiOpen = False
            guiThread = None
        
        sleep(0.2)

    # Release the video capture object
    vid.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
