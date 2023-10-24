from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import string


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) < 1 or len(password) < 1:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details you entered: \nEmail:{email} "
                                                              f"\nPassword:{password} \nIs ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as data_file:
                data_file.write(f"{website}  |  {email}  |  {password}\n")
                web_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

wd = Tk()
wd.title("Password Manager")
wd.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

web_label = Label(text="Website :")
web_label.grid(column=0, row=1)

email_label = Label(text="Email/Username :")
email_label.grid(column=0, row=2)

password_label = Label(text="Password :")
password_label.grid(column=0, row=3)

web_entry = Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
web_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "anas@gmail.com")  # this is not my exact email

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")

generate_button = Button(text="Generate Password", command=password_generator)
generate_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

wd.mainloop()

