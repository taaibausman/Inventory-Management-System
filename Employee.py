from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

class EmployeeClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1150x700+200+120")
        self.root.title("Inventory Management System ")
        self.root.config(bg="#e0f7fa")
        self.root.focus_force()

        # Variables
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_emp_id = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_date_of_birth = StringVar()
        self.var_date_of_joining = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()
        self.var_salary = StringVar()

        # Search Frame
        SearchFrame = LabelFrame(self.root, text="Search Employee", font=("goudy old style", 15, "bold"), bg="#e0f7fa", fg="#800000")
        SearchFrame.place(x=150, y=10, width=800, height=80)

        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Select", "name", "email", "contact"), state='readonly', justify=CENTER, font=("goudy old style", 13))
        cmb_search.grid(row=0, column=0, padx=100, pady=10)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("goudy old style", 15), bg="#FBE7A1")
        txt_search.grid(row=0, column=1, padx=10, pady=10)

        btn_search = Button(SearchFrame, text="Search", command=self.search, font=("goudy old style", 15), bg="#A52A2A", fg="white", cursor="hand2")
        btn_search.grid(row=0, column=2, padx=15, pady=10)

        # Title
        title = Label(self.root, text="Employee Details", font=("goudy old style", 20, "bold"), bg="#0f4d7d", fg="white")
        title.place(x=150, y=100, width=800)

        # Form Frame
        FormFrame = Frame(self.root, bd=1, relief=RIDGE, bg="white")
        FormFrame.place(x=100, y=140, width=1000, height=240)

        # Left Side
        lbl_empid = Label(FormFrame, text="Emp ID:", font=("goudy old style", 12, "bold"), bg="#C0C0C0")
        lbl_empid.grid(row=0, column=0, padx=15, pady=10, sticky="w")
        txt_empid = Entry(FormFrame, textvariable=self.var_emp_id, font=("goudy old style", 12), bg="#FBE7A1")
        txt_empid.grid(row=0, column=1, padx=0, pady=10, sticky="w")

        lbl_name = Label(FormFrame, text="Name:", font=("goudy old style", 12, "bold"), bg="#C0C0C0")
        lbl_name.grid(row=1, column=0, padx=15, pady=10, sticky="w")
        txt_name = Entry(FormFrame, textvariable=self.var_name, font=("goudy old style", 12), bg="#FBE7A1")
        txt_name.grid(row=1, column=1, padx=0, pady=10, sticky="w")

        lbl_email = Label(FormFrame, text="Email:", font=("goudy old style", 12, "bold"), bg="#C0C0C0")
        lbl_email.grid(row=2, column=0, padx=15, pady=10, sticky="w")
        txt_email = Entry(FormFrame, textvariable=self.var_email, font=("goudy old style", 12), bg="#FBE7A1")
        txt_email.grid(row=2, column=1, padx=0, pady=10, sticky="w")

        lbl_address = Label(FormFrame, text="Address", font=("goudy old style", 12, "bold"), bg="#C0C0C0")
        lbl_address.grid(row=3, column=0, padx=15, pady=10, sticky="w")
        self.txt_address = Text(FormFrame, font=("goudy old style", 12), bg="#FBE7A1", height=1, width=20)
        self.txt_address.grid(row=3, column=1, padx=0, pady=10, sticky="w")

        # Middle Side
        lbl_gender = Label(FormFrame, text="Gender:", font=("goudy old style", 12, "bold"), bg="#C0C0C0")
        lbl_gender.grid(row=0, column=2, padx=15, pady=10, sticky="w")
        cmb_gender = ttk.Combobox(FormFrame, textvariable=self.var_gender, values=("Select", "Male", "Female"), state='readonly', justify=CENTER, font=("goudy old style", 11))
        cmb_gender.grid(row=0, column=3, padx=0, pady=10, sticky="w")

        lbl_date_of_birth = Label(FormFrame, text="Date of Birth:", font=("goudy old style", 12, "bold"), bg="#C0C0C0")
        lbl_date_of_birth.grid(row=1, column=2, padx=15, pady=10, sticky="w")
        txt_date_of_birth = Entry(FormFrame, textvariable=self.var_date_of_birth, font=("goudy old style", 12), bg="#FBE7A1")
        txt_date_of_birth.grid(row=1, column=3, padx=0, pady=10, sticky="w")

        lbl_pass = Label(FormFrame, text="Password:", font=("goudy old style", 12, "bold"), bg="#C0C0C0")
        lbl_pass.grid(row=2, column=2, padx=15, pady=10, sticky="w")
        txt_pass = Entry(FormFrame, textvariable=self.var_pass, font=("goudy old style", 12), bg="#FBE7A1", show="*")
        txt_pass.grid(row=2, column=3, padx=0, pady=10, sticky="w")

        lbl_salary = Label(FormFrame, text="Salary:", font=("goudy old style", 12, "bold"), bg="#C0C0C0")
        lbl_salary.grid(row=3, column=2, padx=15, pady=10, sticky="w")
        txt_salary = Entry(FormFrame, textvariable=self.var_salary, font=("goudy old style", 12), bg="#FBE7A1")
        txt_salary.grid(row=3, column=3, padx=0, pady=10, sticky="w")

        # Right Side
        lbl_contact = Label(FormFrame, text="Contact:", font=("goudy old style", 12, "bold"), bg="#C0C0C0")
        lbl_contact.grid(row=0, column=4, padx=15, pady=10, sticky="w")
        txt_contact = Entry(FormFrame, textvariable=self.var_contact, font=("goudy old style", 12), bg="#FBE7A1")
        txt_contact.grid(row=0, column=5, padx=0, pady=10, sticky="w")

        lbl_date_of_joining = Label(FormFrame, text="Date of Joining:", font=("goudy old style", 12, "bold"), bg="#C0C0C0")
        lbl_date_of_joining.grid(row=1, column=4, padx=15, pady=10, sticky="w")
        txt_date_of_joining = Entry(FormFrame, textvariable=self.var_date_of_joining, font=("goudy old style", 12), bg="#FBE7A1")
        txt_date_of_joining.grid(row=1, column=5, padx=0, pady=10, sticky="w")

        lbl_utype = Label(FormFrame, text="User Type:", font=("goudy old style", 12, "bold"), bg="#C0C0C0")
        lbl_utype.grid(row=2, column=4, padx=15, pady=10, sticky="w")
        cmb_utype = ttk.Combobox(FormFrame, textvariable=self.var_utype, values=("Select", "Admin", "Employee"), state='readonly', justify=CENTER, font=("goudy old style", 11))
        cmb_utype.grid(row=2, column=5, padx=0, pady=10, sticky="w")

        # Buttons Frame
        btn_Frame=Frame(FormFrame,bd=1, relief=RIDGE, bg="yellow")
        btn_Frame.place(x=580, y=190, width=400, height=40)
        btn_add = Button(btn_Frame, text="Save", command=self.add, font=("goudy old style", 15), bg="#32CD32", fg="white", cursor="hand2")
        btn_add.place(x=0, y=0, width=110, height=40)

        btn_update = Button(btn_Frame, text="Update", command=self.update, font=("goudy old style", 15), bg="#FFD700", fg="white", cursor="hand2")
        btn_update.place(x=100, y=0, width=110, height=40)

        btn_delete = Button(btn_Frame, text="Delete", command=self.delete, font=("goudy old style", 15), bg="#DC143C", fg="white", cursor="hand2")
        btn_delete.place(x=200, y=0, width=110, height=40)

        btn_clear = Button(btn_Frame, text="Clear", command=self.clear, font=("goudy old style", 15), bg="#D2691E", fg="white", cursor="hand2")
        btn_clear.place(x=300, y=0, width=110, height=40)

        # Employee Table Frame
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=400, width=1150, height=200)

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.employee_table = ttk.Treeview(emp_frame, columns=("emp_id", "name", "email", "gender", "contact", "dob", "doj", "pass", "utype", "address", "salary"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.employee_table.xview)
        scrolly.config(command=self.employee_table.yview)

        self.employee_table.heading("emp_id", text="Emp ID")
        self.employee_table.heading("name", text="Name")
        self.employee_table.heading("email", text="Email")
        self.employee_table.heading("gender", text="Gender")
        self.employee_table.heading("contact", text="Contact")
        self.employee_table.heading("dob", text="DOB")
        self.employee_table.heading("doj", text="DOJ")
        self.employee_table.heading("pass", text="Password")
        self.employee_table.heading("utype", text="User Type")
        self.employee_table.heading("address", text="Address")
        self.employee_table.heading("salary", text="Salary")
        self.employee_table["show"] = 'headings'

        self.employee_table.column("emp_id", width=90)
        self.employee_table.column("name", width=100)
        self.employee_table.column("email", width=100)
        self.employee_table.column("gender", width=100)
        self.employee_table.column("contact", width=100)
        self.employee_table.column("dob", width=100)
        self.employee_table.column("doj", width=100)
        self.employee_table.column("pass", width=100)
        self.employee_table.column("utype", width=100)
        self.employee_table.column("address", width=200)
        self.employee_table.column("salary", width=100)
        self.employee_table.pack(fill=BOTH, expand=1)
        self.employee_table.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM employee WHERE emp_id=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "This Employee ID already assigned, try different ID", parent=self.root)
                else:
                    cur.execute("INSERT INTO employee (emp_id, name, email, gender, contact, dob, doj, pass, utype, address, salary) values(?,?,?,?,?,?,?,?,?,?,?)", (
                        self.var_emp_id.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_date_of_birth.get(),
                        self.var_date_of_joining.get(),
                        self.var_pass.get(),
                        self.var_utype.get(),
                        self.txt_address.get('1.0', END),
                        self.var_salary.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee Added Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM employee")
            rows = cur.fetchall()
            self.employee_table.delete(*self.employee_table.get_children())
            for row in rows:
                self.employee_table.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.employee_table.focus()
        content = (self.employee_table.item(f))
        row = content['values']
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_date_of_birth.set(row[5])
        self.var_date_of_joining.set(row[6])
        self.var_pass.set(row[7])
        self.var_utype.set(row[8])
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END, row[9])
        self.var_salary.set(row[10])

    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM employee WHERE emp_id=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
                else:
                    cur.execute("UPDATE employee SET name=?, email=?, gender=?, contact=?, dob=?, doj=?, pass=?, utype=?, address=?, salary=? WHERE emp_id=?", (
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_date_of_birth.get(),
                        self.var_date_of_joining.get(),
                        self.var_pass.get(),
                        self.var_utype.get(),
                        self.txt_address.get('1.0', END),
                        self.var_salary.get(),
                        self.var_emp_id.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM employee WHERE emp_id=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
                else:
                    cur.execute("DELETE FROM employee WHERE emp_id=?", (self.var_emp_id.get(),))
                    con.commit()
                    messagebox.showinfo("Success", "Employee Deleted Successfully", parent=self.root)
                    self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_date_of_birth.set("")
        self.var_date_of_joining.set("")
        self.var_pass.set("")
        self.var_utype.set("Select")
        self.txt_address.delete('1.0', END)
        self.var_salary.set("")
        self.show()

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get() == "Select":
                messagebox.showerror("Error", "Select Search By option", parent=self.root)
            elif self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Search input should be required", parent=self.root)
            else:
                cur.execute(f"SELECT * FROM employee WHERE {self.var_searchby.get()} LIKE '%{self.var_searchtxt.get()}%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for row in rows:
                        self.employee_table.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = EmployeeClass(root)
    root.mainloop()

