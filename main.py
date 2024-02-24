import cv2
import numpy as np
import mediapipe as mp

def draw_landmarks_on_image(rgb_image, detection_result):
    pose_landmarks_list = detection_result.pose_landmarks.landmark
    annotated_image = np.copy(rgb_image)

    # Draw the pose landmarks.
    for landmark in pose_landmarks_list:
        x = int(landmark.x * annotated_image.shape[1])
        y = int(landmark.y * annotated_image.shape[0])
        cv2.circle(annotated_image, (x, y), 5, (255, 0, 0), -1)

    return annotated_image

def main():
    # Define a video capture object 
    vid = cv2.VideoCapture(0) 

    # Initialize MediaPipe Pose Landmark Model
    mp_pose = mp.solutions.pose.Pose()

    while True: 
        # Capture the video frame by frame 
        ret, frame = vid.read() 

        if not ret:
            break

        # Detect pose landmarks from the input image
        results = mp_pose.process(frame)

        # Process the detection result
        if results.pose_landmarks:
            annotated_image = draw_landmarks_on_image(frame, results)
            # Display the resulting frame
            cv2.imshow('MediaPipe Pose Detection', annotated_image)

        # Check if the user pressed the 'q' key, if so quit.
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break

    # Release the video capture object
    vid.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
