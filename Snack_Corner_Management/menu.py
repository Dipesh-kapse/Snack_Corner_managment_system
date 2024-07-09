from tkinter import *


# make a window
root = Tk()
root.title("Snacks Corner Management")
# specify it's size
root.geometry("500x500")
root.maxsize(500,500)
root.minsize(500,500)

def next():
    root.destroy()
    import main

frm1=Frame(root,bg="silver",width=500,height=500)
frm1.place(x=0,y=0)

lbl1= Label(root,text="MENU CARD",font="times 18 bold",bg="tomato",width=35,height=2,bd=5,relief=GROOVE)
lbl1.place(y=0)

lbl2 = Label(frm1,text=("Pizza                    99\n\n\n""Burger                 70\n\n\n""Coffee                  30\n\n\n"
             "Chinese                60\n\n\n""French Fries         55"),bg="silver",font="Times 15 bold")
lbl2.place(x=30,y=100)

nextbtn = Button(frm1,text="NEXT",font="Arial 15 bold",width=10,bd=5,relief=GROOVE,bg="black",fg="white",command=next)
nextbtn.place(x=320,y=400)

root.mainloop()