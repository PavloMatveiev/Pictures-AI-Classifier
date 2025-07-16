# Importing the tkinter module
import tkinter as tk
from tkinter import filedialog



class window(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.wm_title("AI Classifier")

        self.geometry("600x400")        
        self.resizable(False, False)    

        container = tk.Frame(self, height=400, width=600)
        container.pack(side="top", fill="both", expand=True)
        
        
        
        self.entry = tk.Entry(container, width=40, font=("Arial", 14))
        self.entry.insert(0, "Enter Chat GPT key...")
        self.entry.pack(pady=20)
        
        
        
        self.entry.bind("<FocusIn>", self.clear_placeholder)
        self.entry.bind("<FocusOut>", self.add_placeholder)
        
        self.select_button = tk.Button(container, text="Select folder", command=self.select_folder)
        self.select_button.pack()
        
        
        
        
        self.option_var = tk.StringVar(value = "option1")  

        option_frame = tk.Frame(self)
        option_frame.pack(pady=10)

        self.radio1 = tk.Radiobutton(container, text="Use AI classification", variable=self.option_var, value="option1")
        self.radio2 = tk.Radiobutton(container, text="Use manual input", variable=self.option_var, value="option2")

        self.radio1.pack(pady=20)
        self.radio2.pack()
        
        
        

    def clear_placeholder(self, event):
        if self.entry.get() == "Enter Chat GPT key...":
            self.entry.delete(0, tk.END)
            self.entry.config(fg='black')

    def add_placeholder(self, event):
        if self.entry.get() == "":
            self.entry.insert(0, "Enter Chat GPT key...")
            self.entry.config(fg='gray')
            
    def select_folder(self):
        filedialog.askdirectory(title="Choose Folder")


        
        
        
if __name__ == "__main__":
    testObj = window()
    testObj.mainloop()