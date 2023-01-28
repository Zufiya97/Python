import socket

from tkinter import *


def send(listbox, entry):
    message = entry.get()
    listbox.insert('end', "Server:" + message)
    entry.delete(0, END)
    client.send(bytes(message, "utf-8"))


def receive(listbox):
    message2 = client.recv(50)
    listbox.insert('end', "Client :" + message2.decode('utf-8'))


root = Tk()

root.title("Server")
root.geometry("200x250")
entry = Entry()
entry.pack(side="bottom", fill="x", padx=10, pady=10)

listbox = Listbox(root)
listbox.pack()

button = Button(root, text="Send", command=lambda: send(listbox, entry))
button.pack(side="right", padx=10, pady=10)

rbutton = Button(root, text="Receive", command=lambda: receive(listbox))
rbutton.pack(side="left", padx=10, pady=10)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST_NAME = socket.gethostname()
PORT = 12345

s.bind((HOST_NAME, PORT))
s.listen(4)
client, address = s.accept()

root.mainloop()