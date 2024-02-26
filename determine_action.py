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
                                "pinch+pinch": self.select
                                },
                        "Scroll": {
                                "vertical-flap+vertical-flap": self.scroll_up,
                                "horizontal-flap+horizontal-flap": self.scroll_down
                                }
                        }

    def handle_action(self, gesture, overlayGui):
        if gesture is not None:
            self.handle_gui(gesture, overlayGui)

            if not self.isGuiOpen and self.lastFrameGesture is not None:
                action = self.encode_gesture(gesture)
                if self.mode in self.actions and action in self.actions[self.mode]:
                    self.actions[self.mode][action]()
            
            
        # TODO: Add the rest of the actions here
        self.lastFrameGesture = gesture
    
    def encode_gesture(self, gesture):
        return self.lastFrameGesture + "+" + gesture
    
    def handle_gui(self, gesture, overlayGui):
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