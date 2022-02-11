
import tkinter
from tkinter import *
from tkinter import messagebox





# setting up the tkinter window
root = tkinter.Tk()
root.geometry("300x500+400+400")
root.resizable(0,0)
root.title("Surjo's calculator")

val=" "

A = 0
operator = ""

# function for numerical button clicked

def btn_1_isclicked():
    global val
    val = val + "1"
    data.set(val)

def btn_2_isclicked():
    global val
    val = val + "2"
    data.set(val)

def btn_3_isclicked():
    global val
    val = val + "3"
    data.set(val)

def btn_4_isclicked():
    global val
    val = val + "4"
    data.set(val)

def btn_5_isclicked():
    global val
    val = val + "5"
    data.set(val)

def btn_6_isclicked():
    global val
    val = val + "6"
    data.set(val)

def btn_7_isclicked():
    global val
    val = val + "7"
    data.set(val)

def btn_8_isclicked():
    global val
    val = val + "8"
    data.set(val)

def btn_9_isclicked():
    global val
    val = val + "9"
    data.set(val)

def btn_0_isclicked():
    global val
    val = val + "0"
    data.set(val)


# functions for the operator button click
def btn_plus_clicked():
    global A
    global operator,val
    A = float(val)
    operator = "+"
    val = val + "+"
    data.set(val)

def btn_minus_clicked():
    global A
    global operator,val
    A = float(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def btn_mult_clicked():
    global A
    global operator,val
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)

def btn_div_clicked():
    global A
    global operator,val
    A = float(val)
    operator = "/"
    val = val + "/"
    data.set(val)

def btn_c_pressed():
    global A,operator,val
    val = ""
    A = 0
    operator = ""
    data.set(val)
def btn_del_pressed():
    global val
    lista = []
    new_val = val
    for i in range(0, len(new_val)):
        lista.append(new_val[i])
    lista.pop()
    new_val = ''
    for i in lista:
        new_val += i
    val = new_val
    data.set(val)



def btn_dot_pressed():
    global A
    global operator, val
    A = float(val)
    operator = "."
    val = val + "."
    data.set(val)


# function to find the result
def result():
    global A,operator,val
    val2 = val
    if operator == "+":
        x = float((val2.split("+")[1]))
        C = A + x
        val = str(C)
        data.set(val)
    if operator == ".":
        x = float((val2.split(".")[1]))
        C = A + x
        val = str(C)
        data.set(val)
    if operator == "-":
        x = float((val2.split("-")[1]))
        C = A - x
        val = str(C)
        data.set(val)
    if operator == "*":
        x = float((val2.split("*")[1]))
        C = A * x
        val = str(C)
        data.set(val)
    if operator == "/":
        x = float((val2.split("/")[1]))
        if x == 0:
            messagebox.showerror("Error", "Division By 0 Not Supported")
            A = ""
            val = ""
            data.set(val)
        else:
            C = float(A / x)
            data.set(C)


# the label that shows the result
data = StringVar()
lbl = Label(
    root,
    text = "Label",
    anchor = SE,
    font = ("ds-digital", 20),
    textvariable = data,
    background = "#ffffff",
    fg = "#000000",
)
lbl.pack(expand = True, fill = "both")

# the frames section
btnrow1 = Frame(root)
btnrow1.pack(expand = True, fill = "both")

btnrow2 = Frame(root)
btnrow2.pack(expand = True, fill = "both")

btnrow3 = Frame(root)
btnrow3.pack(expand = True, fill = "both")

btnrow4 = Frame(root)
btnrow4.pack(expand = True, fill = "both")

btnrow5 = Frame(root)
btnrow5.pack(expand = True, fill = "both")

# The buttons section
btn1 = Button(
    btnrow1,
    text = "1",
    font = ("ds-digital", 22,'bold'),
    relief = GROOVE,
    border = 0,
    command = btn_1_isclicked,
)
btn1.pack(side = LEFT, expand = True, fill = "both",)

btn2 = Button(
    btnrow1,
    text = "2",
    font = ("ds-digital", 22),
    relief = GROOVE,
    border = 0,
    command = btn_2_isclicked,
)
btn2.pack(side = LEFT, expand = True, fill = "both",padx=16,pady=16)

btn3 = Button(
    btnrow1,
    text = "3",
    font = ("ds-digital", 22),
    relief = GROOVE,
    border = 0,
    command = btn_3_isclicked,
)
btn3.pack(side = LEFT, expand = True, fill = "both",)

btnplus = Button(
    btnrow1,
    text = "+",
    font = ("ds-digital", 22),
    relief = GROOVE,
    border = 0,
    command = btn_plus_clicked,
)
btnplus.pack(side = LEFT, expand = True, fill = "both",)

# buttons for frame 2

btn4 = Button(
    btnrow2,
    text = "4",
    font = ("ds-digital", 22),
    relief = GROOVE,
    border = 0,
    command = btn_4_isclicked,
)
btn4.pack(side = LEFT, expand = True, fill = "both",)

btn5 = Button(
    btnrow2,
    text = "5",
    font = ("ds-digital", 22),
    relief = GROOVE,
    border = 0,
    command = btn_5_isclicked,
)
btn5.pack(side = LEFT, expand = True, fill = "both",)

btn6 = Button(
    btnrow2,
    text = "6",
    font = ("ds-digital", 22),
    relief = GROOVE,
    border = 0,
    command = btn_6_isclicked,
)
btn6.pack(side = LEFT, expand = True, fill = "both",)

btnminus = Button(
    btnrow2,
    text = "-",
    font = ("ds-digital", 22),
    relief = GROOVE,
    border = 0,
    command = btn_minus_clicked,
)
btnminus.pack(side = LEFT, expand = True, fill = "both",)

# button for frame 3

btn7 = Button(
    btnrow3,
    text = "7",
    font = ("ds-digital", 22),
    relief = GROOVE,
    border = 0,
    command = btn_7_isclicked,
)
btn7.pack(side = LEFT, expand = True, fill = "both",)

btn8 = Button(
    btnrow3,
    text = "8",
    font = ("ds-digital", 22),
    relief = GROOVE,
    border = 0,
    command = btn_8_isclicked,
)
btn8.pack(side = LEFT, expand = True, fill = "both",)

btn9 = Button(
    btnrow3,
    text = "9",
    font = ("ds-digital", 22),
    relief = GROOVE,
    border = 0,
    command = btn_9_isclicked,
)
btn9.pack(side = LEFT, expand = True, fill = "both",)

btnmult = Button(
    btnrow3,
    text = "*",
    font = ("ds-digital", 22),
    relief = GROOVE,
    border = 0,
    command = btn_mult_clicked,
)
btnmult.pack(side = LEFT, expand = True, fill = "both",)

# button for frame4

btndot = Button(
    btnrow4,
    text = ".",
    font = ("ds-digital", 22),
    relief = GROOVE,
    border = 0,
    command = btn_dot_pressed,
)
btndot.pack(side = LEFT, expand = True, fill = "both",)

btnc = Button(
    btnrow5,
    text = "C",
    font = ("ds-digital", 22),
    relief = GROOVE,
    border = 0,
    command = btn_c_pressed,
)
btnc.pack(side = LEFT, expand = True, fill = "both",)

btn0 = Button(
    btnrow4,
    text = "0",
    font = ("ds-digital", 22),
    relief = GROOVE,
    border = 0,
    command = btn_0_isclicked,
)
btn0.pack(side = LEFT, expand = True, fill = "both",)

btnequal = Button(
    btnrow4,
    text = "=",
    font = ("ds-digital", 22),
    relief = GROOVE,
    border = 0,
    command = result,
)
btnequal.pack(side = LEFT, expand = True, fill = "both",)

btndiv = Button(
    btnrow4,
    text = "/",
    font = ("ds-digital", 22),
    relief = GROOVE,
    border = 0,
    command = btn_div_clicked,
)
btndiv.pack(side = LEFT, expand = True, fill = "both",)

btndel = Button(
    btnrow5,
    text = "⌫",
    font = ("ds-digital", 22),
    relief = GROOVE,
    border = 0,
    command = btn_del_pressed,
)
btndel.pack(side = LEFT, expand = True, fill = "both",)


root.mainloop()
