from tkinter import *
from tkinter.ttk import *
window = Tk()
window.title("Drawing Calculator")
# default size and position
window.geometry("300x300")
# minimum size
window.minsize(200, 200)
# maximum size
window.maxsize(500, 500)
# making the whiteboard canvas
Grid.columnconfigure(window, index = 0,weight = 1)
Grid.rowconfigure(window, index=0, weight = 1)
my_canvas=Canvas(window,width=300, height=250, bg="white")
my_canvas.grid(row=0,column=0,sticky="NSEW")
#equation produced after input made
#sample holder
equation = Label(window,text="7+8")
equation.place(relx=0.35,y=10,anchor='n')
#label will be constant
equal = Label(window,text="=")
equal.place(relx=0.50,y=10,anchor='n')
#produce result of the equation
answer = Label(window,text="15")
answer.place(relx=0.60,y=10,anchor='n')
window.mainloop
