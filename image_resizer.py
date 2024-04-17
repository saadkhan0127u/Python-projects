from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def resize_image(image_path, width, height):
    img = Image.open(image_path)
    img = img.resize((width, height))
    img.save('resized_image.jpg')

def main():
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    image_path = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    width = int(input("Enter the desired width: "))
    height = int(input("Enter the desired height: "))
    resize_image(image_path, width, height)
    print("Image resized successfully!")

if __name__ == "__main__":
    main()
