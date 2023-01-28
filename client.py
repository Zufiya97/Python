import socket

from tkinter import *


def send(listbox, entry):
    message = entry.get()
    listbox.insert('end', "Client : "+message)
    entry.delete(0, END)
    s.send(bytes(message, "utf-8"))
    receive(listbox)


def receive(listbox):
    message = s.recv(50)
    listbox.insert('end', "Server : " +message.decode('utf-8'))


root = Tk()

root.geometry("200x250")
entry = Entry()
entry.pack(side="bottom", fill="x", padx=10, pady=10)

listbox = Listbox(root)
listbox.pack()

button = Button(root, text="Send", command=lambda: send(listbox, entry))
button.pack(side="left", padx=10, pady=10)

rbutton = Button(root, text="Receive", command=lambda: receive(listbox))
rbutton.pack(side="right", padx=10, pady=10)

root.title('Client')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST_NAME = socket.gethostname()
PORT = 12345

s.connect((HOST_NAME, PORT))
root.mainloop()

