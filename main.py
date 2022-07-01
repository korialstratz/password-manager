from tkinter import *
from tkinter import messagebox
import random
import pyperclip

FONT_NAME = "Arial"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
               't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for letter in range(nr_letters)]
    password_symbols = [random.choice(symbols) for symbol in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for number in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    website = website_entry.get()
    email_ = email_entry.get()
    password = password_entry.get()
    line = f"{website} | {email_} | {password}\n"

    if website == "" or email_ == "" or password == "":
        messagebox.showerror(title="Oppsss", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered :\nEmail: {email_}\n"
                                                              f"Password: {password}\n Is it ok to save?\n")
        if is_ok:
            with open("password.txt", "a") as file:
                file.writelines(line)
            password_entry.delete(0, END)
            website_entry.delete(0, END)
            website_entry.focus()
        else:
            messagebox.showinfo(title=website, message="Please re-enter the details")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=220, height=260)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(135, 130, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=(FONT_NAME, 12, "bold"))
website_label.grid(column=0, row=1, sticky="w")

email_label = Label(text="Email/Username:", font=(FONT_NAME, 12, "bold"))
email_label.grid(column=0, row=2, sticky="w")

password_label = Label(text="Password", font=(FONT_NAME, 12, "bold"))
password_label.grid(column=0, row=3, sticky="w")

website_entry = Entry(width=66)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=66)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "yourmail@gmail.com")

password_entry = Entry(width=38)
password_entry.grid(column=1, row=3)

generate = Button(text="Generate Password", font=(FONT_NAME, 12, "bold"), command=generate_password)
generate.grid(column=2, row=3)

add = Button(text="Add", font=(FONT_NAME, 12, "bold"), width=39, command=add_password)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()
