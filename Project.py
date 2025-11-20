import tkinter as tk
from datetime import date

def calculate_age():
        d = int(day.get())
        m = int(month.get())
        y = int(year.get())

        today = date.today()
        age = today.year - y

        if (today.month, today.day) < (m, d):
            age -= 1

        result.configure(text=f"Age: {age}")


root = tk.Tk()
root.title("Age Calculator")
root.geometry("400x400")
root.configure(bg="#EFC3CA")

tk.Label(root, text="Day:",bg="#DFC57B").pack()
day = tk.Entry(root)
day.pack()
tk.Label(root, text="Month:",bg="#DFC57B").pack()
month = tk.Entry(root)
month.pack()
tk.Label(root, text="Year:",bg="#DFC57B").pack()
year = tk.Entry(root)
year.pack()
tk.Button(root, text="Calculate", command=calculate_age,bg="#7DDA58").pack(pady=10)
result = tk.Label(root, text="Age:",bg="#DFC57B")
result.pack()

root.mainloop()