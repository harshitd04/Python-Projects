from tkinter import *
from tkinter import messagebox
import pyperclip
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_random_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters_list = [random.choice(letters) for i in range(random.randint(8, 10))]
    password_numbers_list = [random.choice(numbers) for i in range(random.randint(2, 4))]
    password_symbols_list = [random.choice(symbols) for i in range(random.randint(2, 4))]

    password_list = password_symbols_list + password_numbers_list + password_letters_list

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data_to_file():
    website_data = website_input.get()
    email_data = email_input.get()
    password_data = password_input.get()

    if len(website_data)== 0 or len(email_data)== 0 or len(password_data) == 0:
        messagebox.showerror(title="Empty Field",message="Please don't leave any fields empty.")

    else:
        save_data = messagebox.askokcancel(title=website_data,message=f"These are the details entered:\n"
                                                          f"Email:{email_data}\nPassword:{password_data}\nSave Data?")
        if save_data:
            with open("data.txt","a") as password_file:
                password_file.write(f"{website_data} | {email_data} | {password_data}\n")
                website_input.delete(0,END)
                password_input.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=40,pady=40)

canvas = Canvas(width=200,height=200,highlightthickness=1)
image_for_canvas = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=image_for_canvas)
canvas.grid(row=0,column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)
password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

#Entries
website_input = Entry(width=35)
website_input.grid(row=1,column=1,columnspan=2)
website_input.focus()

email_input = Entry(width=35)
email_input.grid(row=2,column=1,columnspan=2)
email_input.insert(0, "abc@gmail.com")

password_input = Entry(width=21)
password_input.grid(row=3,column=1)

#Buttons
generate_button = Button(text="Generate Password",command=generate_random_password)
generate_button.grid(row=3,column=2)
add_button = Button(text="Add",width=36,command=add_data_to_file)
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()




