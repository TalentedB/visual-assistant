# visual-assistant

## Introduction

This project aims to develop a gesture-based input system as an alternative to traditional mouse and trackpad interfaces. By leveraging hand gestures, the system intends to reduce motor fatigue, prevent repetitive motion injuries, and broaden the accessibility of computing devices beyond conventional input methods. 

## Why Gesture-Based Input?

### Benefits
- **Reduction of Motor Fatigue/Injuries**: Offers relief from the strain of continuous mouse/trackpad usage.
- **Applications Beyond Educational Settings**: Expands usability to various domains beyond just educational environments.

### Usefulness
- **Addressing Demand**: Aims to fill the gap in alternative input aids for mouse/trackpad usage.
- **Wide Range of Potential Users**: Targets all age groups with particular emphasis on children, the elderly, and individuals with physical disabilities.
- **Enhanced Engagement for Learning Disabilities**: Physical gestures are often more engaging and intuitive compared to traditional input methods, benefiting users with learning disabilities such as ADHD and autism.

## Implementation Considerations

### Gesture Recognition Tools
- Utilizes TensorFlow and OpenCV for gesture recognition.
- Performance is influenced by background complexity and is currently limited to recognizing palm and fist gestures.

### Gestures/Functions to Implement
- **Swipe** and **Scroll**: Considerations include direction, speed, and scrolling amount.
- **Zoom**: Implementing zoom functionality.
- **Tabbing** through elements on the screen.
- **Select (Click)**: Requires a secondary feedback mechanism in the absence of tactile feedback.

### Actual Implementation
- Utilizes pose and hand models for gesture recognition.
- Users demonstrate gestures upon initialization, which are saved and matched to predefined gestures.
- Basic set of gestures provided for users to mimic with future plans to allow users to create their own gestures.

## Future Considerations
- Incorporating fine motor control for diverse needs including sign language.
- Expanding input modalities to include head/facial movements.
- Customizability for users to select preferred gestures and functions.
- Integration of speech-to-text for users with keyboard usage difficulties.

## Installation

To install and use our gesture-based computer control system, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/TalentedB/visual-assistant.git
    ```

2. Navigate to the project directory:

    ```bash
    cd visual-assistant
    ```

3. Install any dependencies required by the system. You may need to use a specific package manager depending on the project:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the software using the following command:
    ```bash
    python main.py
    ```

## Additional Information
1. The system comes preloaded with a set of gestures that may not work for all users. We recommend that you replace the preloaded gestures to your own gestures to suit your needs, preferences, and physique.

## Current Limitations
- The system is currently limited to only having one user on the camera at a time.
- The gestures that are made must be recreated at the same distance and angle as the original gesture.

## Creating Your Own Gestures
0. Before creating your own gestures, unless you are adding to or replacing the preloaded gestures, you must delete the values within the `gestures.json` file, resetting the file to:
    ```json
    {
    "relative": {},
    "absolute": {}
    }
    ```

1. Run the system using the following command:
    ```bash
    python gestureCreator.py
    ```
2. Once the video appears hold `e` to capture your current gesture.

3. 0. The terminal will ask you to enter the name of the gesture.
   1. If replacing the preloaded gestures. You want to replace the following names:
        - `horizontal-flap`
        - `vertical-flap`
        - `pinch`
        - `fist`
        - `point-up`
        - `point-left`
        - `point-right`
        - `point-down`

4. Describe whether it is relative or absolute (For your purposes, it is recommended to use relative).

5. Repeat steps `2-4` for every gesture you want to add.

6. Once you are done, press `q` to exit the program or `ctrl + c` within the terminal.

## References
- [Reference 1](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8321080/)
- [Reference 2](https://www.sciencedirect.com/science/article/abs/pii/S1071581998902385)
- [Reference 3](http://www.inderscience.com/storage/f592103711148126.pdf)
- [Reference 4](https://ieeexplore.ieee.org/abstract/document/7033762)






