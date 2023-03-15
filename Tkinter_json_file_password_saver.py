from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
FONT = ("arial",10)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def create_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for let in range(nr_letters)]
    password_list.extend([random.choice(numbers) for num in range(nr_numbers)])
    password_list.extend([random.choice(symbols) for sym in range(nr_symbols)])

    random.shuffle(password_list)

    password = "".join(password_list)
    pass_input.insert(0, password)
    pyperclip.copy(password)


# Save password
def add_password():
    if len(web_input.get()) != 0 and len(pass_input.get()) != 0:
        website = web_input.get()
        email = email_input.get()
        password = pass_input.get()
        new_data ={website:{
            "email":email,
            "password":password}}
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent =4)
        else:
            data.update(new_data)
            with open("data.json", mode="w") as file:
                json.dump(data, file, indent=4)
        finally:
            web_input.delete(0,END)
            pass_input.delete(0,END)
    else:
        messagebox.showerror(message="Do not leave any boxes blank")


def search_password():
    user_input = web_input.get()
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
            try:
                messagebox.showinfo(title="Title", message=f"Email: {data[user_input]['email']}\n Password:{data[user_input]['password']}")
            except KeyError:
                messagebox.showinfo(message="No details for this Website")

    except FileNotFoundError:
        messagebox.showinfo(message="No Passwords Saved")

    finally:
        web_input.delete(0, END)
        pass_input.delete(0, END)

# UI setup
window = Tk()
window.title("Password Manager")
window.configure(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=1, column=2)
# Label creation
web_label = Label(text="Website:", font=FONT)
web_label.grid(row=2, column=1)
email_label = Label(text="Email/Username:", font=FONT)
email_label.grid(row=3, column=1)
pass_label = Label(text="Password:", font=FONT)
pass_label.grid(row=4, column=1)
# input creation
web_input = Entry(width=21)
web_input.grid(row=2, column=2)
web_input.focus()
email_input = Entry(width=35)
email_input.grid(row=3, column=2, columnspan=2)
email_input.insert(0, "joel.paull96@hotmail.co.uk")
pass_input = Entry(width=21)
pass_input.grid(row=4, column=2)
# Button creation
gen_pass_button = Button(text="Generate Password", font=FONT, command=create_password)
gen_pass_button.grid(row=4, column=3)
add_button = Button(text="Add",command= add_password, font=FONT, width=50)
add_button.grid(row=5, column=2, columnspan=2)
search = Button(text="Search", width=13,command=search_password, font=FONT)
search.grid(row=2, column=3)

window.mainloop()
