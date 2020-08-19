from tkinter import *

window = Tk()
window.title('displayenteredinfo')
window.geometry('300x400')

def myclicked():
    res = e1.get()
    res2 = e2.get()
    res3 = e3.get()
    Label(window, text=res).grid()
    Label(window, text=res2).grid()
    Label(window, text=res3).grid()


Label(window, text='Enter Name').grid(row=0, column=0)
e1= Entry(window, width=20)
e1.grid(row=0,column=1)
e1.focus()
Label(window, text='Enter age').grid(row=1, column=0)
e2 = Entry(window, width=20)
e2.grid(row=1, column=1)
Label(window, text='Enter class').grid(row=2, column=0)
e3= Entry(window, width=20)
e3.grid(row=2,column=1)
Button(window, text='click me', command=myclicked).grid(row=4, column=1)



window.mainloop()