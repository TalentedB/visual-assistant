import tkinter as tk
import threading


class ModeSwitchGui(tk.Tk):
    modes = ["Zoom", "Selection", "Scroll", "Switch Window"]
    labels = []
    
    def __init__(self):
        super().__init__()
        self.mode = 0
        self.__createGui__()
        
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
                self.destroy()
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
        
        label = tk.Label(self, text=text, font=("Arial", fontSize), bg=bg)
        label.place(x=x-len(text)*fontSize/2, y=y)
        self.labels.append(label)

    def __createGui__(self, override=True):
        """
        Creates the GUI for the mode switcher.
        
        Parameters:
        override (bool): Whether to override the window manager.
        """
        
        # Initial Setup
        self.mode_label = tk.Label(self, textvariable=self.mode)
        self.mode_label.place()
        self.after(20000, self.destroy)
        self.title("Mode Switch")
        
        self.width = 200 * len(self.modes)
        self.height = 200
        self.centerx = (self.winfo_screenwidth() // 2) - (self.width // 2)
        self.centery = (self.winfo_screenheight() // 2) - (self.height // 2)
        
        self.geometry('{}x{}+{}+{}'.format(self.width, self.height, self.centerx, self.centery))
        
        self.overrideredirect(override)
        
        self.attributes('-alpha', 1)
        self.attributes('-topmost', True)
        
        # Create the selection labels
        self.__createSelections__()
        
        # Bind the tab key to switch the selection
        self.bind("<Tab>", self.switchSelection)
        self.bind("<Escape>", self.destroyGUI)
        
        # Start the main loop
        self.mainloop()
    
    def destroyGUI(self, event):
        """
        Destroys the GUI (Needed for the escape key to work).
        """
        self.destroy()
    
    def switchSelection(self, event):
        """
        Switches the selection of the mode switcher.
        """
        self.mode = (self.mode + 1) % len(self.modes)
        self.__destroyLabels__()
        self.__createSelections__(self.mode)
        
        self.update()
        


