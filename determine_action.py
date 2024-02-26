import pyautogui

class actionHandler:

    def __init__(self, overlayGui):
        self.mode = "Zoom"
        self.lastFrameGesture = None
        self.isGuiOpen = False
        
        self.actions = {
                        "Zoom": {
                                "horizontal-flap+horizontal-flap": self.zoom_in,
                                "vertical-flap+vertical-flap": self.zoom_out
                                },
                        "Switch Tab": {
                                "horizontal-flap+horizontal-flap": self.browser_switch_tab
                                },
                        "Switch Window": {
                                "horizontal-flap+horizontal-flap": self.switch_window,
                                "pinch+pinch": self.select
                                },
                        "Element Select": {
                                "horizontal-flap+horizontal-flap": self.tab_forward,
                                "vertical-flap+vertical-flap": self.tab_backwards,
                                "pinch+pinch": self.select,
                                "point-up+point-up": self.escape
                                },
                        "Scroll": {
                                "vertical-flap+vertical-flap": self.scroll_up,
                                "horizontal-flap+horizontal-flap": self.scroll_down
                                },
                        "Arrow Keys": {
                                "point-up+point-up": self.arrow_up,
                                "point-down+point-down": self.arrow_down,
                                "point-left+point-left": self.arrow_left,
                                "point-right+point-right": self.arrow_right
                                }
                        }

    def handle_action(self, gesture, overlayGui):
        """
        Handles the action based on the gesture provided.
        
        Parameters:
        gesture (str): The gesture to handle.
        overlayGui (ModeSwitchGui): The mode switcher GUI.
        """
        if gesture is not None:
            self.handle_gui(gesture, overlayGui)

            if not self.isGuiOpen and self.lastFrameGesture is not None:
                action = self.encode_gesture(gesture)
                if self.mode in self.actions and action in self.actions[self.mode]:
                    print(action)
                    self.actions[self.mode][action]()
            
        self.lastFrameGesture = gesture
    
    def encode_gesture(self, gesture):
        """
        Encodes the gesture to be used in the actions dictionary.
        
        Parameters:
        gesture (str): The gesture to encode.
        
        Returns:
        str: The encoded gesture.
        """
        return self.lastFrameGesture + "+" + gesture
    
    def handle_gui(self, gesture, overlayGui):
        """
        Handles the GUI based on the gesture provided.
        
        Parameters:
        gesture (str): The gesture to handle.
        overlayGui (ModeSwitchGui): The mode switcher GUI.
        """
        if gesture == "fist" and self.lastFrameGesture != "fist":
            if not self.isGuiOpen:
                self.isGuiOpen = True
                overlayGui.createGui()
                overlayGui.updateGui()
                
            elif self.isGuiOpen:
                overlayGui.destroyGUI()
                self.isGuiOpen = False
                
        
        elif self.isGuiOpen and gesture == "pinch":
            self.mode = overlayGui.switchSelection()
            overlayGui.updateGui()

    """
    The following functions are the actions that can be performed based on the gesture.
    """

    def zoom_in(self):
        pyautogui.hotkey('ctrl', '+')
    
    def zoom_out(self):
        pyautogui.hotkey('ctrl', '-')
    
    def browser_switch_tab(self):
        pyautogui.hotkey('ctrl', 'tab')
    
    def switch_window(self):
        pyautogui.hotkey('ctrl', 'alt', 'tab')
    
    def tab_forward(self):
        pyautogui.hotkey('tab')
        
    def tab_backwards(self):
        pyautogui.hotkey('shift', 'tab')
    
    def select(self):
        pyautogui.hotkey('enter')
        
    def scroll_up(self):
        pyautogui.scroll(300)
    
    def scroll_down(self):
        pyautogui.scroll(-300)
    
    def escape(self):
        pyautogui.hotkey('esc')
        
    def arrow_up(self):
        pyautogui.press('up')
    
    def arrow_down(self):
        pyautogui.press('down')
    
    def arrow_left(self):
        pyautogui.press('left')
    
    def arrow_right(self):
        pyautogui.press('right')