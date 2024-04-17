import time
import threading
import keyboard

# Global variable to track whether the spamming is active
spam_active = False

def spam_x_key():
    global spam_active
    while True:
        if spam_active:
            # Press the 'X' key
            keyboard.press_and_release('x')
            time.sleep(0.1)  # Adjust the delay as needed

# Create a separate thread for spamming the 'X' key
spam_thread = threading.Thread(target=spam_x_key)
spam_thread.daemon = True
spam_thread.start()

# Main loop to toggle spamming on/off
while True:
    user_input = input("Press 'T' to toggle spamming (or 'Q' to quit): ").lower()
    if user_input == 't':
        spam_active = not spam_active
        print(f"Spamming {'enabled' if spam_active else 'disabled'}")
    elif user_input == 'q':
        spam_active = False  # Stop spamming
        print("Spamming disabled. Thank you!")
        break

# Note: Press 'T' to toggle spamming on/off, and 'Q' to quit the script.
