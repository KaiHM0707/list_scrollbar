from tkinter import *

scr = Tk()
scr.geometry("300x250")
scr.title("Places to go")
sign = Label(scr, text="places:")
sign.pack()
#Create a list
l1 = Listbox(scr, height=10, width=15, bg="lightgreen", fg="black", font="Helvetica", activestyle="dotbox")
l1.insert(1,"Seattle")
l1.insert(2,"London")
l1.insert(3,"Germany")
l1.insert(4,"Tokyo")
l1.insert(5,"Bozeman")
l1.insert(6,"Silicon valley")
l1.pack()



scr.mainloop()