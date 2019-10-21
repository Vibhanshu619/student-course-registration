#importing modules
import mysql.connector
from tkinter import *
from tkinter import messagebox

#connecting to MySQL Database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="Course_Registration_database"
)
#Making cursor to execute queries
cur = conn.cursor()

#Function to Add details of a Student to the database
def Add_Entry():
    name = name_entry.get()
    reg = reg_entry.get()
    dept = dept_entry.get()
    course = course_entry.get()
    s = (name, reg, dept, course)
    sql = "INSERT INTO course VALUES(%s,%s,%s,%s)"
    cur.execute(sql, s)
    conn.commit()
    messagebox.showinfo("OK", "Course Registered for Registration Number "+reg)
    name_entry.delete(0,END)
    reg_entry.delete(0, END)
    dept_entry.delete(0, END)
    course_entry.delete(0, END)

#Function to delete details of a student where Reg. No. is provided
def Delete_Entry():
    reg=reg_entry.get()
    sql="DELETE FROM course WHERE Registration_Number='%s' " %reg
    cur.execute(sql)
    conn.commit()
    messagebox.showinfo("OK", "Student Details Successfully Removed")
    reg_entry.delete(0, END)

#Function to show the entries of the Database
def Show_Entry():
    cur.execute("SELECT * FROM course")
    result=cur.fetchall()
    messagebox.showinfo("Fetching Entry","Please Wait....Fetching Details")
    for r in result:
        showbox.insert(END,r)
        showbox.insert(END,"\n")

#Function to update the course of a student by providing Reg. No.
def Update_Entry():
    reg=reg_entry.get()
    course=course_entry.get()
    sql="UPDATE course SET Course ='%s'WHERE Registration_Number='%s' "%(course,reg)
    cur.execute(sql)
    conn.commit()
    messagebox.showinfo("Updated","Course successfully updated")
    reg_entry.delete(0, END)
    course_entry.delete(0, END)

#Function to search a student by providing Reg No.
def Search_Entry():
    reg=reg_entry.get()
    sql="SELECT * FROM course WHERE Registration_Number ='%s' " %reg
    cur.execute(sql)
    reg_entry.delete(0, END)
    result = cur.fetchall()
    messagebox.showinfo("Search", "Student successfully Found")
    for r in result:
        showbox.insert(END, r)
        showbox.insert(END, "\n")

#Making GUI Interface
window = Tk()

window.title("Student Course Registration")#Giving a tile to the application
window.geometry("450x450")#Reshe window of applicationizing t

#Taking input from the user

name_label = Label(window, text="Name ",font=("Helvetica",12))
name_label.place(x=135,y=10)
name_entry = Entry(window,width=27)
name_entry.place(x=200,y=10)

reg_label = Label(window, text="Registration Number ",font=("Helvetica",12))
reg_label.place(x=45,y=40)
reg_entry = Entry(window,width=27)
reg_entry.place(x=200,y=40)

dept_label = Label(window, text="Department ",font=("Helvetica",12))
dept_label.place(x=95,y=70)
dept_entry = Entry(window,width=27)
dept_entry.place(x=200,y=70)

course_label = Label(window, text="Course ",font=("Helvetica",12))
course_label.place(x=120,y=100)
course_entry = Entry(window,width=27)
course_entry.place(x=200,y=100)

#Different buttons to perfom various queries
add_button = Button(window, text="Add", command=Add_Entry,font=("Helvetica",12))
add_button.place(x=50,y=150)

delete_button = Button(window, text="Delete", command=Delete_Entry,font=("Helvetica",12))
delete_button.place(x=110,y=150)

show_Button=Button(window,text="Show",command=Show_Entry,font=("Helvetica",12))
show_Button.place(x=190,y=150)

update_button=Button(window,text="Update",command=Update_Entry,font=("Helvetica",12))
update_button.place(x=265,y=150)

search_button=Button(window,text="Search",command=Search_Entry,font=("Helvetica",12))
search_button.place(x=350,y=150)

#Output box to show the databse when requested
showbox=Text(window,width=45,height=12)
showbox.place(x=45,y=220)

window.mainloop()
