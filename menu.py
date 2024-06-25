from tkinter import *

scr = Tk()
scr.geometry("300x150")
scr.title("menus")

text = Label(scr, text="chocolate icecream", font="45")
text.pack()

frame = Frame(scr)
frame.pack()
bot_frame = Frame(scr)
bot_frame.pack(side=BOTTOM)

btn1 = Button(frame, text="Banana split", bg="brown", fg="black")
btn1.pack(side=LEFT)

btn2 = Button(frame, text="Rocky mountain", bg="brown", fg="black")
btn2.pack(side=LEFT)

btn3 = Button(bot_frame, text="Bubble gum", bg="pink", fg="black")
btn3.pack(side=LEFT)

scr.mainloop()





