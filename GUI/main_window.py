# Importing the tkinter module
import tkinter as tk



class window(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.wm_title("AI Classifier")

        self.geometry("600x400")        
        self.resizable(False, False)    

        container = tk.Frame(self, height=400, width=600)
        container.pack(side="top", fill="both", expand=True)
        



        
        
        
if __name__ == "__main__":
    testObj = window()
    testObj.mainloop()