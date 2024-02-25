import tkinter as tk
import threading


class ModeSwitchGui():
    modes = ["Zoom", "Selection", "Scroll", "Switch Window"]
    labels = []
    
    def __init__(self, mode=0):
        self.mode = mode
        
    def __createSelections__(self, selected=0):
        """
        Creates the selection labels for the mode switcher.
        
        Parameters:
        selected (int): The index of the selected mode.
        """
        
        fontSize = 10
        
        for i in range(len(self.modes)):
            if i == selected:
                self.__createLabel__(text=self.modes[i], x=self.height*i+100, y=self.height // 2 - fontSize, bg="red")
            else:
                self.__createLabel__(text=self.modes[i], x=self.height*i+100, y=self.height // 2 - fontSize)

    def __destroyLabels__(self):
        """
        Destroys all the labels in the mode switcher.
        """
        
        for label in self.labels:
            try:
                label.destroy()
            except():
                pass
        self.labels = []
    
    def __createLabel__(self, fontSize=10, x=0, y=0, text="", bg="white"):
        """
        Creates a label for the mode switcher.
        
        Parameters:
        fontSize (int): The size of the font.
        x (int): The x position of the label.
        y (int): The y position of the label.
        text (str): The text of the label.
        bg (str): The background color of the label.
        """
        
        label = tk.Label(self.root, text=text, font=("Arial", fontSize), bg=bg)
        label.place(x=x-len(text)*fontSize/2, y=y)
        self.labels.append(label)

    def createGui(self, override=True):
        """
        Creates the GUI for the mode switcher.
        
        Parameters:
        override (bool): Whether to override the window manager.
        """
        self.root = tk.Tk()
        
        # Initial Setup
        self.root.after(20000, self.root.destroy)
        self.root.title("Mode Switch")
        
        self.width = 200 * len(self.modes)
        self.height = 200
        self.centerx = (self.root.winfo_screenwidth() // 2) - (self.width // 2)
        self.centery = (self.root.winfo_screenheight() // 2) - (self.height // 2)
        
        self.root.geometry('{}x{}+{}+{}'.format(self.width, self.height, self.centerx, self.centery))
        
        self.root.overrideredirect(override)
        
        self.root.attributes('-alpha', 1)
        self.root.attributes('-topmost', True)
        
        # Create the selection labels
        self.__createSelections__(self.mode)
        
        # Bind the tab key to switch the selection
        self.root.bind("<Tab>", self.switchSelection)
        self.root.bind("<Escape>", self.destroyGUI)
        
        self.root.update()
    
    
    def destroyGUI(self, event=None):
        """
        Destroys the GUI (Needed for the escape key to work).
        """
        self.__destroyLabels__()
        self.root.destroy()
        self.root.update()
    
    def switchSelection(self, event=None):
        """
        Switches the selection of the mode switcher.
        """
        self.mode = (self.mode + 1) % len(self.modes)
        self.__destroyLabels__()
        self.__createSelections__(self.mode)
        return self.modes[self.mode]
        
        self.root.update()
    
    def updateGui(self):
        """
        Updates the GUI.
        """
        self.root.update()
        


