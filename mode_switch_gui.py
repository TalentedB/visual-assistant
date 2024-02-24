import tkinter as tk
import threading


class ModeSwitchGui(tk.Tk):
    modes = ["Zoom", "Selection", "xyz"]
    
    
    def __init__(self):
        super().__init__()
        self.title("Mode Switch")
        self.geometry("700x400+-100+100")
        self.overrideredirect(True)

        self.mode = 0

        self.mode_label = tk.Label(self, textvariable=self.mode)
        self.mode_label.pack(pady=20)
        self.after(1000, self.destroy)
        self.mainloop()

        
    def switchSelection(self):
        print("Switching selection")
        self.mode = (self.mode + 1) % len(self.modes)
        self.mode_label.config(text=self.mode)
        self.update()
        



thread = threading.Thread(target=ModeSwitchGui)
thread.start()

