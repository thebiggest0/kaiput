from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener


# Mouse event handler
def on_click(x, y, button, pressed):
    # action = 'Pressed' if pressed else 'Released'
    # print(f'Mouse {action} at ({x}, {y}) with button {button}')
    if pressed:
        print(button.name)


# Keyboard event handler
def on_key_event(key):
    # try:
    #     print(f'Key {key.char} {key.name} was pressed')
    # except AttributeError:
    #     print(f'Special key {key} was pressed')
    if key:
        print(key)

# Create mouse listener
mouse_listener = MouseListener(on_click=on_click)

# Create keyboard listener
keyboard_listener = KeyboardListener(on_press=on_key_event)


# Start both listeners
def mouse_key_listern():
    with mouse_listener, keyboard_listener:
        mouse_listener.join()
        keyboard_listener.join()


def main():
    mouse_key_listern()


if __name__ == '__main__':
    main()