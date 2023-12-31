import tkinter as tk
from PIL import Image, ImageTk
import os

class ImageApp:
    def __init__(self, root, image_files):
        self.root = root
        self.image_files = image_files
        self.current_image = 0

        self.load_images()
        self.display_image(0)

        self.root.bind("<KeyPress>", self.on_keypress)

    def load_images(self):
        self.images = []
        for file in self.image_files:
            image = Image.open(file)
            photo = ImageTk.PhotoImage(image)
            self.images.append(photo)

    def display_image(self, index):
        self.image_label = tk.Label(self.root, image=self.images[index])
        self.image_label.pack()

    def on_keypress(self, event):
        self.current_image = (self.current_image + 1) % len(self.images)
        self.image_label.configure(image=self.images[self.current_image])

def main():
    root = tk.Tk()
    root.title("Image Viewer")

    # Assuming your images are named 'image1.jpg', 'image2.jpg', etc.
    image_files = [f"image{i}.jpg" for i in range(1, 4)]

    app = ImageApp(root, image_files)
    root.mainloop()

if __name__ == "__main__":
    main()
