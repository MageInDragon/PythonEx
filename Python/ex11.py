from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import Menu
from tkinter import scrolledtext

window = Tk()
window.title("Безлепкин К.В.")
window.geometry('900x350')
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Калькулятор')
tab_control.add(tab2, text='Чекбоксы')
tab_control.add(tab3, text='Текст')
tab_control.pack(expand=1, fill='both')

#tab1

def calcclick():
    if(oper.get() == '+'):
        ans = int(num1.get()) + int(num2.get())
        answer.configure(text=ans)
    elif(oper.get() == '-'):
        ans = int(num1.get()) - int(num2.get())
        answer.configure(text=ans)
    elif(oper.get() == '*'):
        ans = int(num1.get()) * int(num2.get())
        answer.configure(text=ans)
    else:
        ans = int(num1.get()) / int(num2.get())
        answer.configure(text=ans)
    

num1 = Entry(tab1, width=5)
num2 = Entry(tab1, width=5)
num1.grid(column=0,row=0)
num2.grid(column=2,row=0)
oper = Combobox(tab1)
oper['values'] = ('+','-','*','/')
oper.current(0)
oper.grid(column=1,row=0)
calc = Button(tab1, text="=", command=calcclick)
calc.grid(column=3,row=0)
answer = Label(tab1, text='')
answer.grid(column=4,row=0)

#tab2

def checkboxclicked():
    if(selected.get() == 1):
         lbl.configure(text="Вы выбрали первый вариант")
    elif(selected.get() == 2):
         lbl.configure(text="Вы выбрали второй вариант")
    elif(selected.get() == 3):
         lbl.configure(text="Вы выбрали третий вариант")
 

selected = IntVar()
rad1 = Radiobutton(tab2,text='Первый', value=1,
variable=selected)
rad2 = Radiobutton(tab2,text='Второй', value=2,
variable=selected)
rad3 = Radiobutton(tab2,text='Третий', value=3,
variable=selected)
btn = Button(tab2, text="Клик", command=checkboxclicked)
lbl = Label(tab2)
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
btn.grid(column=3, row=0)
lbl.grid(column=4, row=0)

#tab3

txt = scrolledtext.ScrolledText(tab3, width=40, height=10)
txt.grid(column=0, row=0)
    
def opentext():
    with open('BKV_Ym232_vvod11.txt','r') as textfile:
        txt.insert(INSERT, textfile.read())
    




menu = Menu(window)
new_item = Menu(menu,tearoff=0)
new_item.add_command(label='Открыть', command=opentext)
menu.add_cascade(label='Файл', menu=new_item)
window.config(menu=menu)  


window.mainloop()
