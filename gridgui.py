from tkinter import *
parent=Tk()
parent.geometry("400x250")
name=Label(parent,text="Name").grid(row=0,column=0)
e1=Entry(parent).grid(row=0,column=1)
password=Label(parent,text="Password").grid(row=2,column=0)
e2=Entry(parent).grid(row=2,column=1)
submit=Button(parent,text="Submit").grid(row=4,column=1)
parent.mainloop()