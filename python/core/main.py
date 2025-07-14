#!/usr/bin/env python3
"""
main.py – script for “smart” image transfer.

New functionality:
1. For each selected image, the "virtual" ChatGPT API is called,
which supposedly returns the name of the target subfolder (currently this is a stub,
randomly returning "dog" or "cat").
2. A subfolder with that name is created in the destination folder (if it doesn't already exist).
3. The image is moved to that subfolder without overwriting existing files.

Запуск:
    python move_images.py

Requirements:
    Python ≥ 3.6 (built-in modules: tkinter, shutil, pathlib, os, random, time)
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import random
import shutil
import time
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox
from GUI.main_window import *


def ask_chatgpt_for_folder(img_path: Path) -> str:
    """Simulates a call to ChatGPT for a folder name for an image."""
    print(f"👉 Sending {img_path.name} to ChatGPT for classification…")
    time.sleep(0.5)  # simulate network latency
    label = random.choice(["dog", "cat"])
    print(f"🤖 ChatGPT recommends the folder: {label}")
    return label


def safe_move(src: Path, dst_dir: Path) -> None:
    """Move file to dst_dir, avoiding overwriting existing files."""
    dst_dir.mkdir(parents=True, exist_ok=True)
    target = dst_dir / src.name

    # If the name is taken, add " (n)" before the extension
    if target.exists():
        stem, suffix = src.stem, src.suffix
        counter = 1
        while True:
            new_name = f"{stem} ({counter}){suffix}"
            target = dst_dir / new_name
            if not target.exists():
                break
            counter += 1
    shutil.move(str(src), target)


def main() -> None:
    # root = tk.Tk()
    # root.withdraw()  # hide the main window
    testObj = window()
    testObj.mainloop()

    # 1. Selecting images
    filetypes = [
        ("Images", "*.png *.jpg *.jpeg *.gif *.bmp *.tiff"),
        ("All files", "*.*"),
    ]
    image_paths = filedialog.askopenfilenames(
        title="Select images to transfer",
        filetypes=filetypes,
    )
    if not image_paths:
        messagebox.showinfo("Cancel", "No files selected - operation cancelled.")
        return

    # 2. Selecting a destination folder
    destination_dir = filedialog.askdirectory(title="Select Destination Folder")
    if not destination_dir:
        messagebox.showinfo("Cancel", "No folder selected - operation cancelled.")
        return

    destination_path = Path(destination_dir)

    # 3. Classification and transfer of files
    errors = []
    for img in image_paths:
        img_path = Path(img)
        try:
            label = ask_chatgpt_for_folder(img_path)
            dest_subdir = destination_path / label
            safe_move(img_path, dest_subdir)
        except Exception as exc:
            errors.append((img_path, str(exc)))

    if errors:
        error_lines = "\n".join(f"{p}: {e}" for p, e in errors)
        messagebox.showwarning(
            "Transfer errors" 
            f"Could not move some files:\n\n{error_lines}",
        )
    else:
        messagebox.showinfo("Done", "All images have been successfully classified and transferred!")


if __name__ == "__main__":
    main()
