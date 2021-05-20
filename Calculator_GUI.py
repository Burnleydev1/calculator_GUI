#start program

from tkinter import *

root = Tk()
#root.geometry('355x475')
root.iconbitmap('logo.ico')
root.title("The Box ii group 9 Calculator")
root.resizable(False, False)

btn_param = {
    'bd': 1,
    'fg': 'green',
    'bg': '#000',
    'font': ('arial', 18),
    'width': 2,
    'height': 2,
    'relief': 'flat',
    'activebackground': "#000"
}
btn_params = {
    'padx': 15,
    'pady': 1,
    'bd': 4,
    'fg': 'white',
    'bg': '#0f0e0e',
    'font': ('arial', 20),
    'relief': 'flat',
    'width': 2,
    'height': 1,
    'activebackground': "#666666"
}
btn_operant = {
    'padx': 15,
    'pady': 1,
    'bd': 4,
    'fg': 'green',
    'bg': '#0f0e0e',
    'font': ('arial', 20),
    'relief': 'flat',
    'width': 2,
    'height': 1,
    'activebackground': "#666666"
}
btn_eq = {
    'padx': 15,
    'pady': 1,
    'bd': 4,
    'fg': 'white',
    'bg': 'green',
    'font': ('arial', 20),
    'relief': 'flat',
    'width': 2,
    'height': 1,
    'activebackground': "#666666"
}
root.configure(background='#000')

expression = ''
def btn_click(number):
    global expression

    expression = expression + str(number)
    equation.set(expression)

def btn_equal():
    global expression
    
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = ''
    except:
        equation.set('Math ERROR')
        expression = ''

def btn_clear():
    global expression
    expression = ''
    equation.set('|')

def btn_clear1():
    global expression
    expression = expression[:-1]
    equation.set(expression)

btn_sqrt = Button(root, **btn_param, text="√x", command=lambda: btn_click(9))
btn_dollar = Button(root, **btn_param, text="$", command=lambda: btn_click(9))
btn_sqrt.grid(row=0, column=3, sticky='W')
btn_dollar.grid(row=0, column=3, sticky='E')

equation = StringVar()
equation.set('|')
txt_display = Entry(root,textvariable=equation, relief='flat',font=('arial', 30), bg='black', fg='white', justify='right',width=12,)
txt_display.grid(row=1, column=0, columnspan=4, ipady=30)

btn_C = Button(root, **btn_operant, text="C", command=btn_clear)
btn_div = Button(root, **btn_operant, text="÷", command=lambda: btn_click('/'))
btn_mult = Button(root, **btn_operant, text="x", command=lambda: btn_click('*'))
btn_delete = Button(root, **btn_operant, text="cl", command=btn_clear1)

btn_7 = Button(root, **btn_params, text="7", command=lambda: btn_click(7))
btn_8 = Button(root, **btn_params, text="8", command=lambda: btn_click(8))
btn_9 = Button(root, **btn_params, text="9", command=lambda: btn_click(9))
btn_sub = Button(root, **btn_operant, text="-", command=lambda: btn_click('-'))

btn_4 = Button(root, **btn_params, text="4", command=lambda: btn_click(4))
btn_5 = Button(root, **btn_params, text="5", command=lambda: btn_click(5))
btn_6 = Button(root, **btn_params, text="6", command=lambda: btn_click(6))
btn_sum = Button(root, **btn_operant, text="+", command=lambda: btn_click('+'))


btn_1 = Button(root, **btn_params, text="1", command=lambda: btn_click(1))
btn_2 = Button(root, **btn_params, text="2", command=lambda: btn_click(2))
btn_3 = Button(root, **btn_params, text="3", command=lambda: btn_click(3))
btn_eq = Button(root, **btn_eq, text="=", command=btn_equal)

btn_percent = Button(root, **btn_params, text="%", command=lambda: btn_click('%'))
btn_0 = Button(root, **btn_params, text="0", command=lambda: btn_click(0))
btn_dot = Button(root, **btn_params, text=".", command=lambda: btn_click('.'))

btn_C.grid(row=2, column=0,)
btn_div.grid(row=2, column=1)
btn_mult.grid(row=2, column=2)
btn_delete.grid(row=2, column=3)

btn_7.grid(row=3, column=0)
btn_8.grid(row=3, column=1)
btn_9.grid(row=3, column=2)
btn_sub.grid(row=3, column=3)

btn_4.grid(row=4, column=0)
btn_5.grid(row=4, column=1)
btn_6.grid(row=4, column=2)
btn_sum.grid(row=4, column=3)

btn_1.grid(row=5, column=0)
btn_2.grid(row=5, column=1)
btn_3.grid(row=5, column=2)
btn_eq.grid(row=5, column=3, rowspan=2, ipady=30)

btn_percent.grid(row=6, column=0)
btn_0.grid(row=6, column=1)
btn_dot.grid(row=6, column=2)



root.mainloop()