from tkinter import *
import random
import string

top = Tk()
top.title('CRUD MySQL')
top.geometry('430x400')

def CreateOperation():
    from create import InsertData

    top1 = Tk()
    top1.geometry('300x200')
    top1.title('CRUD')

    name = StringVar(top1)
    email = StringVar(top1)

    Label(top1, text='Nome').grid(row=0, column=0, padx=20, pady=20, sticky='w')
    Entry(top1, textvariable=name).grid(row=0, column=1, padx=20)

    Label(top1, text='email').grid(row=1, padx=20, column=0, sticky='w')
    Entry(top1, textvariable=email).grid(row=1, column=1)

    Button(top1, text='Criar', fg='white', bg='green', font=('Arial', 20), command=lambda: InsertData(name.get(), email.get())).grid(row=2, column=0, columnspan=2, pady=20)

    top1.mainloop()


Button(top, text='Create', bg='green', fg='white', width=12, font=('Arial', 18), command=lambda: CreateOperation()).grid(row=0, column=0, padx=25, pady=30)


top.mainloop()
		