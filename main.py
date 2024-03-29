import cv2
from time import sleep
from time import time

import detect_hands
from mode_switch_gui import ModeSwitchGui
import determine_gesture
from determine_action import actionHandler as actionHandlerClass

def getDiff(t1, t2):
    """
    Returns the absolute difference between t1 and t2.
    """
    return abs(t1 - t2)
    
def main():
    lastUpdate = 0
    overlayGui = None
    # Define a video capture object 
    vid = cv2.VideoCapture(0) 

    # Initialize MediaPipe Pose Landmark Model
    handsDetector = detect_hands.HandDetector()
    gestureDetector = determine_gesture.gestureDetector()
    overlayGui = ModeSwitchGui()
    actionHandler = actionHandlerClass(overlayGui)
    
    while True: 
        # Capture the video frame by frame 
        ret, frame = vid.read() 

        if not ret:
            break
        
        frame = cv2.flip(frame, 1)
        frame = handsDetector.find_hands(frame, True)
        
        cv2.imshow('Tracking Camera', frame)

        # Check if the user pressed the 'q' key, if so quit.
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
        
        if getDiff(lastUpdate, time()) > 0.5 and handsDetector.results.multi_hand_landmarks is not None:
            gesture = gestureDetector.detect_gesture(handsDetector.results.multi_hand_landmarks[0])
            actionHandler.handle_action(gesture, overlayGui)
            
            lastUpdate = time()

    # Release the video capture object
    vid.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
