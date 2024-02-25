import mediapipe as mp

BaseOptions = mp.tasks.BaseOptions
PoseLandmarker = mp.tasks.vision.PoseLandmarker
PoseLandmarkerOptions = mp.tasks.vision.PoseLandmarkerOptions
PoseLandmarkerResult = mp.tasks.vision.PoseLandmarkerResult
VisionRunningMode = mp.tasks.vision.RunningMode

# Create a pose landmarker instance with the live stream mode:
def print_result(result: PoseLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
    print('pose landmarker result: {}'.format(result))

options = PoseLandmarkerOptions(
    base_options=BaseOptions(model_asset_path='pose_landmarker_full'),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=print_result)

with PoseLandmarker.create_from_options(options) as landmarker:
    pass
  # The landmarker is initialized. Use it here.
  # ...


"""

    vid = cv2.VideoCapture(0) 

    while True:
        ret, frame = vid.read()

        if not ret:
            break

        frame = cv2.flip(frame, 1)

              

        cv2.imshow('MediaPipe Pose Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break

    vid.release()
    cv2.destroyAllWindows()"""