import tkinter as tk

root = tk.Tk()

root.title("Calc-ex")

e = tk.Entry(borderwidth=5, width=28, font=("Cambria Math", 16), justify="right")
e.grid(row=0, column=0, columnspan=3)


def button_Backspace(event=None):
    current_text = e.get()
    last_index = len(current_text) - 1
    if last_index >= 0:
        e.delete(last_index)

root.bind("<BackSpace>", lambda event: button_Backspace())

Button_back = tk.Button(root, font=("Arial", 16, "bold"), padx=20, pady=45, text="Back", borderwidth=3,
                        command=button_Backspace)
Button_back.grid(row=0, column=3)

root.bind("<Escape>", lambda event: e.delete(0, "end"))

Button_clear = tk.Button(root, font=("Arial", 16, "bold"), padx=20, pady=45, text="Clear", borderwidth=3,
                         command=lambda: e.delete(0, "end"))
Button_clear.grid(row=1, column=3)


def button_Operator(operation, event=None):
    try:
        global f_num, math
        first_num = eval(e.get())
        f_num = first_num
        math = operation
        e.delete(0, "end")
    except Exception:
        e.delete(0, "end")
        e.insert(0, "Error")


def button_Equal(event=None):
     try:
        second_num = eval(e.get())
        e.delete(0, "end")
        if math == "add":
            e.insert(0, str(f_num + second_num))
        if math == "subtract":
            e.insert(0, str(f_num - second_num))
        if math == "multiply":
            e.insert(0, str(f_num * second_num))
        if math == "divide":
            if second_num != 0:
                if (f_num/second_num) % 1 == 0:
                    e.insert(0, str(int(f_num / second_num)))
                else:
                    e.insert(0, str(f_num / second_num))
            else:
                e.insert(0, "ZeroDivisionError: division by zero")
     except Exception:
         e.delete(0, "end")
         e.insert(0, "Error")


root.bind("/", lambda event: button_Operator("divide"))

Button_div = tk.Button(root, font=("Arial", 16, "bold"), padx=43, pady=45, text="/", borderwidth=3,
                       command=lambda: button_Operator("divide"))
Button_div.grid(row=1, column=0)

root.bind("*", lambda event: button_Operator("multiply"))

Button_mul = tk.Button(root, font=("Arial", 16, "bold"), padx=43, pady=45, text="*", borderwidth=3,
                       command=lambda: button_Operator("multiply"))
Button_mul.grid(row=1, column=1)

root.bind("-", lambda event: button_Operator("subtract"))

Button_sub = tk.Button(root, font=("Arial", 16, "bold"), padx=43, pady=45, text="-", borderwidth=3,
                       command=lambda: button_Operator("subtract"))
Button_sub.grid(row=1, column=2)

root.bind("7", lambda event: e.insert("end", "7"))

Button7 = tk.Button(root, font=("Arial", 16, "bold"), padx=40, pady=45, text="7", borderwidth=3,
                    command=lambda: e.insert("end", "7"))
Button7.grid(row=2, column=0)

root.bind("8", lambda event: e.insert("end", "8"))

Button8 = tk.Button(root, font=("Arial", 16, "bold"), padx=40, pady=45, text="8", borderwidth=3,
                    command=lambda: e.insert("end", "8"))
Button8.grid(row=2, column=1)

root.bind("9", lambda event: e.insert("end", "9"))

Button9 = tk.Button(root, font=("Arial", 16, "bold"), padx=40, pady=45, text="9", borderwidth=3,
                    command=lambda: e.insert("end", "9"))
Button9.grid(row=2, column=2)

root.bind("+", lambda event: button_Operator("add"))

Button_add = tk.Button(root, font=("Arial", 16, "bold"), padx=40, pady=112, text="+", borderwidth=3,
                       command=lambda: button_Operator("add"))
Button_add.grid(row=2, column=3, rowspan=2)

root.bind("4", lambda event: e.insert("end", "4"))

Button4 = tk.Button(root, font=("Arial", 16, "bold"), padx=40, pady=45, text="4", borderwidth=3,
                    command=lambda: e.insert("end", "4"))
Button4.grid(row=3, column=0)

root.bind("5", lambda event: e.insert("end", "5"))

Button5 = tk.Button(root, font=("Arial", 16, "bold"), padx=40, pady=45, text="5", borderwidth=3,
                    command=lambda: e.insert("end", "5"))
Button5.grid(row=3, column=1)

root.bind("6", lambda event: e.insert("end", "6"))

Button6 = tk.Button(root, font=("Arial", 16, "bold"), padx=40, pady=45, text="6", borderwidth=3,
                    command=lambda: e.insert("end", "6"))
Button6.grid(row=3, column=2)

root.bind("=", lambda event: button_Equal())

root.bind("<Return>", lambda event: button_Equal())

Button_enter = tk.Button(root, font=("Arial", 16, "bold"), padx=40, pady=112, text="=", borderwidth=3,
                         command=button_Equal)
Button_enter.grid(row=4, column=3, rowspan=2)

root.bind("1", lambda event: e.insert("end", "1"))

Button1 = tk.Button(root, font=("Arial", 16, "bold"), padx=40, pady=45, text="1", borderwidth=3,
                    command=lambda: e.insert("end", "1"))
Button1.grid(row=4, column=0)

root.bind("2", lambda event: e.insert("end", "2"))

Button2 = tk.Button(root, font=("Arial", 16, "bold"), padx=40, pady=45, text="2", borderwidth=3,
                    command=lambda: e.insert("end", "2"))
Button2.grid(row=4, column=1)

root.bind("3", lambda event: e.insert("end", "3"))

Button3 = tk.Button(root, font=("Arial", 16, "bold"), padx=40, pady=45, text="3", borderwidth=3,
                    command=lambda: e.insert("end", "3"))
Button3.grid(row=4, column=2)

root.bind("0", lambda event: e.insert("end", "0"))

Button0 = tk.Button(root, font=("Arial", 16, "bold"), padx=40, pady=45, text="0", borderwidth=3,
                    command=lambda: e.insert("end", "0"))
Button0.grid(row=5, column=1)

root.bind(".", lambda event: e.insert("end", "."))

Button_decimal = tk.Button(root, font=("Arial", 16, "bold"), padx=43, pady=45, text=".", borderwidth=3,
                           command=lambda: e.insert("end", "."))
Button_decimal.grid(row=5, column=2)

root.mainloop()
