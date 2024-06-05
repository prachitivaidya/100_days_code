from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)


    passwordg = "".join(password_list)
    password.insert(0, passwordg)
    pyperclip.copy(passwordg)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_text.get()
    email = email_text.get()
    passwordt = password.get()

    if len(website) == 0 or len(passwordt) == 0:
        messagebox.showerror("Oops", "Please enter your website and password !")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\n "
                                                              f"Password: {passwordt}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {passwordt}\n")
                website_text.delete(0, END)
                password.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# canvas
canvas = Canvas(width= 200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0,column=1, padx=5, pady=5)

# labels
website = Label(window, text="Website:")
website.grid(column=0, row=1)

email = Label(window, text="Email/Username:")
email.grid(column=0, row=2)

password = Label(window, text="Password:")
password.grid(column=0, row=3)

# text areas
website_text = Entry(width=35, highlightthickness=0)
website_text.grid(column=1, row=1, columnspan=2, padx=5, pady=5)
website_text.focus()

email_text = Entry(width=35, highlightthickness=0)
email_text.grid(column=1, row=2, columnspan=2, padx=5, pady=5)
email_text.insert(0,"prachiti@gmail.com")

password = Entry(width=22, highlightthickness=0)
password.grid(column=1, row=3, padx=5, pady=5)

# buttons
pwd = Button(text="Generate Password", width=10, highlightthickness=0,command=generate_password)
pwd.grid(column=2, row=3, padx=2, pady=2)

add = Button(text="Add", width=32, highlightthickness=0, command=save)
add.grid(column=1, row=4, columnspan=2, padx=2, pady=2)

window.mainloop()