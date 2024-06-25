from tkinter import *

scr = Tk()
scr.geometry("150x200")

text = Label(scr, text="List:")
text.pack()
#creating the scroll bar
scrollbar = Scrollbar(scr)
scrollbar.pack(side="right")

l1 = Listbox(scr, yscrollcommand=scrollbar.set)
for i in range(1,20):
    l1.insert(END, "apple" + str(i))
l1.pack()
scrollbar.config(command=l1.yview)

scr.mainloop()






