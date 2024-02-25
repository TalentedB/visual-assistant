import pyautogui


class actionHandler:

    
    def __init__(self, overlayGui):
        self.lastFrameGesture = None
        self.isGuiOpen = False
        self.actions = {
            "palm+full-pinch": self.zoom_in,
            "full-pinch+palm": self.zoom_out,
            }

    def handle_action(self, gesture, overlayGui):
        if gesture is not None:
            self.handle_gui(gesture, overlayGui)

            if self.lastFrameGesture is not None:
                action = self.encode_gesture(gesture)
                print(action)
                if action in self.actions:
                    self.actions[action]()
            
            
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
            overlayGui.switchSelection()
            overlayGui.updateGui()
            
    def zoom_in(self):
        pyautogui.hotkey('ctrl', '+')
    
    def zoom_out(self):
        pyautogui.hotkey('ctrl', '-')