# visual-assistant

## Introduction

This project aims to develop a gesture-based input system as an alternative to traditional mouse and trackpad interfaces. By leveraging hand gestures, Virtual Assistant intends to broaden the accessibility of computing devices beyond conventional input methods by facilitating learning engagement and intuitive technology interaction.   

Our gesture-based computer control system aims to enhance the education experience for disabled and abled individuals of all age demographics. Our current implementation is designed to dismantle barriers faced by individuals with mobility challenges, cognitive/learning challenges, or a combination of both. In terms of physical disabilities, our current implementation is best-suited for users with fine-motor impairments, such as: arthritis, carpal tunnel syndrome, repetitive motion injuries, and temporary injuries. With regard to cognitive disabilities, our solution targets individuals with autism, ADHD, and information-processing learning disabilities. In short, Virtual Assistant bypasses the fine-motor skills required by traditional computer input tools, such as the computer mouse, and facilitates learning engagement and accessible, intuitive technology use.

## Why Gesture-Based Input?

### Mobility
Those with mobility challenges--including impairments caused by autism--may struggle to meet the fine-motor control, strength, coordination, and range-of-motion requirements of traditional computer input tools. For example, operating a computer mouse requires fine-motor control for clicking, scrolling, dragging, and navigating accurately (Trewin & Pain, 1999) (Prasanth et al., 2023). Gesture-based controls circumvent these obstacles entirely by leveraging natural body movements as a means to execute computer controls. 

### Learning
Our system targets individuals who struggle with attention retention, learning engagement, and computer navigation. Gesture-based controls fuse physical movements with the visual and auditory feedback mechanism provided by the computer. This fusion creates a multisensory experience for users–engaging multiple information-processing pathways in the brain–with the overall effect of capturing and maintaining user attention (Cai et al., 2022). Furthermore, an embodied approach facilitates active learning through proprioceptive feedback. Traditional computer-control frameworks incorporate an extremely limited range of movements (i.e. controlling a mouse); by utilizing gestures to increase sensorimotor engagement, users are more likely to enter a state of active (engaged) learning (Macrine & Fugate, 2021). Lastly, gestures provide an intuitive and direct framework for interacting with the computer, thereby reducing cognitive load. More specifically, coherently-mapped gestures (such as an upward movement to scroll up) use less cognitive resources to process, meaning more cognitive resources are devoted to learning (Cai et al., 2022). In other words, coherently-mapped gestures enable users to focus more cognitive resources on understanding the learning material rather than navigating the technological interface.  


### Key Points
- **Addressing Demand**: Aims to fill the gap in alternative input aids for mouse/trackpad usage.
- **Wide Range of Potential Users**: Targets all age groups with particular emphasis on children, the elderly, and individuals with physical disabilities.
- **Enhanced Learning Engagement**: Physical gestures are more engaging and intuitive compared to traditional input methods, thereby increasing user propensity to engage in active learning.
- **Applications Beyond Educational Settings**: Expands usability to various domains beyond just educational environments.
- **Reduction of Motor Fatigue/Injuries**: Offers relief from the strain of continuous mouse/trackpad usage.


## Implementation Considerations

### Gesture Recognition Tools
- Utilizes TensorFlow and OpenCV for gesture recognition.
- Performance is influenced by background complexity and is currently limited to recognizing palm and fist gestures.

### Actual Implementation
- Utilizes pose and hand models for gesture recognition.
- Users demonstrate gestures upon initialization, which are saved and matched to predefined gestures.
- Basic set of pre-defined gestures provided for users to get started immediately.
- Users have the freedom to create their own gestures.

### Current Features
- **Swipe** and **Scroll**: Considerations include direction, speed, and scrolling amount.
- **Custom gesture implementation**: Users can add custom gestures (and subsequent functions) to fit diverse accesibility needs. 
- **Dual-hand identification**: Users can customize gestures according to their dominant handedness, additionally, multi-hand gestures can be implemented.
- **Built-in Functionalities**:
    - **Zoom** in and out.
    - **Scroll** up and down.
    - **Switch** between **tabs**.
    - **Switch** between **windows**.
    - **Traverse/interact** with supported applications.


## Future Considerations
- Incorporating **fine motor control** for diverse needs, such as sign language.
- Expanding input modalities to include **head/facial movements**.
    - Specifically geared towards individuals with severe movement limitations. 
- Customizability for users to select **preferred gestures and functions**.
- Integration of **speech-to-text** for users with keyboard usage difficulties.
- Integration of **text-to-speech** for users with sight challenges.
- **Universal "Help" gesture:** performing the "Help" gesture in a given mode pulls up a "Help Menu", showcasing available gestures and functionalities for that specific mode. 
- **User tutorial:** Upon initial start of application, Virtual Assistant launches a tutorial to walk the user through the built-in gestures and functionalities.
- **Cursor Control:** Fully eliminate the need for a traditional computer mouse/trackpad by allowing users to control the cursor via gesture tracking.
- **Full-body** customizable gestures.
- Additional considerations concerning system capability expansion should be derived from consultation with individuals with disabilities.      
  

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
Birchfield, D., Thornburg, H., Megowan-Romanowicz, C., Romoslawski, S., Mechtley, B., Dolgov, I., & Burleson, W. (2008). Embodiment, multimodality, and composition: Convergent themes across HCI and education for mixed-reality learning environments. __Adv. Human-Computer Interaction__. 2008. 10.1155/2008/874563. [Link](https://www.researchgate.net/publication/220316649_Embodiment_Multimodality_and_Composition_Convergent_Themes_across_HCI_and_Education_for_Mixed-Reality_Learning_Environments)


Cai, B., Cai, S., He, H., He, L., Chen, Y., & Wang, A. (2022). Multisensory enhancement of cognitive control over working memory capture of attention in children with ADHD. __Brain Sci__. 2022 Dec 29;13(1):66. doi: 10.3390/brainsci13010066. PMID: 36672047; PMCID: PMC9856446. [Link](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9856446/)


Macrine, S. L. & Fugate, J. M. B. (2021). Translating embodied cognition for embodied learning in the classroom. __Frontiers in Education__, Vol. 6. ISSN 2504-284X, 10.3389/feduc.2021.712626. [Link](https://www.frontiersin.org/articles/10.3389/feduc.2021.712626)    


Prasanth, N., Shrivastava, K., Sharma, A., Basu, A., Sinha, R.A. & Raja, S.P. (2023) Gesture-based mouse control system based on MPU6050 and Kalman filter technique. __Int. J. Intelligent Systems Technologies and Applications__, Vol. 21, No. 1, pp.56–71. [Link](https://www.researchgate.net/publication/370379787_Gesture-based_mouse_control_system_based_on_MPU6050_and_Kalman_filter_technique)


Trewin, S. & Pain, H. (1999). Keyboard and mouse errors due to motor disabilities. __International Journal of Human-Computer Studies__, Vol 50, Issue 2, 1999, Pages 109-144, ISSN 1071-5819. [Link](https://doi.org/10.1006/ijhc.1998.0238)








