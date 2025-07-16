# Importing the tkinter module
from pathlib import Path
import tkinter as tk
from tkinter import filedialog

import sys
import os
from tkinter import messagebox
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from core.main import move_all

class window(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.wm_title("AI Classifier")

        self.geometry("600x400")        
        self.resizable(False, False)    

        container = tk.Frame(self, height=400, width=600)
        container.pack(side="top", fill="both", expand=True)
        
        # store the folders
        self.source_folder = None
        self.destination_folder = None
        
        # Entry for AI key
        self.entry = tk.Entry(container, width=40, font=("Arial", 14))
        self.entry.insert(0, "Enter Chat GPT key...")
        self.entry.pack(pady=20)
        self.entry.bind("<FocusIn>", self.clear_placeholder)
        self.entry.bind("<FocusOut>", self.add_placeholder)
        
        # Select sause directory button
        self.src_button = tk.Button(container, text="Select source folder", command=self.select_source)
        self.src_button.pack()
        
        # Select destiny directory button
        self.dest_button = tk.Button(container, text="Select destinatiob folder", command=self.select_destination)
        self.dest_button.pack()
        
        # ???
        option_frame = tk.Frame(self)
        option_frame.pack(pady=10)

        # radio buttons for category selection
        self.option_var = tk.StringVar(value = "option1")  
        self.radio1 = tk.Radiobutton(container, text="Use AI classification", variable=self.option_var, value="option1")
        self.radio2 = tk.Radiobutton(container, text="Use manual input", variable=self.option_var, value="option2")

        self.radio1.pack(pady=20)
        self.radio2.pack()

        # Start button to click for tranfer
        self.start_btn = tk.Button(container, text = "Start tranfer", command=self.run_transfer)
        self.start_btn.pack()
        
        

    def clear_placeholder(self, event):
        if self.entry.get() == "Enter Chat GPT key...":
            self.entry.delete(0, tk.END)
            self.entry.config(fg='black')

    def add_placeholder(self, event):
        if self.entry.get() == "":
            self.entry.insert(0, "Enter Chat GPT key...")
            self.entry.config(fg='gray')
            
    def select_source(self):
        source = filedialog.askdirectory(title="Select Source Folder")
        if not source:
            messagebox.showinfo("Cancel", "No files selected - operation cancelled.")
            return

        self.source_folder = Path(source)
        self.src_button.config(text=f"Source: {self.source_folder.name}")

    def select_destination(self):
        destination = filedialog.askdirectory(title="Select Source Folder")
        if not destination:
            messagebox.showinfo("Cancel", "No folder selected - operation cancelled.")
            return    
        
        self.destination_folder = Path(destination)
        self.dest_button.config(text=f"Destination: {self.destination_folder.name}")


    def run_transfer(self):
        if not self.source_folder or not self.destination_folder:
            messagebox.showwarning("Unselected Folders", "Select source and destination folders")
            return
        
        move_all(self.source_folder, self.destination_folder)




        
        
        
if __name__ == "__main__":
    testObj = window()
    testObj.mainloop()
