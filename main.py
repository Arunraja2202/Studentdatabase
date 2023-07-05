from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database

db = Database("Student.db")
root=Tk()
root.title("Student Management System")
root.geometry("500x500+100+100")
root.config(bg="light blue")
root.state("zoomed")

name= StringVar()
age= StringVar()
rollno= StringVar()
dob=StringVar()
Gender=StringVar()
contact=StringVar()
address=StringVar()

#Entries frame
entries_frame= Frame(root, bg="red")
entries_frame.pack(side=TOP, fill=X)
title= Label(entries_frame, text="Student Management System", font=("arial",35,"bold"), bg="red", fg="white")
title.grid(row=0, columnspan=2, padx=20, pady=20)

labelname=Label(entries_frame, text="Name", font=("aril",14, "bold"),fg="black", bg="red")
labelname.grid(row=1, column=0, padx=10, pady=20, sticky="w")
textname=Entry(entries_frame,textvariable=name, font=("arial",14))
textname.grid(row=1, column=1,sticky="w")

labelage=Label(entries_frame, text="Age", font=("aril",14, "bold"),fg="black", bg="red")
labelage.grid(row=1, column=2,padx=10, pady=20,sticky="w")
textage=Entry(entries_frame,textvariable=age, font=("arial",14))
textage.grid(row=1, column=3, sticky="w")

labelrollno=Label(entries_frame, text="Roll No.", font=("aril",14, "bold"),fg="black", bg="red")
labelrollno.grid(row=2, column=0,padx=10, pady=20, sticky="w")
textrollno=Entry(entries_frame,textvariable=rollno, font=("arial",14))
textrollno.grid(row=2, column=1, sticky="w")

labeldob=Label(entries_frame, text="D.O.B", font=("aril",14, "bold"),fg="black", bg="red")
labeldob.grid(row=2, column=2, padx=10, pady=20, sticky="w")
textdob=Entry(entries_frame,textvariable=dob, font=("arial",14))
textdob.grid(row=2, column=3, sticky="w")

labelgender=Label(entries_frame, text="Gender", font=("aril",14, "bold"),fg="black", bg="red")
labelgender.grid(row=3, column=0,padx=10, pady=20, sticky="w")
combgender=ttk.Combobox(entries_frame,textvariable=Gender,font=("aril",13, "bold"),state="readonly")
combgender["value"]=("Male","Female")
combgender.grid(row=3, column=1, sticky="w")


labelcontact=Label(entries_frame, text="Contact", font=("aril",14, "bold"),fg="black", bg="red")
labelcontact.grid(row=3, column=2,padx=10, pady=20, sticky="w")
textcontact=Entry(entries_frame,textvariable=contact, font=("arial",14))
textcontact.grid(row=3, column=3, sticky="w")

labeladdress=Label(entries_frame, text="Address", font=("aril",14, "bold"),fg="black", bg="red")
labeladdress.grid(row=4, column=0,padx=10, pady=20, sticky="w")
textaddress=Text(entries_frame,font=("arial",14),width=50, height=3)
textaddress.grid(row=4, column=0,columnspan=4,padx=10,pady=10, sticky="w")

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    name.set(row[1])
    age.set(row[2])
    dob.set(row[3])
    rollno.set(row[4])
    Gender.set(row[5])
    contact.set(row[6])
    textaddress.delete(1.0, END)
    textaddress.insert(END, row[7])

def dispalyAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)


def add_student():
    if textname.get() == "" or textage.get() == "" or textdob.get() == "" or  textrollno.get() == "" or combgender.get() == "" or textcontact.get() == "" or textaddress.get(
            1.0, END) == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.insert(textname.get(),textage.get(), textdob.get() , textrollno.get() ,combgender.get(), textcontact.get(), textaddress.get(
            1.0, END))
    messagebox.showinfo("Success", "Record Inserted")
    clear_student()
    dispalyAll()



def update_student():
    if textname.get() == "" or textage.get() == "" or textdob.get() == "" or textrollno.get() == "" or combgender.get() == "" or textcontact.get() == "" or textaddress.get(
            1.0, END) == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.update(row[0],textname.get(), textage.get(), textdob.get(), textrollno.get(), combgender.get(), textcontact.get(),
              textaddress.get(
                  1.0, END))
    messagebox.showinfo("Success", "Record Update")
    clear_student()
    dispalyAll()


def delete_student():
    db.remove(row[0])
    clear_student()
    dispalyAll()


def clear_student():
    name.set("")
    age.set("")
    dob.set("")
    Gender.set("")
    rollno.set("")
    contact.set("")
    textaddress.delete(1.0, END)
buttonframe=Frame(entries_frame, bg="red")
buttonframe.grid(row=12, column=0,columnspan=4,padx=10, pady=20, sticky="w")
buttonadd=Button(buttonframe,bg="white", command=add_student,text="Add Details", width=20,bd=0,font=("arial",10,"bold")).grid(row=0,column=0, padx=10)
buttonupdate=Button(buttonframe,bg="white", command=update_student,text="Update Details", width=20,bd=0,font=("arial",10,"bold")).grid(row=0,column=1, padx=10)
buttondelete=Button(buttonframe,bg="white", command=delete_student,text="Delete", width=20,bd=0,font=("arial",10,"bold")).grid(row=0,column=2, padx=10)
buttonclear=Button(buttonframe,bg="white", command=clear_student,text="Clear All", width=20,bd=0,font=("arial",10,"bold")).grid(row=0,column=3, padx=10)

tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.place(x=0, y=480, width=1980, height=520)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 18),
                rowheight=50)  # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=5)
tv.heading("2", text="Name")
tv.heading("3", text="Age")
tv.column("3", width=5)
tv.heading("4", text="D.O.B")
tv.column("4", width=10)
tv.heading("5", text="Email")
tv.heading("6", text="Gender")
tv.column("6", width=10)
tv.heading("7", text="Contact")
tv.heading("8", text="Address")
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

dispalyAll()
root.mainloop()

