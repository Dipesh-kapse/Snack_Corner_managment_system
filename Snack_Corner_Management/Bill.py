from tkinter import *
from tkinter import messagebox

win=Tk()
win.geometry('1160x670+60+0')
win.title('Billing System')

title=Label(win,text='Billing System',font=('times new roman',30,'bold'),fg='dark blue',bg='powder blue',width=50)
title.grid(row=0,column=3)

#~~~~~~~~~~~~~~~~~~~~~variables~~~~~~
Pizza=IntVar()
Burger=IntVar()
French_Fries=IntVar()
Coffee=IntVar()
Chinese=IntVar()
total=IntVar()

cp=StringVar()
cb=StringVar()
cf=StringVar()
cc=StringVar()
cch=StringVar()
total_cost=StringVar()

#~~~~~~~Function~~~~~~~~~~~~
def Total():
    if Pizza.get()==0 and Burger.get()==0 and French_Fries.get()==0 and Coffee.get()==0 and Chinese.get()==0:
        messagebox.showerror('Error','Please Select Number of Quantity')
    else:
        p=Pizza.get()
        b=Burger.get()
        f=French_Fries.get()
        c=Coffee.get()
        ch=Chinese.get()

        t=float(p*99+b*70+f*55+c*30+ch*60)
        total.set(p+b+f+c+ch)
        total_cost.set(str(round(t,2)))

        cp.set('₹' + str(round(p * 99.00, 2)))
        cb.set('₹' + str(round(b * 70.00, 2)))
        cf.set('₹' + str(round(f * 55.00, 2)))
        cc.set('₹' + str(round(c * 30.00, 2)))
        cch.set('₹' + str(round(ch * 60.00, 2)))

def reciept():
    txtarea.delete(1.0,END)
    txtarea.insert(END,'Items\tQuantity Of Items \tCost Of Items')
    txtarea.insert(END, '\n================================')
    if Pizza.get() > 0:
        txtarea.insert(END,f'\nPizza\t\t{Pizza.get()}\t {cp.get()}')

    if Burger.get()>0:
        txtarea.insert(END, f'\nBurger\t\t{Burger.get()}\t {cb.get()}')

    if French_Fries.get()>0:
            txtarea.insert(END,f'\nFrench Fries\t\t{French_Fries.get()}\t {cf.get()}')

    if Coffee.get()>0:
            txtarea.insert(END,f'\nCoffee\t\t{Coffee.get()}\t {cc.get()}')

    if Chinese.get()>0:
            txtarea.insert(END,f'\nChinese\t\t{Chinese.get()}\t {cch.get()}')


    txtarea.insert(END,'\n\n================================')
    txtarea.insert(END, f'\nTotal Price\t\t{total.get()}\t {total_cost.get()}')
    txtarea.insert(END,'\n================================')

def reset():
    txtarea.delete(1.0,END)
    Pizza.set(0)
    Burger.set(0)
    French_Fries.set(0)
    Coffee.set(0)
    Chinese.set(0)
    total.set(0)

    cp.set('')
    cb.set('')
    cf.set('')
    cc.set('')
    cch.set('')
    total_cost.set('')

def exit():
    if messagebox.askyesno('Confirm','Do You Really Want To Exit'):
        win.destroy()


#~~~~~~~~~~Item Details~~~~~~~~~~~~~~
f1=LabelFrame(win,text='Item Details',font=('times new roman',15,'bold'),fg='dark blue',bg='powder blue',bd=4)
f1.place(x=5,y=90,width=690,height=500)

itm=Label(f1,text='Items',font=('times new roman',20,'bold'),fg='dark blue',bg='powder blue')
itm.grid(row=0,column=0,padx=20,pady=15)

quantity=Label(f1,text='Quantity Of Items',font=('times new roman',20,'bold'),fg='dark blue',bg='powder blue')
quantity.grid(row=0,column=1,padx=20,pady=15)

cost=Label(f1,text='Cost Of Items',font=('times new roman',20,'bold'),fg='dark blue',bg='powder blue')
cost.grid(row=0,column=2,padx=20,pady=15)

#~~~~~~~~~Items~~~~~~~~~~~~~~
pizza=Label(f1,text='Pizza',font=('times new roman',15,'bold'),fg='blue',bg='powder blue')
pizza.grid(row=1,column=0,pady=15,padx=20)
qpEntry=Entry(f1,font='arial 15 bold',relief=SUNKEN,bd=5,justify=CENTER,textvariable=Pizza)
qpEntry.grid(row=1,column=1,padx=20,pady=15)
cpEntry=Entry(f1,font='arial 15 bold',relief=SUNKEN,bd=5,justify=CENTER,textvariable=cp)
cpEntry.grid(row=1,column=2,padx=20,pady=15)

burger=Label(f1,text='Burger',font=('times new roman',15,'bold'),fg='blue',bg='powder blue')
burger.grid(row=2,column=0,pady=15,padx=20)
qbEntry=Entry(f1,font='arial 15 bold',relief=SUNKEN,bd=5,justify=CENTER,textvariable=Burger)
qbEntry.grid(row=2,column=1,padx=20,pady=15)
cbEntry=Entry(f1,font='arial 15 bold',relief=SUNKEN,bd=5,justify=CENTER,textvariable=cb)
cbEntry.grid(row=2,column=2,padx=20,pady=15)

french_fries=Label(f1,text='French Fries',font=('times new roman',15,'bold'),fg='blue',bg='powder blue')
french_fries.grid(row=3,column=0,pady=15,padx=20)
qfEntry=Entry(f1,font='arial 15 bold',relief=SUNKEN,bd=5,justify=CENTER,textvariable=French_Fries)
qfEntry.grid(row=3,column=1,padx=20,pady=15)
cfEntry=Entry(f1,font='arial 15 bold',relief=SUNKEN,bd=5,justify=CENTER,textvariable=cf)
cfEntry.grid(row=3,column=2,padx=20,pady=15)

coffee=Label(f1,text='Coffee',font=('times new roman',15,'bold'),fg='blue',bg='powder blue')
coffee.grid(row=4,column=0,pady=15,padx=20)
qcEntry=Entry(f1,font='arial 15 bold',relief=SUNKEN,bd=5,justify=CENTER,textvariable=Coffee)
qcEntry.grid(row=4,column=1,padx=20,pady=15)
ccEntry=Entry(f1,font='arial 15 bold',relief=SUNKEN,bd=5,justify=CENTER,textvariable=cc)
ccEntry.grid(row=4,column=2,padx=20,pady=15)

chinese=Label(f1,text='Chinese',font=('times new roman',15,'bold'),fg='blue',bg='powder blue')
chinese.grid(row=5,column=0,pady=15,padx=20)
qchEntry=Entry(f1,font='arial 15 bold',relief=SUNKEN,bd=5,justify=CENTER,textvariable=Chinese)
qchEntry.grid(row=5,column=1,padx=20,pady=15)
cchEntry=Entry(f1,font='arial 15 bold',relief=SUNKEN,bd=5,justify=CENTER,textvariable=cch)
cchEntry.grid(row=5,column=2,padx=20,pady=15)

TotalPrice=Label(f1,text='Total Price',font=('times new roman',15,'bold'),fg='blue',bg='powder blue')
TotalPrice.grid(row=6,column=0,pady=15,padx=20)
qtpEntry=Entry(f1,font='arial 15 bold',relief=SUNKEN,bd=5,justify=CENTER,textvariable=total)
qtpEntry.grid(row=6,column=1,padx=20,pady=15)
ctpEntry=Entry(f1,font='arial 15 bold',relief=SUNKEN,bd=5,justify=CENTER,textvariable=total_cost)
ctpEntry.grid(row=6,column=2,padx=20,pady=15)

#~~~~~~~~~~~Reciept~~~~~~~~~~~~~~~~~~
f2=Frame(win,relief=GROOVE,bd=10)
f2.place(x=700,y=90,width=420,height=500)

billtitle=Label(f2,text='Reciept',font=('times new roman',15,'bold'),bd=5,bg='dark blue',fg='white',relief=GROOVE).pack(fill=X)
scrol=Scrollbar(f2,orient=VERTICAL)
scrol.pack(side=RIGHT,fill=Y)
txtarea=Text(f2,font=('times new roman',15,'bold'),yscrollcommand=scrol.set)
txtarea.pack(fill=BOTH)
scrol.config(command=txtarea.yview)

#~~~~~~~~~~~Buttons~~~~~~~~~~~~~~~~~~
f3=Frame(win,relief=GROOVE,bd=10)
f3.place(x=4,y=590,width=1100,heigh=80)

btn1=Button(f3,text='Total',font=('times new roman',15,'bold'),bg='dark blue',fg='white',padx=5,pady=2,width=10,command=Total)
btn1.grid(row=0,column=0,pady=10,padx=20)

btn2=Button(f3,text='Reciept',font=('times new roman',15,'bold'),bg='dark blue',fg='white',padx=5,pady=2,width=10,command=reciept)
btn2.grid(row=0,column=1,pady=10,padx=20)

btn3=Button(f3,text='Reset',font=('times new roman',15,'bold'),bg='dark blue',fg='white',padx=5,pady=2,width=10,command=reset)
btn3.grid(row=0,column=3,pady=10,padx=20)

btn4=Button(f3,text='Exit',font=('times new roman',15,'bold'),bg='dark blue',fg='white',padx=5,pady=2,width=10,command=exit)
btn4.grid(row=0,column=4,pady=10,padx=20)

win.mainloop()
