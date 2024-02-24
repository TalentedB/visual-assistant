# Visual-Assistant

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

## References
- [Reference 1](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8321080/)
- [Reference 2](https://www.sciencedirect.com/science/article/abs/pii/S1071581998902385)
- [Reference 3](http://www.inderscience.com/storage/f592103711148126.pdf)
- [Reference 4](https://ieeexplore.ieee.org/abstract/document/7033762)






