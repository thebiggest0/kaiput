import tkinter as tk
import threading
from PIL import Image, ImageTk
from pynput import keyboard

class ImageApp:
    def __init__(self, root, image_files, idle_images):
        self.root = root
        self.image_files = image_files
        self.idle_images = idle_images
        self.current_image = 0
        self.idle_mode = False
        self.window_width = 320
        self.window_height = 240

        self.load_images()
        self.display_image(0)

        # Set up the global key listener
        self.listener = keyboard.Listener(on_press=self.on_keypress)
        self.listener.start()

        self.idle_timer = threading.Timer(10, self.enter_idle_mode)
        self.idle_timer.start()

    def load_images(self):
        self.images = []
        # Load regular images
        for file in self.image_files:
            image = Image.open(file)
            image = self.resize_image(image, self.window_width, self.window_height)
            photo = ImageTk.PhotoImage(image)
            self.images.append(photo)
        # Load idle images
        for file in self.idle_images:
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
        if self.idle_mode:
            self.exit_idle_mode()
        else:
            self.current_image = (self.current_image + 1) % len(self.image_files)
            self.root.after(0, self.update_image)
        self.reset_idle_timer()

    def reset_idle_timer(self):
        self.idle_timer.cancel()
        self.idle_timer = threading.Timer(10, self.enter_idle_mode)
        self.idle_timer.start()

    def enter_idle_mode(self):
        self.idle_mode = True
        self.idle_loop()

    def exit_idle_mode(self):
        self.idle_mode = False
        self.update_image()

    def idle_loop(self):
        if self.idle_mode:
            # Adjust the index for idle images
            idle_index = len(self.image_files) + (self.current_image % len(self.idle_images))
            self.root.after(0, lambda: self.update_image(idle_index))
            self.root.after(500, self.idle_loop)  # Change image every half second

    def update_image(self, index=None):
        if index is not None:
            self.current_image = index
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

    # gui width x height and location
    # root.geometry("320x240")

    # width = 320
    # height = 240
    # width_screen = root.winfo_screenwidth()
    # height_screen = root.winfo_screenheight()
    # x_start = width_screen - width
    # y_start = height_screen - height
    # root.geometry(f"{width_screen}x{height_screen}+{x_start}+{y_start}")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = 320
    window_height = 240
    print(screen_width, screen_height)

    x_coord = screen_width - window_width
    y_coord = screen_height - window_height

    root.geometry(f"{window_width}x{window_height}+{x_coord}+{y_coord}")  # Set geometry for bottom right corner

    # no top menu
    root.overrideredirect(True)
    # above all screens
    root.attributes('-topmost', True)

    image_files = [f"image{i}.jpg" for i in range(1, 4)]
    idle_images = ["image_sleep1.jpg", "image_sleep2.jpg"]
    app = ImageApp(root, image_files, idle_images)

    # exit
    root.mainloop()

if __name__ == "__main__":
    main()
