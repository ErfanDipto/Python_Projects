import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # print("Welcome to the PyPassword Generator!")
    # nr_letters = int(input("How many letters would you like in your password?\n"))
    # nr_symbols = int(input(f"How many symbols would you like?\n"))
    # nr_numbers = int(input(f"How many numbers would you like?\n"))
    nr_letters = 4
    nr_symbols = 2
    nr_numbers = 2

    # Eazy Level - Order not randomised:
    # e.g. 4 letter, 2 symbol, 2 number = JduE&!91

    # Hard Level - Order of characters randomised:
    # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
    # eazy level
    p_letters = [random.choice(letters) for letter in range(nr_letters)]
    # print(p_letters)
    p_symbols = [random.choice(symbols) for symbol in range(nr_symbols)]
    p_numbers = [random.choice(numbers) for number in range(nr_numbers)]
    # for i in range(0, nr_letters):
    #     p_letters.append(random.choice(letters))
    # # print(p_letters)
    # for j in range(0, nr_symbols):
    #     p_symbols.append(random.choice(symbols))
    # for i in range(0, nr_numbers):
    #     p_numbers.append(random.choice(numbers))

    # total = [p_letters, p_symbols, p_numbers]

    string = ""

    for ele in p_letters:
        string += ele
    for ele in p_symbols:
        string += ele
    for ele in p_numbers:
        string += ele

    # hard mode

    ran_string_list = random.sample(string, len(string))

    ran_string = ""

    for ele in ran_string_list:
        ran_string += ele
    # print(f"Your password is: {ran_string}")
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, ran_string)
    pyperclip.copy(ran_string)
    # print(string)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def info_saver():
    is_ok = False
    new_data = {
        web_entry.get(): {
            "Email/User": email_user_entry.get(),
            "Password": password_entry.get()

        }
    }
    if len(web_entry.get()) == 0 or len(email_user_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showerror(title="Empty Field", message="Hey! You have left empty field")
    else:
        # is_ok = messagebox.askokcancel(title="Proceed?", message=f"This is your info-\n\nWebsite: "
        #                                                          f"{web_entry.get()}\nEmail\\Username: "
        #                                                          f"{email_user_entry.get()}\nPassword: "
        #                                                          f"{password_entry.get()}\n\nDo you want to proceed?")
        is_ok = True
    if is_ok:
        try:
            with open("Data.json", "r") as data_file:
                data = json.load(data_file)
                print(data)
                data.update(new_data)
                # data.write(f"{web_entry.get()} | {email_user_entry.get()} | {password_entry.get()}\n")
        except json.decoder.JSONDecodeError or FileNotFoundError:
            # with open("Data.json", "w") as data_file:
            #     data = json.load(data_file)
            #     data.update(new_data)
            with open("Data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("Data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        web_entry.delete(0, tk.END)
        email_user_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)


# ---------------------------- Data Search ------------------------------- #


def data_search():
    found = False
    try:
        with open("Data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError or json.decoder.JSONDecodeError:
        messagebox.showerror(title="No data", message="No data file found")
    else:
        for (key, value) in data.items():
            if web_entry.get() == key:
                found = True
                messagebox.showinfo(title="Match Found", message=f"You already have an account in this website."
                                                                 f"\nEmail\\User: {data[key]['Email/User']}\nPassword: "
                                                                 f"{data[key]['Password']}")
            else:
                pass
        if not found:
            messagebox.showinfo(title="No Match", message="Sorry, no match found")


# ---------------------------- UI SETUP ------------------------------- #
# ui window
window = tk.Tk()
window.config(padx=50, pady=50, bg="white")
window.title("Password Manager")

# canvas setup
canvas = tk.Canvas(width=202, height=200, bg="white", highlightthickness=0)
lock_image = tk.PhotoImage(file="logo.png")
canvas.create_image(101, 100, image=lock_image)
canvas.grid(row=0, column=1)

# labels
web_labels = tk.Label(text="Website: ", bg="white")
web_labels.grid(row=1, column=0)

email_user = tk.Label(text="Email/Username: ", bg="white")
email_user.grid(row=2, column=0)

password_label = tk.Label(text="Password: ", bg="white")
password_label.grid(row=3, column=0)

# entry
web_entry = tk.Entry(width=33)
web_entry.grid(row=1, column=1, columnspan=1)
web_entry.focus()

email_user_entry = tk.Entry(width=50)
email_user_entry.grid(row=2, column=1, columnspan=2)

password_entry = tk.Entry(width=33)
password_entry.grid(row=3, column=1)

# buttons
search_button = tk.Button(text="Search", bg="white", font=("", 8, "normal"), width=15, command=data_search)
search_button.grid(row=1, column=2)

generate_button = tk.Button(text="Generate Password", width=15, bg="white", font=("", 7, "normal"), command=pass_gen)
generate_button.grid(row=3, column=2)

add_button = tk.Button(text="Add", width=42, bg="white", command=info_saver)
add_button.grid(row=4, column=1, columnspan=2)

# with open("Data.json", "r") as data_file:
#     data = json.load(data_file)
#     print(data['facebook']['Email/User'])

window.mainloop()
