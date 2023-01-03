from tkinter import *
import bcrypt


def validate(password):
    hash = b'$2b$12$eMAENpMOOqZJAlrHQJx9aOw7v/IYBdNPpO2smis2xEcR8vNnjKQPG'
    password = bytes(password, encoding="utf-8")

    if bcrypt.checkpw(password, hash):
        print("Login Successful!")
    else:
        print("Invalid Password")


root = Tk()
root.geometry("200x200")

label = Label(root, text="Enter your password")
label.pack()

password_entry = Entry(root)
password_entry.pack()

password_entry.get()
button = Button(text="Validate", command=lambda: validate(password_entry.get()))
button.pack()

root.mainloop()
