
from  tkinter import *
from  tkinter.ttk import *
from time import strftime

root=Tk()
root.title("Surjo's Clock")

def time():
    string=strftime('%I:%M:%S  %p')
    label.config(text=string)
    label.after(200,time)



label=Label(root,font=("ds-digital",80),background="black",foreground ="green")
label.pack(anchor='center')
time()

root.mainloop()

