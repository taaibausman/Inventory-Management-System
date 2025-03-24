from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

class supplierClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1150x700+200+120")
        self.root.title("Inventory Management System ")
        self.root.config(bg="#e0f7fa")
        self.root.focus_force()

        # Variables
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.var_sup_invoice = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()

        # Search Frame
        SearchFrame = LabelFrame(self.root, text="Search Supplier", font=("goudy old style", 15, "bold"), bg="#e0f7fa", fg="#800000")
        SearchFrame.place(x=150, y=10, width=800, height=80)

        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Select", "Invoice Number", "Name"), state='readonly', justify=CENTER, font=("goudy old style", 13))
        cmb_search.grid(row=0, column=0, padx=100, pady=10, sticky="w")
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("goudy old style", 15), bg="#FBE7A1")
        txt_search.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        btn_search = Button(SearchFrame, text="Search", command=self.search, font=("goudy old style", 15), bg="#A52A2A", fg="white", cursor="hand2")
        btn_search.grid(row=0, column=2, padx=15, pady=10, sticky="w")

        # Title
        title = Label(self.root, text="Supplier Details", font=("goudy old style", 20, "bold"), bg="#0f4d7d", fg="white")
        title.place(x=150, y=100, width=800)

        # Form Frame
        FormFrame = Frame(self.root, bd=1, relief=RIDGE, bg="white")
        FormFrame.place(x=100, y=140, width=1000, height=240)

        # Left Side
        lbl_supplier_invoice = Label(FormFrame, text="Invoice No:", font=("goudy old style", 15, "bold"), bg="#C0C0C0")
        lbl_supplier_invoice.grid(row=0, column=0, padx=15, pady=40, sticky="w")
        txt_supplier_invoice = Entry(FormFrame, textvariable=self.var_sup_invoice, font=("goudy old style", 15), bg="#FBE7A1")
        txt_supplier_invoice.grid(row=0, column=1, padx=0, pady=40, sticky="w")

        lbl_contact = Label(FormFrame, text="Contact:", font=("goudy old style", 15, "bold"), bg="#C0C0C0")
        lbl_contact.grid(row=1, column=0, padx=15, pady=0, sticky="w")
        txt_contact = Entry(FormFrame, textvariable=self.var_contact, font=("goudy old style", 15), bg="#FBE7A1")
        txt_contact.grid(row=1, column=1, padx=0, pady=10, sticky="w")

        lbl_desc = Label(FormFrame, text="Description:", font=("goudy old style", 15, "bold"), bg="#C0C0C0")
        lbl_desc.grid(row=3, column=0, padx=15, pady=10, sticky="w")
        self.txt_desc = Text(FormFrame, font=("goudy old style", 15), bg="#FBE7A1", height=2, width=20)
        self.txt_desc.grid(row=3, column=1, padx=0, pady=10, sticky="nsew")

        # Right Side
        lbl_name = Label(FormFrame, text="Name:", font=("goudy old style", 15, "bold"), bg="#C0C0C0")
        lbl_name.grid(row=0, column=4, padx=15, pady=0, sticky="w")
        txt_name = Entry(FormFrame, textvariable=self.var_name, font=("goudy old style", 15), bg="#FBE7A1")
        txt_name.grid(row=0, column=5, padx=0, pady=10, sticky="w")

        lbl_email = Label(FormFrame, text="Email:", font=("goudy old style", 15, "bold"), bg="#C0C0C0")
        lbl_email.grid(row=1, column=4, padx=15, pady=0, sticky="w")
        txt_email = Entry(FormFrame, textvariable=self.var_email, font=("goudy old style", 15), bg="#FBE7A1")
        txt_email.grid(row=1, column=5, padx=0, pady=10, sticky="w")

        # Buttons
        btn_Frame = Frame(FormFrame, bd=1, relief=RIDGE, bg="yellow")
        btn_Frame.place(x=520, y=200, width=450, height=30)

        btn_add = Button(btn_Frame, text="Add", font=("goudy old style", 15), bg="#2196f3", fg="white", cursor="hand2", command=self.add)
        btn_add.place(x=0, y=0, width=110, height=30)

        btn_update = Button(btn_Frame, text="Update", font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2", command=self.update)
        btn_update.place(x=112, y=0, width=110, height=28)

        btn_delete = Button(btn_Frame, text="Delete", font=("goudy old style", 15), bg="#f44336", fg="white", cursor="hand2", command=self.delete)
        btn_delete.place(x=224, y=0, width=110, height=28)

        btn_clear = Button(btn_Frame, text="Clear", font=("goudy old style", 15), bg="#607d8b", fg="white", cursor="hand2", command=self.clear)
        btn_clear.place(x=336, y=0, width=110, height=28)

        # Supplier Details
        sup_frame = Frame(self.root, bd=3, relief=RIDGE)
        sup_frame.place(x=0, y=400, width=1150, height=200)

        scrolly = Scrollbar(sup_frame, orient=VERTICAL)
        scrollx = Scrollbar(sup_frame, orient=HORIZONTAL)

        self.supplierTable = ttk.Treeview(sup_frame, columns=("invoice", "name", "contact", "email", "desc"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)

        self.supplierTable.heading("invoice", text="Invoice No.")
        self.supplierTable.heading("name", text="Name")
        self.supplierTable.heading("contact", text="Contact")
        self.supplierTable.heading("email", text="Email")
        self.supplierTable.heading("desc", text="Description")
        self.supplierTable["show"] = "headings"
        self.supplierTable.column("invoice", width=90)
        self.supplierTable.column("name", width=100)
        self.supplierTable.column("contact", width=100)
        self.supplierTable.column("email", width=100)
        self.supplierTable.column("desc", width=100)
        self.supplierTable.pack(fill=BOTH, expand=1)
        self.supplierTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()



    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice must be required", parent=self.root)
            elif self.var_name.get() == "":
                messagebox.showerror("Error", "Name must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Invoice No. already assigned, try different ID", parent=self.root)
                else:
                    cur.execute("INSERT INTO supplier (invoice, name, contact, email, desc) values(?,?,?,?,?)", (
                        self.var_sup_invoice.get(),
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.txt_desc.get('1.0', END),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier Added Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice No. must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Invoice No.", parent=self.root)
                else:
                    cur.execute("UPDATE supplier SET name=?, contact=?, email=?, desc=? WHERE invoice=?", (
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.txt_desc.get('1.0', END),
                        self.var_sup_invoice.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice No. must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Invoice No.", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op:
                        cur.execute("DELETE FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Supplier Deleted Successfully", parent=self.root)
                        self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.var_email.set("")
        self.txt_desc.delete('1.0', END)
        self.var_searchtxt.set("")
        self.show()

    def get_data(self, ev):
        r = self.supplierTable.focus()
        content = self.supplierTable.item(r)
        row = content["values"]
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.var_email.set(row[3])
        self.txt_desc.delete('1.0', END)
        self.txt_desc.insert(END, row[4])

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM supplier")
            rows = cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get() == "Select":
                messagebox.showerror("Error", "Select search by option", parent=self.root)
            elif self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Search input should be required", parent=self.root)
            else:
                if self.var_searchby.get() == "Invoice Number":
                    cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_searchtxt.get(),))
                elif self.var_searchby.get() == "Name":
                    cur.execute("SELECT * FROM supplier WHERE name LIKE ?", ('%'+self.var_searchtxt.get()+'%',))
                rows = cur.fetchall()
                if rows:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    for row in rows:
                        self.supplierTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

if __name__ == "__main__":
    root = Tk()
    obj = supplierClass(root)
    root.mainloop()
