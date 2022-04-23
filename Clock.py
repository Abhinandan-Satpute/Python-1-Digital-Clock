#Digital Clock
from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("-->* Digital Clock *<--")

def gettime():
	stime = strftime("%I:%M:%S %p") #%H:24-Hour Clock and %I:12-Hour Clock
	label.config(text=stime)
	label.after(1000,gettime)



label = Label(root,font=("Algerian",80),background="black",foreground="cyan")
label.pack(anchor="center")
gettime()
mainloop()