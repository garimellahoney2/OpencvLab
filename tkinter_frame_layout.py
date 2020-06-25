from tkinter import *
root = Tk()#represents screen
"""
The fill option tells the manager that the widget wants fill the entire space assigned to it. The value controls how to fill the space;
BOTH means that the widget should expand both horisontally and vertically
"""
x = Label(root,text="manvi")
fm = Frame(root)
fm.pack(fill=BOTH)

Button(fm,text = "button",fg="red").pack()
Button(fm,text = "button1",fg="green").pack()
Button(fm,text = "button2",fg="blue").pack(side = RIGHT)
x.pack()#is like wrap content #wrap_content is used when we want the view to occupy only as much space as required by it

root.mainloop()#is like loop to not stop the program
