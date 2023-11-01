from pynput.mouse import Listener

# Mouse event handler
def on_click(x, y, button, pressed):
    if pressed:
        action = 'Pressed'
    else:
        action = 'Released'
    print(f'Mouse {action} at ({x}, {y}) with button {button}')

# Create a mouse listener
with Listener(on_click=on_click) as listener:
    listener.join()



