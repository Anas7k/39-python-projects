from tkinter import *


def mile_to_km():
    user_input = float(entry.get())
    result = (user_input * 1.60934)
    result_label.config(text=f"{result:.2f}")

    
wd = Tk()
wd.minsize(width=200, height=100)
wd.title("Mile to Km Converter")
wd.config(padx=20, pady=10)

entry = Entry(width=12)
entry.grid(column=1, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

button = Button(text="Calculate", command=mile_to_km)
button.grid(column=1, row=2)

wd.mainloop()

