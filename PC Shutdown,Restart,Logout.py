from tkinter import *
import os

root=Tk()
root.geometry("325x200")
root.title("PC-Shutdown,Restart,Logout")
root.config(bg='#E6E6FA')
f=('Arial,15,bold')

def shutdown():
    os.system("shutdown /s /t 0")
def restart():
    os.system("shutdown /r /t 0")
def logout():
    os.system("shutdown /l /t 0")

lb1=Label(root,text='Shutdown,Restart or Logout',font=(f),bg='#E6E6FA',fg='#303030')
lb1.pack(pady=5)

Button(root,text='Shutdown',font=(f),bg='#333333',fg='white',command=shutdown).pack(pady=5)
Button(root,text='Restart',font=(f),bg='#333333',fg='white',command=restart).pack(pady=5)
Button(root,text='Logout',font=(f),bg='#333333',fg='white',command=logout).pack(pady=5)

root.mainloop()
