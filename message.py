from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("300x200")

w=Label(root,text="Messagebox")
w.pack()

# messagebox.showinfo("showinfo","Information")
messagebox.askyesno("askyesno","Are you sure")
# messagebox.showinfo("showinfo","Information")
# messagebox.showinfo("showinfo","Information")
# messagebox.showinfo("showinfo","Information")
root.mainloop()