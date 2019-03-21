from Tkinter import *
from math import *
root=Tk()
root.title('CALCULATOR')
e=Entry(root, width=28, font='Arial 30 bold', bd=7, relief='sunken', bg='light grey', justify='right')
e.grid(row=0, column=0, columnspan=4)
def add_entry(x):
    e.insert(28, x)
def result(y):
    e.delete(0, END)
    e.insert(28, y)
def clear():
    e.delete(0, END)
def backspace():
    e.delete(len(e.get())-1,END)
Button(root, text='7',font='Bodoni 10 bold', width=10, height=5, command=lambda: add_entry('7')).grid(row=1,column=0, sticky=E+W+N+S)
Button(root, text='8',font='Bodoni 10 bold' ,width=10, height=5, command=lambda: add_entry('8')).grid(row=1,column=1, sticky=E+W+N+S)
Button(root, text='9',font='Bodoni 10 bold' ,width=10, height=5, command=lambda: add_entry('9')).grid(row=1,column=2, sticky=E+W+N+S)
Button(root, text='+',font='Bodoni 10 bold' ,width=10, height=5, command=lambda: add_entry('+')).grid(row=2,column=3, sticky=E+W+N+S)

Button(root, text='4',font='Bodoni 10 bold' ,width=10, height=5, command=lambda: add_entry('4')).grid(row=2,column=0, sticky=E+W+N+S)
Button(root, text='5',font='Bodoni 10 bold' ,width=10, height=5, command=lambda: add_entry('5')).grid(row=2,column=1, sticky=E+W+N+S)
Button(root, text='6',font='Bodoni 10 bold' ,width=10, height=5, command=lambda: add_entry('6')).grid(row=2,column=2, sticky=E+W+N+S)
Button(root, text='-',font='Bodoni 10 bold' ,width=10, height=5, command=lambda: add_entry('-')).grid(row=3,column=3, sticky=E+W+N+S)

Button(root, text='1',font='Bodoni 10 bold' ,width=10, height=5, command=lambda: add_entry('1')).grid(row=3,column=0, sticky=E+W+N+S)
Button(root, text='2',font='Bodoni 10 bold', width=10, height=5, command=lambda: add_entry('2')).grid(row=3,column=1, sticky=E+W+N+S)
Button(root, text='3',font='Bodoni 10 bold', width=10, height=5, command=lambda: add_entry('3')).grid(row=3,column=2, sticky=E+W+N+S)
Button(root, text='0',font='Bodoni 10 bold', width=10, height=5, command=lambda: add_entry('0')).grid(row=4,column=0, sticky=E+W+N+S)

Button(root, text='*',font='Bodoni 10 bold', width=10, height=5, command=lambda: add_entry('*')).grid(row=5,column=2, sticky=E+W+N+S)
Button(root, text='/',font='Bodoni 10 bold', width=10, height=5, command=lambda: add_entry('/')).grid(row=4,column=3, sticky=E+W+N+S)
Button(root, text='.',font='Bodoni 10 bold', width=10, height=5, command=lambda: add_entry('.')).grid(row=4,column=1, sticky=E+W+N+S)

Button(root,text='cos',font='Bodoni 10 bold',width=10,height=5,command=lambda:add_entry('cos(')).grid(row=6,column=1,sticky=E+W+N+S)
Button(root,text='sin',font='Bodoni 10 bold',width=10,height=5,command=lambda:add_entry('sin(')).grid(row=6,column=0,sticky=E+W+N+S)
Button(root,text='tan',font='Bodoni 10 bold',width=10,height=5,command=lambda:add_entry('tan(')).grid(row=6,column=2,sticky=E+W+N+S)
Button(root,text='log',font='Bodoni 10 bold',width=10,height=5,command=lambda:add_entry('log(')).grid(row=6,column=3,sticky=E+W+N+S)

Button(root,text=',',font='Bodoni 10 bold',width=10,height=5,command=lambda:add_entry(',')).grid(row=4,column=2,sticky=E+W+N+S)
Button(root,text='sqrt',font='Bodoni 10 bold',width=10,height=5,command=lambda:add_entry('sqrt(')).grid(row=7,column=1,sticky=E+W+N+S)
Button(root,text='pi',font='Bodoni 10 bold',width=10,height=5,command=lambda:add_entry('pi')).grid(row=7,column=2, sticky=E+W+N+S)
Button(root, text='del', font='Bodoni 10 bold',width=10, height=5, command=lambda: backspace()).grid(row=7,column=3, sticky=E+W+N+S)
Button(root, text='C', font='Bodoni 10 bold',width=10, height=5, command=lambda: clear()).grid(row=1,column=3, sticky=E+W+N+S)
Button(root, text='=', font='Bodoni 10 bold',width=10, height=5, command=lambda: result(eval(e.get()))).grid(row=5,column=3, sticky=E+W+N+S)
Button(root, text='Power', font='Bodoni 10 bold',width=10, height=5, command=lambda: add_entry('**')).grid(row=7,column=0, sticky=E+W+N+S)
Button(root, text='(', font='Bodoni 10 bold',width=10, height=5, command=lambda: add_entry('(')).grid(row=5,column=0, sticky=E+W+N+S)
Button(root, text=')', font='Bodoni 10 bold',width=10, height=5, command=lambda: add_entry(')')).grid(row=5,column=1, sticky=E+W+N+S)
root.mainloop()
