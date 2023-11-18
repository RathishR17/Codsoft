
#Python Simple Calculator Using Tkinter(GUI)
from tkinter import *
import math

rathish=Tk()  #Creating a window for using Calculator
rathish.geometry("421x460")  #Size
rathish.resizable(0,0) #preventing from resizing
rathish.title("Calculator by Rathish") # Title

#Button Functions click which enables the user to give input,[we can also know the button is working]

def btn_click(item):
    global expression
    expression=expression+str(item)
    input_text.set(expression)
#Clear used to clear the inputs so that we can calculate new one
def btn_clear():
    global expression
    expression= ""
    input_text.set("")
#Equal buuton to get the answers
def btn_equal():
    global expression
    result=str(eval(expression))  #evaluating the expresion and storing in the result variable
    input_text.set(result)
    expression= ""

def btn_square_root():
    global expression
    expression="math.sqrt("+expression+")"   #To find the square root
    input_text.set(expression)

def btn_power():
    global expression
    expression="math.pow("+ expression +",2)"  #To find the power of the input
    input_text.set(expression)

def btn_exp():
    global expression
    expression="math.exp("+expression+")"   #To find the square root
    input_text.set(expression)

expression = ""

# 'StringVar()' :It is used to get the instance of input field
input_text = StringVar()

# Let us creating a frame for the input field

input_frame = Frame(rathish, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black",highlightthickness=3)

input_frame.pack(side=TOP)

# Let us create a input field inside the 'Frame'

input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0,justify=RIGHT)

input_field.grid(row=0, column=0)

input_field.pack(ipady=20)  # 'ipady' is internal padding to increase the height of input field

btns_frame = Frame(rathish, width=312, height=272.5, bg="grey")
btns_frame.pack()

# first row

clear =Button(btns_frame,text="C", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2",command=lambda: btn_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)

divide = Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click("/")).grid(row=0, column=3, padx=1, pady=1)

# second row

seven = Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)

eight = Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)

nine = Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)

multiply = Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",command=lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1)

# third row

four = Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)

five = Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)

six = Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)

minus = Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_click("-")).grid(row=2, column=3, padx=1, pady=1)

# fourth row

one = Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)

two = Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)

three = Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)

plus = Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",command=lambda: btn_click("+")).grid(row=3, column=3, padx=1, pady=1)

# fourth row

zero = Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2",command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

point = Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1)

equals = Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",command=lambda: btn_equal()).grid(row=4, column=3, padx=1, pady=1)

# fifth row
sqrt = Button(btns_frame, text='√', fg='black', bg='yellow', width=5,command=lambda: btn_square_root()).grid(row=5, column=1,columnspan=1, pady=1)

power = Button(btns_frame, text='^', fg='black', bg='yellow', width=5,command=lambda: btn_power()).grid(row=5, column=2, pady=1)

exp = Button(btns_frame, text='exp', fg='black', bg='yellow', width=5,command=lambda: btn_exp()).grid(row=5, column=3, pady=1)

rathish.mainloop()