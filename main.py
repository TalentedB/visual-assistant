import cv2
from time import sleep

import detect_pose
import detect_hands
from mode_switch_gui import ModeSwitchGui
import determine_gesture
from determine_action import actionHandler as actionHandlerClass

overlayGui = None

def main():
    isGuiOpen = False
    global overlayGui
    current_mode = 0
    lastFrameGesture = None
    
    # Define a video capture object 
    vid = cv2.VideoCapture(0) 

    # Initialize MediaPipe Pose Landmark Model
    poseDetector = detect_pose.PoseDetector()
    handsDetector = detect_hands.HandDetector()
    gestureDetector = determine_gesture.gestureDetector()
    overlayGui = ModeSwitchGui()
    actionHandler = actionHandlerClass(overlayGui)
    
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
        
        cv2.imshow('Tracking Camera', frame)

        # Check if the user pressed the 'q' key, if so quit.
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
        
        if detected_landmarks["hands"].multi_hand_landmarks is not None:
            gesture = gestureDetector.detect_gesture(detected_landmarks["hands"].multi_hand_landmarks[0])
            
            actionHandler.handle_action(gesture, overlayGui)
                
            lastFrameGesture = gesture
    
        
        sleep(0.1)

    # Release the video capture object
    vid.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
