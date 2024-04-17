import subprocess
import pyttsx3

if __name__ == '__main__':
    print("Welcome to Robo speaker created by saad khan")
    engine = pyttsx3.init() # initialize the text-to-speech engine
    while True:
        x = input("Enter what you want to speak >>>>")
        if x=='q':
            break
        try:
            engine.say(x) # use the engine to say the input
            engine.runAndWait() # wait until the speech is finished
        except Exception as e:
            print(f"An error occurred: {e}") # print the error message
