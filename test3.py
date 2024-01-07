import tkinter as tk
from PIL import Image, ImageTk

class ImageApp:
    def __init__(self, root, image_files):
        self.root = root
        self.image_files = image_files
        self.current_image = 0
        self.window_width = 400
        self.window_height = 300

        self.load_images()
        self.display_image(0)

        self.root.bind("<KeyPress>", self.on_keypress)

    def load_images(self):
        self.images = []
        for file in self.image_files:
            image = Image.open(file)
            image = self.resize_image(image, self.window_width, self.window_height)
            photo = ImageTk.PhotoImage(image)
            self.images.append(photo)

    def resize_image(self, image, max_width, max_height):
        original_width, original_height = image.size

        ratio = min(max_width / original_width, max_height / original_height)
        new_width = int(original_width * ratio)
        new_height = int(original_height * ratio)

        return image.resize((new_width, new_height), Image.Resampling.LANCZOS)

    def display_image(self, index):
        if hasattr(self, 'image_label'):
            self.image_label.destroy()
        self.image_label = tk.Label(self.root, image=self.images[index])
        self.image_label.pack()

    def on_keypress(self, event):
        self.current_image = (self.current_image + 1) % len(self.images)
        self.display_image(self.current_image)

def main():
    root = tk.Tk()
    root.title("Image Viewer")
    root.geometry("400x300")

    image_files = [f"image{i}.jpg" for i in range(1, 4)]
    app = ImageApp(root, image_files)

    root.mainloop()

if __name__ == "__main__":
    main()
