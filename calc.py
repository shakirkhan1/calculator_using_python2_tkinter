from Tkinter import *

root=Tk()
root.title('MYCLALCULATOR')
e=Entry(root,width=16,bd=10,font="times 32 bold",justify='right')
e.grid(row=0,column=1,columnspan=4)#spanning columnwise

def insert(x):
    e.insert(16,x)# 16 is for rightmost position

def result():
    y=eval(e.get())
    e.delete(0,END)# deletes all characters from positon 0 to end
    e.insert(16,y)

def clear():
    e.delete(0,END)
    

Button(root,text="9",width=7,height=3,font="times 20 bold",activebackground='light blue',bd=5,fg='blue',command=lambda:insert(9)).grid(row=1,column=0)
Button(root,text="8",width=7,height=3,font="times 20 bold",activebackground='light blue',bd=5,fg='blue',command=lambda:insert(8)).grid(row=1,column=1)
Button(root,text="7",width=7,height=3,font="times 20 bold",activebackground='light blue',bd=5,fg='blue',command=lambda:insert(7)).grid(row=1,column=2)
Button(root,text="C",width=7,height=3,font="times 20 bold",activebackground='light blue',bd=5,fg='red',command=clear).grid(row=1,column=3)
Button(root,text="6",width=7,height=3,font="times 20 bold",activebackground='light blue',bd=5,fg='blue',command=lambda:insert(6)).grid(row=2,column=0)
Button(root,text="5",width=7,height=3,font="times 20 bold",activebackground='light blue',bd=5,fg='blue',command=lambda:insert(5)).grid(row=2,column=1)
Button(root,text="4",width=7,height=3,font="times 20 bold",activebackground='light blue',bd=5,fg='blue',command=lambda:insert(4)).grid(row=2,column=2)
Button(root,text="+",width=7,height=3,font="times 20 bold",activebackground='light blue',bd=5,fg='black',command=lambda:insert('+')).grid(row=2,column=3)
Button(root,text="3",width=7,height=3,font="times 20 bold",activebackground='light blue',bd=5,fg='blue',command=lambda:insert(3)).grid(row=3,column=0)
Button(root,text="2",width=7,height=3,font="times 20 bold",activebackground='light blue',bd=5,fg='blue',command=lambda:insert(2)).grid(row=3,column=1)
Button(root,text="1",width=7,height=3,font="times 20 bold",activebackground='light blue',bd=5,fg='blue',command=lambda:insert(1)).grid(row=3,column=2)
Button(root,text="-",width=7,height=3,font="times 20 bold",activebackground='light blue',bd=5,fg='black',command=lambda:insert('-')).grid(row=3,column=3)
Button(root,text="0",width=7,height=3,font="times 20 bold",activebackground='light blue',bd=5,fg='blue',command=lambda:insert(0)).grid(row=4,column=0)
Button(root,text=".",width=7,height=3,font="times 20 bold",activebackground='light blue',bd=5,fg='black',command=lambda:insert('.')).grid(row=4,column=1)
Button(root,text="=",width=7,height=3,font="times 20 bold",activebackground='light blue',bd=5,fg='black',command=result).grid(row=4,column=2)
Button(root,text="/",width=7,height=3,font="times 20 bold",activebackground='light blue',bd=5,fg='black',command=lambda:insert('/')).grid(row=4,column=3)

root.mainloop()
