from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
root=Tk()
root.geometry('1250x750+0+0')
root.title('Snacks Corner Management System')
def connect():
    cur = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Dipesh@143",
        database="snack"
    )
    return cur

def add_record():
    con = connect()
    cur = con.cursor()
    id = e1.get()
    name=e2.get()
    iname=e3.get()
    price=e4.get()
    cn=e5.get()
    Add=e6.get()
    cur.execute("insert into scm values("+id+" , '"+name+"', '"+iname+"', "+price+", "+cn+" , '"+Add+"')")
    con.commit()
    con.close()
    tree.insert('', "end", values=(id, name, iname, price, cn, Add))
    messagebox.showinfo('Success', 'Record Added Successfully')
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)

def delete_record():
    conn = connect()
    c = conn.cursor()
    select_del = tree.focus()
    if select_del:
        values = tree.item(select_del,'values')
        # id_to_delete= values[0]
        # delete in database
        query = f"delete from scm where Customer_ID = %s"
        c.execute(query,(values[0],))
        conn.commit()
        # delete in treeview
        tree.delete(select_del)
    messagebox.showinfo("Information", "The record is deleted.....")

def update():
    conn = connect()
    c = conn.cursor()
    id = e1.get()
    name = e2.get()
    iname = e3.get()
    price = e4.get()
    cn = e5.get()
    Add = e6.get()

    query = ("update scm set Customer_name = '%s',Item_name ='%s',Quentity ='%s',Contact_no = '%s',Address='%s'"
             " where Customer_ID = '%s' " % (name,iname,price,cn,Add,id))
    c.execute(query)
    conn.commit()

    selected_item = tree.selection()
    if len(selected_item) == 1:  # Ensure only one item is selected
        item = selected_item[0]
        # Update the values in the selected item
        tree.item(item, values=(f"{id}", f"{name}", f"{iname}",f"{price}",f"{cn}",f"{Add}"))
    messagebox.showinfo("Info", "Selected Record Updated Successfully")

# ********* selection ***********
def show_selected_row(event):
    selected_item = tree.focus()
    values = tree.item(selected_item, 'values')
    if values:
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e1.insert(0, values[0])
        e2.insert(0, values[1])
        e3.insert(0, values[2])
        e4.insert(0, values[3])
        e5.insert(0, values[4])
        e6.insert(0, values[5])
def clear():
    for i in tree.get_children():
        tree.delete(i)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)

def bill():
        if messagebox.askyesno('Confirm','Do You Want To Make Bill'):
            root.destroy()
            import Bill
        else:
            return

def exit():
        confirm = messagebox.askyesno('Confirm', 'Are You Sure You Want To Exit')
        if confirm > 0:
            root.destroy()
            return

def show():
    # Clear previous data
    tree.delete(*tree.get_children())
    conn = connect()
    c = conn.cursor()
    c.execute("select * from scm")
    res = c.fetchall()
    for i in res:
        tree.insert('','end',values=i)
    conn.commit()
    conn.close()

tlbl = Label(root, text='SNACKS CORNER MANAGEMENT SYSTEM', font=('times new roman', 30, 'bold'), bg='powder blue',
                     fg='dark blue')
tlbl.place(x=0, y=0, width=1500)

frame1 = Frame(root, bd=5, relief=RIDGE, bg='powder blue')
frame1.place(x=20, y=100, width=500, height=550)


# ~~~~~~~~Label~~~~~~~~~~~~~

managelbl = Label(frame1, text='Manage Snacks', font=('times new roman', 18, 'bold'), fg='dark blue', bg='powder blue')
managelbl.grid(row=0, columnspan=3, pady=10, padx=20)

l1 = Label(frame1, text='Customer ID', font=('times new roman', 18, 'bold'), fg='dark blue', bg='powder blue').grid(row=1,column=1,pady=10,padx=20, sticky=W)
e1 = Entry(frame1,font=('times new roman', 18, 'bold'), bd=2,relief=GROOVE)
e1.grid(row=1, column=2, pady=5, padx=15)

l2 = Label(frame1, text='Customer Name', font=('times new roman', 18, 'bold'), fg='dark blue', bg='powder blue').grid(row=2,column=1,pady=10,padx=20,sticky=W)
e2 = Entry(frame1,font=('times new roman', 18, 'bold'), bd=2,relief=GROOVE)
e2.grid(row=2, column=2, pady=5, padx=15)

l3 = Label(frame1, text='Item Name', font=('times new roman', 18, 'bold'), fg='dark blue', bg='powder blue').grid(row=3,column=1,pady=10,padx=20,sticky=W)
e3 = Entry(frame1, font=('times new roman', 18, 'bold'), bd=2,relief=GROOVE)
e3.grid(row=3, column=2, pady=5, padx=15)

l4 = Label(frame1, text='Quantity', font=('times new roman', 18, 'bold'), fg='dark blue', bg='powder blue').grid(row=4,column=1, pady=10,padx=20,sticky=W)
e4 = Entry(frame1, font=('times new roman', 18, 'bold'), bd=2, relief=GROOVE)
e4.grid(row=4, column=2, pady=5, padx=15)

l5 = Label(frame1, text='Contact No.', font=('times new roman', 18, 'bold'), fg='dark blue', bg='powder blue').grid(row=5,column=1,pady=10,padx=20,sticky=W)
e5 = Entry(frame1,font=('times new roman', 18, 'bold'), bd=2,relief=GROOVE)
e5.grid(row=5, column=2, pady=5, padx=15)

l6 = Label(frame1, text='Address', font=('times new roman', 18, 'bold'), fg='dark blue', bg='powder blue').grid(row=6,column=1,pady=10,padx=20,sticky=W)
e6 = Entry(frame1, font=('times new roman', 18, 'bold'),bd=2,relief=GROOVE)
e6.grid(row=6, column=2, pady=5, padx=15)

# ~~~~~~~~BUTTON~~~~~~~~~~~~~

btnframe = Frame(frame1, bd=4, relief=RIDGE, bg='powder blue')
btnframe.place(x=15, y=420, width=460, height=100)

addbtn = Button(btnframe, text='Add Record', font=('', 10), width=10,command=add_record).grid(row=0, column=0,padx=10, pady=10)
delbtn = Button(btnframe, text='Delete Record', font=('', 10), width=10,command=delete_record ).grid(row=0,column=1,padx=10,pady=10)
updbtn = Button(btnframe, text='Update Record', font=('', 10), width=10,command=update).grid(row=0, column=2,padx=10,pady=10)
billbtn = Button(btnframe, text='Bill', font=('', 10), width=10,command=bill).grid(row=0, column=3,padx=10,pady=10)
clrbtn = Button(btnframe, text='Clear', font=('', 10), width=10,command=clear).grid(row=1, column=1,padx=10, pady=10)
extbtn = Button(btnframe, text='Exit', font=('', 10), width=10, command=exit).grid(row=1, column=2,padx=10, pady=10)
showbtn = Button(btnframe,text="Show",font=('',10),width=10,command=show).grid(row=1,column=3,padx=10,pady=10)

frame2 = Frame(root, bd=5, relief=RIDGE, bg='powder blue')
frame2.place(x=550, y=100, width=800, height=550)

tblframe = Frame(frame2, bd=5, relief=RIDGE, bg='powder blue')
tblframe.place(x=10, y=70, width=767, height=450)

scroll_x = Scrollbar(tblframe, orient=HORIZONTAL)
scroll_y = Scrollbar(tblframe, orient=VERTICAL)
columns=('customer_id', 'customer_name', 'item_name', 'Quantity', 'contact_no', 'address')
tree= ttk.Treeview(tblframe,columns=columns , xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=tree.xview)
scroll_y.config(command=tree.yview)

tree.heading('customer_id', text='Customer ID')
tree.heading('customer_name', text='Customer Name')
tree.heading('item_name', text='Item Name')
tree.heading('Quantity', text='Quantity')
tree.heading('contact_no', text='Contact No.')
tree.heading('address', text='Address')
tree['show'] = 'headings'
tree.pack()
tree.bind("<<TreeviewSelect>>",show_selected_row)
tree.column('customer_id', width=100, anchor=CENTER)
tree.column('customer_name', width=150, anchor=CENTER)
tree.column('item_name', width=130, anchor=CENTER)
tree.column('Quantity', width=70, anchor=CENTER)
tree.column('contact_no', width=140, anchor=CENTER)
tree.column('address', width=150, anchor=CENTER)
tree.pack(fill=BOTH, expand=1, anchor=CENTER)

# ********** Ending statement ***********
root.mainloop()