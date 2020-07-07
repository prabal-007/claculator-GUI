from tkinter import *

root=Tk()
root.title('Calculator by Prabal')
root.geometry('400x500')
root.configure(background='black')
def click(event):
    global var
    text = event.widget.cget('text')
    if text == '=':
        if var.get().isdigit():
            value = int(var.get())
        else:
            value = eval(var.get())
        var.set(value)
        screen.update()

    elif text == 'Er':
        pass

    elif text == 'c':
        var.set("") 
        screen.update()
    else:
        try:
            var.set(var.get() + text)
            screen.update()
        except Exception as e:
            print(e)

var = StringVar()
var.set('')
screen = Entry(root, textvariable=var, font='lucida 35 bold').pack(fill=X, padx='8', pady='10')

frm1 = Frame(root, bg='grey')
b1 = Button(frm1, text='c', font='lucida 30 bold')
b1.pack(side=RIGHT, padx='3', pady='5')
b1.bind('<Button-1>', click)

b2=Button(frm1, text='Er', font='lucida 30 bold')
b2.pack(side=RIGHT, padx='3', pady='5')
b2.bind('<Button-1>', click)

b3=Button(frm1, text='%', font='lucida 30 bold')
b3.pack(side=RIGHT, padx='3', pady='5')
b3.bind('<Button-1>', click)

b4=Button(frm1, text='/', font='lucida 30 bold')
b4.pack(side=RIGHT, padx='3', pady='5')
b4.bind('<Button-1>', click)
frm1.pack()

frm1 = Frame(root, bg='grey')
b1 = Button(frm1, text='9', font='lucida 30 bold')
b1.pack(side=RIGHT, padx='3', pady='5')
b1.bind('<Button-1>', click)

b2=Button(frm1, text='8', font='lucida 30 bold')
b2.pack(side=RIGHT, padx='3', pady='5')
b2.bind('<Button-1>', click)

b3=Button(frm1, text='7', font='lucida 30 bold')
b3.pack(side=RIGHT, padx='3', pady='5')
b3.bind('<Button-1>', click)

b4=Button(frm1, text='X', font='lucida 30 bold')
b4.pack(side=RIGHT, padx='3', pady='5')
b4.bind('<Button-1>', click)
frm1.pack()

frm1 = Frame(root, bg='grey')
b1 = Button(frm1, text='6', font='lucida 30 bold')
b1.pack(side=RIGHT, padx='3', pady='5')
b1.bind('<Button-1>', click)

b2=Button(frm1, text='5', font='lucida 30 bold')
b2.pack(side=RIGHT, padx='3', pady='5')
b2.bind('<Button-1>', click)

b3=Button(frm1, text='4', font='lucida 30 bold')
b3.pack(side=RIGHT, padx='3', pady='5')
b3.bind('<Button-1>', click)

b4=Button(frm1, text='-', font='lucida 30 bold')
b4.pack(side=RIGHT, padx='3', pady='5')
b4.bind('<Button-1>', click)
frm1.pack()

frm1 = Frame(root, bg='grey')
b1 = Button(frm1, text='3', font='lucida 30 bold')
b1.pack(side=RIGHT, padx='3', pady='5')
b1.bind('<Button-1>', click)

b2=Button(frm1, text='2', font='lucida 30 bold')
b2.pack(side=RIGHT, padx='3', pady='5')
b2.bind('<Button-1>', click)

b3=Button(frm1, text='1', font='lucida 30 bold')
b3.pack(side=RIGHT, padx='3', pady='5')
b3.bind('<Button-1>', click)

b4=Button(frm1, text='+', font='lucida 30 bold')
b4.pack(side=RIGHT, padx='3', pady='5')
b4.bind('<Button-1>', click)
frm1.pack()

frm1 = Frame(root, bg='grey')
b1 = Button(frm1, text='Q', font='lucida 30 bold', command=quit)
b1.pack(side=RIGHT, padx='3', pady='5')

b2=Button(frm1, text='0', font='lucida 30 bold')
b2.pack(side=RIGHT, padx='3', pady='5')
b2.bind('<Button-1>', click)

b3=Button(frm1, text='.', font='lucida 30 bold')
b3.pack(side=RIGHT, padx='3', pady='5')
b3.bind('<Button-1>', click)

b4=Button(frm1, text='=', font='lucida 30 bold')
b4.pack(side=RIGHT, padx='3', pady='5')
b4.bind('<Button-1>', click)
frm1.pack()

root.mainloop()