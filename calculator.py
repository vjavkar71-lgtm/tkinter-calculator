import tkinter as tk

def calculate(op):
    a = float(e1.get())
    b = float(e2.get())

    if op == "+":
        r = a + b
    elif op == "-":
        r = a - b
    elif op == "*":
        r = a * b
    elif op == "/":
        if b == 0:
            result.config(text="Cannot divide by zero")
            return
        r = a / b

    result.config(text="Result: " + str(r),bg="green")

root = tk.Tk()
root.title("Calculator")
root.geometry("300x250")

tk.Label(root, text="First Number").pack()
e1 = tk.Entry(root)
e1.pack()

tk.Label(root, text="Second Number").pack()
e2 = tk.Entry(root)
e2.pack()

tk.Button(root, text="Addition (+)", command=lambda: calculate("+")).pack()
tk.Button(root, text="Subtraction (-)", command=lambda: calculate("-")).pack()
tk.Button(root, text="Multiplication (*)", command=lambda: calculate("*")).pack()
tk.Button(root, text="Division (/)", command=lambda: calculate("/")).pack()

result = tk.Label(root, text="Result:")
result.pack()

root.mainloop()
