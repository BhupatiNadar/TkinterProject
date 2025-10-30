import sqlite3
from tkinter import *
from tkinter import messagebox


window = Tk()
window.title("Login Form")


con = sqlite3.connect("address_book.db")
c = con.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS users(
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
""")
con.commit()
con.close()


def login():
    username = InputName.get()
    password = InputPassword.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "All fields are required")
        return

    con = sqlite3.connect("address_book.db")
    c = con.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    con.close()

    if result:
        messagebox.showinfo("Success", f"Welcome, {username}!")
    else:
        messagebox.showerror("Error", "Invalid username or password")


def register():
    newregister = Toplevel(window)
    newregister.title("Register")
    newregister.geometry("350x200")

    Label(newregister, text="User Name:").grid(row=0, column=0, padx=10, pady=10)
    reg_name = Entry(newregister, width=30)
    reg_name.grid(row=0, column=1, pady=10)

    Label(newregister, text="Password:").grid(row=1, column=0, padx=10, pady=10)
    reg_pass = Entry(newregister, width=30, show="*")
    reg_pass.grid(row=1, column=1, pady=10)

    def submit_register():
        name = reg_name.get()
        pwd = reg_pass.get()

        if name == "" or pwd == "":
            messagebox.showerror("Error", "All fields are required")
            return

        con = sqlite3.connect("address_book.db")
        c = con.cursor()
        try:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (name, pwd))
            con.commit()
            messagebox.showinfo("Success", "Registration successful!")
            newregister.destroy()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists")
        con.close()

    Submit = Button(newregister, text="Submit", command=submit_register)
    Submit.grid(row=2, column=1, pady=10)

Label(window, text="User Name:").grid(row=0, column=0, padx=10, pady=10)
InputName = Entry(window, width=30)
InputName.grid(row=0, column=1, columnspan=2, pady=10)

Label(window, text="Password:").grid(row=1, column=0, padx=10, pady=10)
InputPassword = Entry(window, width=30, show="*")
InputPassword.grid(row=1, column=1, columnspan=2, pady=10)

Login = Button(window, text="Login", command=login)
Login.grid(row=2, column=1, pady=10)

Register = Button(window, text="Register", command=register)
Register.grid(row=2, column=2, pady=10)

window.mainloop()
