import json
from tkinter import *

from canvas import tk
from helpers import clean_screen
from products import render_products


def login(username, pword):
    with open("db/user_credentials_db.txt", "r") as file:
        data = file.readlines()
        for line in data:
            name, password = line.strip().split(", ")
            if name == username and pword == password:
                render_products()
                return

        render_login(error="Invalid username or password")


def register(**user):

    with open("db/user_credentials_db.txt", 'r') as users_db:
        for line in users_db:
            username, password = line.strip().split(", ")
            if user['username'] == username:
                return False

    user.update({"products": []})
    with open("db/users.txt", "a", newline='') as file:
        file.write(json.dumps(user))
        file.write("\n")
    with open("db/user_credentials_db.txt", "a", newline='') as file:
        file.write(f"{user['username']}, {user['password']}\n")
    render_login()
    return True


def render_login(error=None):
    clean_screen()
    Label(tk, text="Username").grid(row=0, column=0)
    username = Entry(tk)
    username.grid(row=0, column=1)
    Label(tk, text="Password").grid(row=1, column=0)
    password = Entry(tk)
    password.grid(row=1, column=1)

    if error is not None:
        Label(tk, text="Invalid username or password", fg="red").grid(row=3, column=1)
    Button(tk, text="Enter", bg="green", command=lambda: login(username.get(), password.get())).grid(row=2, column=1)


def render_register():
    clean_screen()
    Label(tk, text="Username").grid(row=0, column=0)
    username_entry = Entry(tk)
    username_entry.grid(row=0, column=1)
    Label(tk, text="Password").grid(row=1, column=0)
    password_entry = Entry(tk)
    password_entry.grid(row=1, column=1)
    Label(tk, text="First Name").grid(row=2, column=0)
    first_name_entry = Entry(tk)
    first_name_entry.grid(row=2, column=1)
    Label(tk, text="Last Name").grid(row=3, column=0)
    last_name_entry = Entry(tk)
    last_name_entry.grid(row=3, column=1)

    # Make validations for names length and username to be unique and with no special chars
    def on_register():
        if len(first_name_entry.get()) < 3:
            Label(tk, text="First Name should be minimum 3 letters", fg="red").grid(row=5, column=1)
            return
        result = register(username=username_entry.get(),
                          password=password_entry.get(),
                          first_name=first_name_entry.get(),
                          last_name=last_name_entry.get())
        if result:
            render_login()
        else:
            Label(tk, text="Email is already registered!", fg='red').grid(row=5, column=1)

    Button(tk,
           text="Register", bg="green", command=lambda: on_register()).grid(row=4, column=1)

    # Button(tk,
    #        text="Register", bg="green",
    #        command=lambda: register(username=username_entry.get(),
    #                                 password=password_entry.get(),
    #                                 first_name=first_name_entry.get(),
    #                                 last_name=last_name_entry.get())).grid(row=4, column=1)


def render_main_enter_screen():
    Button(tk, text="Login", bg="green", fg="white", command=render_login).grid(row=0, column=0)
    Button(tk, text="Register", bg="yellow", fg="black", command=render_register).grid(row=0, column=1, sticky="e")
