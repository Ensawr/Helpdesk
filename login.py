from tkinter import *
from tkinter import font
import tkinter.messagebox
import mysql.connector
import os
os.system('cls')
currDir = os.getcwd()

db = mysql.connector.connect(
  host="localhost",
  database="helpdesk",
  user="root",
  password=""
)

root = Tk()
root.title("Helpdesk - Login")
root.geometry("300x230")
root.configure(bg='#d1d1d1')

def checkUser():
    userData = login_txtbox.get()
    passData = pass_txtbox.get()
    dbquery = db.cursor(buffered=True)
    dbquery.execute("SELECT username FROM users where username=%s and password=%s",(userData,passData))
    data = dbquery.fetchall()
    if(len(data)<1):
      tkinter.messagebox.showwarning("Warning!",  "Username or password incorrect!")
    else:
      tkinter.messagebox.showinfo("Welcome",  "Welcome "+userData)

def goRegister():
    register = currDir+"/register.py"
    os.system('"%s"' % register)

fontStyle = font.Font(family="Arial", size=11)

loginLabel = Label(root, text="Username", font=fontStyle)
loginLabel.configure(background="#d1d1d1")
loginLabel.pack(pady=5)

login_txtbox = Entry(root, width=30)
login_txtbox.pack()

passLabel = Label(root, text="Password", font=fontStyle)
passLabel.configure(background="#d1d1d1")
passLabel.pack(pady=5)

pass_txtbox = Entry(root, width=30, show="*")
pass_txtbox.pack()

loginButton = Button(root, width=10, text="Login", command=lambda: checkUser())
loginButton.configure(bg="#7d7d7d", fg="#ffffff")
loginButton.pack(pady=20)

registerButton = Button(root, width=10, text="Sign Up", command=lambda: goRegister())
registerButton.configure(bg="#7d7d7d", fg="#ffffff")
registerButton.pack()

root.mainloop()

