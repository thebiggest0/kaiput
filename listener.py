from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener

#Mouse event handler
def on_click(x, y, button, pressed):
    action = 'Pressed' if pressed else 'Released'
    print(f'Mouse {action} at ({x}, {y}) with button {button}')

#Keyboard event handler
def on_key_event(key):
    try:
        print(f'Key {key.char} {key.name} was pressed')
    except AttributeError:
        print(f'Special key {key} was pressed')

#Create mouse listener
mouse_listener = MouseListener(on_click=on_click)

#Create keyboard listener
keyboard_listener = KeyboardListener(on_press=on_key_event)

#Start both listeners
with mouse_listener, keyboard_listener:
    mouse_listener.join()
    keyboard_listener.join()