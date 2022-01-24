from tkinter import *
from tkinter import font
import tkinter.messagebox
import mysql.connector
import os
os.system('cls')

db = mysql.connector.connect(
  host="localhost",
  database="helpdesk",
  user="root",
  password=""
)

root = Tk()
root.title("Helpdesk - Register")
root.geometry("300x250")
root.configure(bg='#d1d1d1')

def createUser():
    nsData = ns_txtbox.get()
    userData = user_txtbox.get()
    passData = pass_txtbox.get()

    dbquery = db.cursor()
    dbquery.execute("SELECT username FROM users where username=%s",(userData,))
    validate = dbquery.fetchall()

    if(len(validate)>0):
        tkinter.messagebox.showwarning("Warning!",  "Username is already taken")
    elif(len(nsData)<1 or len(userData)<1 or len(passData)<1):
        tkinter.messagebox.showwarning("Warning!",  "All inputs must be filled")
    elif(len(passData)<6):
        tkinter.messagebox.showwarning("Warning!",  "Password should be longer")
    else:
        dbquery = db.cursor()
        sql = "insert into users(name,username,password) values(%s,%s,%s)"
        vals = (nsData,userData,passData)
        dbquery.execute(sql,vals)
        db.commit()
        tkinter.messagebox.showinfo("Success!",  "User created.", parent=root, command=root.quit())

fontStyle = font.Font(family="Arial", size=11)

nsLabel = Label(root, text="Name Surname", font=fontStyle)
nsLabel.configure(background="#d1d1d1")
nsLabel.pack(pady=5)

ns_txtbox = Entry(root, width=30)
ns_txtbox.pack()

userLabel = Label(root, text="Username", font=fontStyle)
userLabel.configure(background="#d1d1d1")
userLabel.pack(pady=5)

user_txtbox = Entry(root, width=30)
user_txtbox.pack()

passLabel = Label(root, text="Password", font=fontStyle)
passLabel.configure(background="#d1d1d1")
passLabel.pack(pady=5)

pass_txtbox = Entry(root, width=30, show="*")
pass_txtbox.pack()

registerButton = Button(root, width=10, text="Register", command=lambda: createUser())
registerButton.configure(bg="#7d7d7d", fg="#ffffff")
registerButton.pack(pady=20)

root.mainloop()