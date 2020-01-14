import tkinter as tk

def uppercase(password):
    for char in password:
        if char.isupper():
            return True

def lowercase(password):
    for char in password:
        if char.islower():
            return True

def digit(password):
    for char in password:
        if char.isdigit():
            return True

def sc(password):
    for char in password:
        if char in sclist:
            return True

def login():
    password = pass_box.get()
    if len(password) >= 8 and uppercase(password) and lowercase(password) and digit(password): 
        print("username is :",user_box.get())
        print("password is :",pass_box.get())
    else:
        print('your password must be at least 8 characters, an upercase and lowercase letter, and a digit')


root = tk.Tk()
root.geometry("300x250")
root.title("Login Practice")

user_label = tk.Label(root, text="username:")
user_label.pack()

user_box = tk.Entry(root)
user_box.pack()

pass_label = tk.Label(root, text="password:")
pass_label.pack()

pass_box = tk.Entry(root, show='*')
pass_box.pack()

log_button = tk.Button(root,text = "login", command=login)
log_button.pack()


root.mainloop()
