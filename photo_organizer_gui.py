import tkinter as tk
from tkinter import filedialog
from lib import photo_organizer as po

def main():
    print("Welcome to the photo organizer!\n")
    print("WARNING: Keep terminal open for output messages. Closing the terminal will close the program.\n")
    print("Please select the folder you would like to organize.")

    load_path = filedialog.askdirectory()
    print(f"Selected folder: {load_path}")
    print("Initializing the photo organizer... (the new window may load in the background)")

    po.PhotoOrganizer(load_path) 

if __name__ == "__main__":
    main()