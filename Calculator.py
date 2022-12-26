from tkinter import *
import parser

root = Tk()
root.title('Calculator')

i = 0
def enter_values(num):
    global i
    display.insert(i, num)
    i += 1

def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        ACbtn()
        display.insert(0, result)
    except Exception:
        ACbtn()
        display.insert(0, "Error")

def operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length

def ACbtn():
    display.delete(0, END)

def backspace():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        ACbtn()
        display.insert(0, new_string)
    else:
        ACbtn()
        display.insert(0, "Error")

display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W + E)

Button(root, text="1", command=lambda: enter_values(1)).grid(row=2, column=0, padx=3, pady=3)
Button(root, text="2", command=lambda: enter_values(2)).grid(row=2, column=1, padx=3, pady=3)
Button(root, text="3", command=lambda: enter_values(3)).grid(row=2, column=2, padx=3, pady=3)

Button(root, text="4", command=lambda: enter_values(4)).grid(row=3, column=0, padx=3, pady=3)
Button(root, text="5", command=lambda: enter_values(5)).grid(row=3, column=1, padx=3, pady=3)
Button(root, text="6", command=lambda: enter_values(6)).grid(row=3, column=2, padx=3, pady=3)

Button(root, text="7", command=lambda: enter_values(7)).grid(row=4, column=0, padx=3, pady=3)
Button(root, text="8", command=lambda: enter_values(8)).grid(row=4, column=1, padx=3, pady=3)
Button(root, text="9", command=lambda: enter_values(9)).grid(row=4, column=2, padx=3, pady=3)

Button(root, text="AC", command=lambda: ACbtn()).grid(row=5, column=0, padx=3, pady=3)
Button(root, text="0", command=lambda: enter_values(0)).grid(row=5, column=1, padx=3, pady=3)
Button(root, text="=", command=lambda: calculate()).grid(row=5, column=2, padx=3, pady=3)

Button(root, text="+", command=lambda: operation("+")).grid(row=2, column=3, padx=3, pady=3)
Button(root, text="-", command=lambda: operation("-")).grid(row=3, column=3, padx=3, pady=3)
Button(root, text="*", command=lambda: operation("*")).grid(row=4, column=3, padx=3, pady=3)
Button(root, text="/", command=lambda: operation("/")).grid(row=5, column=3, padx=3, pady=3)

Button(root, text="pi", command=lambda: operation("*3.14")).grid(row=2, column=4, padx=3, pady=3)
Button(root, text="%", command=lambda: operation("%")).grid(row=3, column=4, padx=3, pady=3)
Button(root, text="(", command=lambda: operation("(")).grid(row=4, column=4, padx=3, pady=3)
Button(root, text="exp", command=lambda: operation("**")).grid(row=5, column=4, padx=3, pady=3)

Button(root, text="<-", command=lambda: backspace()).grid(row=2, column=5, padx=3, pady=3)
Button(root, text="^3", command=lambda: operation("**3")).grid(row=3, column=5, padx=3, pady=3)
Button(root, text=")", command=lambda: operation(")")).grid(row=4, column=5, padx=3, pady=3)
Button(root, text="^2", command=lambda: operation("**2")).grid(row=5, column=5, padx=3, pady=3)

root.mainloop()