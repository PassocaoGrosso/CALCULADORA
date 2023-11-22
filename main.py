#importando tkinter.
from tkinter import *
from tkinter import ttk

#COLORS
color1 = "#3b3b3b"
color2 = "#feffff"
color3 = "#38576b"
color4 = "#ECEFF1"
color5 = "#FFAB40"

window = Tk()
window.title("Calculator")
window.geometry("235x318")
window.config(bg=color1)

frame_window = Frame(window, width=235, height=50, bg=color3)
frame_window.grid(row=0, column=0)

frame_body = Frame(window, width=235, height=268)
frame_body.grid(row=1, column=0)

#Creating buttons

#C
b_1 = Button(frame_body, text="C", width=5,height=2)
b_1.place(x=0, y=0)

#%
b_2 = Button(frame_body, text="%", width=5,height=2)
b_2.place(x=50, y=0)


window.mainloop()
