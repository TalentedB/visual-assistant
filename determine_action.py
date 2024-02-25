






class actionHandler:
    def __init__(self, overlayGui):
        self.lastFrameGesture = None
        self.isGuiOpen = False

    def handle_action(self, gesture, overlayGui):
        if gesture is not None:
            self.handle_gui(gesture, overlayGui)
        # TODO: Add the rest of the actions here
        self.lastFrameGesture = gesture
    
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