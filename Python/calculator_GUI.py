from tkinter import *

def calculator():
    num1 = float(input("Enter the first number: "))
    op = input("Enter the operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    else:
        print("Invalid operator")

window = Tk()
window.title("Calculator App")

text_box = Entry(window, width=20, borderwidth=5)
text_box.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

button_1 = Button(window, text="1", padx=40, pady=20, command=lambda: text_box.insert(END, "1"))
button_2 = Button(window, text="2", padx=40, pady=20, command=lambda: text_box.insert(END, "2"))
button_3 = Button(window, text="3", padx=40, pady=20, command=lambda: text_box.insert(END, "3"))
button_4 = Button(window, text="4", padx=40, pady=20, command=lambda: text_box.insert(END, "4"))
button_5 = Button(window, text="5", padx=40, pady=20, command=lambda: text_box.insert(END, "5"))
button_6 = Button(window, text="6", padx=40, pady=20, command=lambda: text_box.insert(END, "6"))
button_7 = Button(window, text="7", padx=40, pady=20, command=lambda: text_box.insert(END, "7"))
button_8 = Button(window, text="8", padx=40, pady=20, command=lambda: text_box.insert(END, "8"))
button_9 = Button(window, text="9", padx=40, pady=20, command=lambda: text_box.insert(END, "9"))
button_0 = Button(window, text="0", padx=40, pady=20, command=lambda: text_box.insert(END, "0"))

button_add = Button(window, text="+", padx=39, pady=20, command=lambda: text_box.insert(END, "+"))
button_subtract = Button(window, text="-", padx=41, pady=20, command=lambda: text_box.insert(END, "-"))
button_multiply = Button(window, text="*", padx=40, pady=20, command=lambda: text_box.insert(END, "*"))
button_divide = Button(window, text="/", padx=41, pady=20, command=lambda: text_box.insert(END, "/"))
button_clear = Button(window, text="Clear", padx=30, pady=20, command=lambda: text_box.delete(0, END))
button_equals = Button(window, text="=", padx=40, pady=20, command=lambda: text_box.insert(END, "="))

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_clear.grid(row=4, column=1)
button_equals.grid(row=4, column=2)

window.mainloop()
