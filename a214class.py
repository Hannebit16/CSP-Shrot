import tkinter as tk

def login():
    print("username is :",user_box.get())
    print("password is :",pass_box.get())


root = tk.Tk()
root.geometry("300x250")
root.title("Login Practice")

user_label = tk.Label(root, text="username:")
user_label.pack()

user_box = tk.Entry(root)
user_box.pack()

pass_label = tk.Label(root, text="password:")
pass_label.pack()

pass_box = tk.Entry(root)
pass_box.pack()

log_button = tk.Button(root,text = "login", command=login)
log_button.pack()


root.mainloop()