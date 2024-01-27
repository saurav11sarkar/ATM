from tkinter import *
from PIL import ImageTk, Image
import os
def rotate_img():
    global counter
    label.config(image=img_array[counter%len(img_array)])
    counter += 1

counter = 1
root = Tk()
root.title('Wellpaper Viewer')
root.geometry('250x400')
root.configure(background='black')

# Use raw string (r) or double backslashes in the path
directory = r'D:\UNIVERSITY\VS CODE\PYTHON\GUI\wellpaper'
files = os.listdir(directory)

img_array = []
for file in files:
    img_path = os.path.join(directory, file)
    img = Image.open(img_path)
    resized_img = img.resize((200, 300))
    img_array.append(ImageTk.PhotoImage(resized_img))

# create a label to display the first image
label = Label(root, image=img_array[0])
label.pack(pady=(15, 10))

next_btn = Button(root,text="Next",bg='white',fg='black',width=28,height=2,command=rotate_img)
next_btn.pack()

root.mainloop()
