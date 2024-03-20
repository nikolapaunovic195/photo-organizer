import os
import tkinter as tk
from PIL import Image, ImageTk
import json

class PhotoOrganizer:
    def __init__(self, load_path):
        self.load_path = load_path
        with open("folder_config.json", "r") as file:
            self._data = json.load(file)
        self._root = tk.Tk()
        self._root.title("Photo Organizer")

        self._photos = self._get_photos()
        print(f"Found {len(self._photos)} photos in the folder.")

        self._current_photo = 0

        # Prepare category labels
        for category in self._data:
            label = tk.Label(self._root, text=category)
            label.pack()

            # Prepare buttons for each folder
            for folder_name, folder_data in self._data[category].items():
                button = tk.Button(self._root, text=folder_name, command=lambda folder_data=folder_data: self.move_file(f"{self.load_path}/{self._photos[self._current_photo]}", f"{folder_data['path']}/{self._photos[self._current_photo]}"))
                button.pack()

        # Display the current photo
        self._display_photo(self._photos[self._current_photo])

        self._root.mainloop()
    
    def _get_photos(self):
        photos = []
        for file in os.listdir(self.load_path):
            if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
                photos.append(file)
        return photos
    
    def _display_photo(self, photo):
        self.img = Image.open(f"{self.load_path}/{photo}")
        self.img = self.img.resize((300, 300))
        self.img = ImageTk.PhotoImage(self.img)
        if (self._current_photo == 0):
            self.panel = tk.Label(self._root, image=self.img)
            self.panel.image = self.img
            self.panel.pack()
        else:
            self.panel.configure(image=self.img)
            self.panel.image = self.img

    def move_file(self, current_path, new_path):
        if os.path.exists(new_path):
            print("File already exists at the target location.")
            return
        try:
            os.rename(current_path, new_path)
            print(f"File moved from {current_path} to {new_path}")
            self._current_photo += 1
        except FileNotFoundError:
            print("File or folder not found.")
        
        if self._current_photo < len(self._photos):
            self._display_photo(self._photos[self._current_photo])
