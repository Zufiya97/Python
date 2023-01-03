from gtts import gTTS
import os
from tkinter import *

root = Tk()


def textToSpeech():
    text = entry.get()
    language = "en"
    output = gTTS(text=text, lang=language, slow=False)
    output.save("project.mp3")
    os.system("start project.mp3")


canvas = Canvas(root, width=400, height=400)
canvas.pack()

Label = Label(root, text="Enter the text that you wish to convert to speech")
canvas.create_window(200, 130, window=Label)

entry = Entry(root)
canvas.create_window(200, 180, window=entry)

button = Button(text="Convert", command=textToSpeech)
canvas.create_window(200, 230, window=button)


root.mainloop()
