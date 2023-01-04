from tkinter import *


def validate():
    card_no = entry.get()
    number = list(card_no)
    # print(number)
    odd_sum = 0
    even_sum = 0
    double_list = []
    for (idx, val) in enumerate(number):
        if idx % 2 != 0:
            odd_sum += int(val)
        else:
            double_list.append(int(val)*2)

    double_string = ""
    for x in double_list:
        double_string += str(x)

    double_list = list(double_string)
    # print(double_string)

    for x in double_list:
        even_sum += int(x)

    net_sum = odd_sum + even_sum
    if net_sum % 10 == 0:
        print("Valid Credit Card")
    else:
        print("Invalid Credit Card")


root = Tk()

root.title("Credit Card Validator")
root.geometry("450x200")

canvas = Canvas(root, width=400, height=150)
canvas.pack()

label = Label(root , text="Enter your Credit Card number", fg="Green" , font=("Cambria Math", 18))
canvas.create_window(200, 20, window=label)

entry = Entry(root)
canvas.create_window(200, 60, window=entry)

btn = Button(root, text="Validate", command=validate)
canvas.create_window(200, 110, window=btn)

root.mainloop()
