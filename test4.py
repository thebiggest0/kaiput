import tkinter as tk
from PIL import Image, ImageTk
from pynput import keyboard

class ImageApp:
    def __init__(self, root, image_files):
        self.root = root
        self.image_files = image_files
        self.current_image = 0
        self.window_width = 320
        self.window_height = 240

        self.load_images()
        self.display_image(0)

        # Set up the global key listener
        self.listener = keyboard.Listener(on_press=self.on_keypress)
        self.listener.start()

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
        self.make_draggable(self.image_label)


    def on_keypress(self, key):
        self.current_image = (self.current_image + 1) % len(self.images)
        self.root.after(0, self.update_image)

    def update_image(self):
        self.image_label.configure(image=self.images[self.current_image])

    def make_draggable(self, widget):
        widget.bind("<Button-1>", self.on_drag_start)
        widget.bind("<B1-Motion>", self.on_drag_motion)

    def on_drag_start(self, event):
        self.drag_start_x = event.x
        self.drag_start_y = event.y

    def on_drag_motion(self, event):
        x = self.root.winfo_pointerx() - self.drag_start_x
        y = self.root.winfo_pointery() - self.drag_start_y
        self.root.geometry(f"+{x}+{y}")

def main():
    root = tk.Tk()
    root.title("Image Viewer")
    root.geometry("320x240")

    root.overrideredirect(True)

    image_files = [f"image{i}.jpg" for i in range(1, 4)]
    app = ImageApp(root, image_files)

    root.mainloop()

if __name__ == "__main__":
    main()
