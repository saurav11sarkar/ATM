from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title('Saurav sarkar')
logo = r'D:\UNIVERSITY\VS CODE\PYTHON\GUI\wellpaper\img3.jpg'
root.iconbitmap(logo)
root.geometry('350x500')
root.configure(background='#9933FF')

flip = r'D:\UNIVERSITY\VS CODE\PYTHON\GUI\flipkart-logo-39904.png'
img = Image.open(flip)
resized_img = img.resize((70,70))
img = ImageTk.PhotoImage(resized_img)
img_label = Label(image=img)
img_label.pack(pady=(10,10))
img_label.image = img


root.mainloop()