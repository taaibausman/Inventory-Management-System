from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

class ProductClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1150x700+200+120")
        self.root.title("Inventory Management System")
        self.root.config(bg="#F0F0F0")
        self.root.focus_force()

        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_pid = StringVar()
        self.var_cat = StringVar()
        self.var_sup = StringVar()
        self.cat_list = []
        self.sup_list = []
        self.fetch_cat_sup()

        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_status = StringVar()

        product_Frame = Frame(self.root, bd=5, relief=RIDGE, bg="#EAEAEA")
        product_Frame.place(x=20, y=10, width=500, height=480)

        title = Label(product_Frame, text="Product Details", font=("Georgia", 18, "bold"), bg="#455A64", fg="white")
        title.pack(side=TOP, fill=X)

        lbl_category = Label(product_Frame, text="Category:", font=("Georgia", 14, "bold"), bg="#EAEAEA")
        lbl_category.place(x=30, y=60)
        lbl_supplier = Label(product_Frame, text="Supplier:", font=("Georgia", 14, "bold"), bg="#EAEAEA")
        lbl_supplier.place(x=30, y=110)
        lbl_product_name = Label(product_Frame, text="Product Name:", font=("Georgia", 14, "bold"), bg="#EAEAEA")
        lbl_product_name.place(x=30, y=160)
        lbl_price = Label(product_Frame, text="Price:", font=("Georgia", 14, "bold"), bg="#EAEAEA")
        lbl_price.place(x=30, y=210)
        lbl_qty = Label(product_Frame, text="Quantity:", font=("Georgia", 14, "bold"), bg="#EAEAEA")
        lbl_qty.place(x=30, y=260)
        lbl_status = Label(product_Frame, text="Status:", font=("Georgia", 14, "bold"), bg="#EAEAEA")
        lbl_status.place(x=30, y=310)

        cmb_cat = ttk.Combobox(product_Frame, textvariable=self.var_cat, values=self.cat_list, state='readonly', justify=CENTER, font=("Georgia", 12))
        cmb_cat.place(x=240, y=60, width=200)
        cmb_cat.current(0)

        cmb_sup = ttk.Combobox(product_Frame, textvariable=self.var_sup, values=self.sup_list, state='readonly', justify=CENTER, font=("Georgia", 12))
        cmb_sup.place(x=240, y=110, width=200)
        cmb_sup.current(0)

        txt_name = Entry(product_Frame, textvariable=self.var_name, font=("Georgia", 12), bg="lightyellow")
        txt_name.place(x=240, y=160, width=200)

        txt_price = Entry(product_Frame, textvariable=self.var_price, font=("Georgia", 12), bg="lightyellow")
        txt_price.place(x=240, y=210, width=200)

        txt_qty = Entry(product_Frame, textvariable=self.var_qty, font=("Georgia", 12), bg="lightyellow")
        txt_qty.place(x=240, y=260, width=200)

        cmb_status = ttk.Combobox(product_Frame, textvariable=self.var_status, values=("Active", "Inactive"), state='readonly', justify=CENTER, font=("Georgia", 12))
        cmb_status.place(x=240, y=310, width=200)
        cmb_status.current(0)

        btn_add = Button(product_Frame, text="Save", font=("Georgia", 14), command=self.add, bg="#4CAF50", fg="white", cursor="hand2")
        btn_add.place(x=10, y=400, width=100, height=40)
        btn_update = Button(product_Frame, text="Update", font=("Georgia", 14), command=self.update, bg="#FFC107", fg="white", cursor="hand2")
        btn_update.place(x=120, y=400, width=100, height=40)
        btn_delete = Button(product_Frame, text="Delete", font=("Georgia", 14), command=self.delete, bg="#F44336", fg="white", cursor="hand2")
        btn_delete.place(x=230, y=400, width=100, height=40)
        btn_clear = Button(product_Frame, text="Clear", font=("Georgia", 14), command=self.clear, bg="#607D8B", fg="white", cursor="hand2")
        btn_clear.place(x=340, y=400, width=100, height=40)

        SearchFrame = LabelFrame(self.root, text="Search Product", font=("Georgia", 12, "bold"), bd=2, relief=RIDGE, bg="#EAEAEA")
        SearchFrame.place(x=540, y=10, width=600, height=80)

        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Select", "Category", "Supplier", "Name"), state='readonly', justify=CENTER, font=("Georgia", 12))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("Georgia", 12), bg="lightyellow")
        txt_search.place(x=200, y=10)
        btn_search = Button(SearchFrame, text="Search", font=("Georgia", 12), command=self.search, bg="#455A64", fg="white", cursor="hand2")
        btn_search.place(x=410, y=9, width=150, height=30)

        p_frame = Frame(self.root, bd=3, relief=RIDGE)
        p_frame.place(x=540, y=100, width=600, height=390)

        #Product Details
        p_frame = Frame(self.root, bd=3, relief=RIDGE)
        p_frame.place(x=540, y=100, width=600, height=390)

        scrolly = Scrollbar(p_frame, orient=VERTICAL)
        scrollx = Scrollbar(p_frame, orient=HORIZONTAL)

        self.product_table = ttk.Treeview(p_frame, columns=("pid", "category", "supplier", "name", "price", "qty", "status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)
        
        self.product_table.heading("pid", text="Product ID")
        self.product_table.heading("category", text="Category")
        self.product_table.heading("supplier", text="Supplier")
        self.product_table.heading("name", text="Product Name")
        self.product_table.heading("price", text="Price")
        self.product_table.heading("qty", text="Quantity")
        self.product_table.heading("status", text="Status")



        self.product_table["show"] = "headings"

        self.product_table.column("pid", width=50)
        self.product_table.column("category", width=100)

        self.product_table.column("supplier", width=100)

        self.product_table.column("name", width=100)
        self.product_table.column("price", width=100)

        self.product_table.column("qty", width=100)
        self.product_table.column("status", width=100)

        self.product_table.pack(fill=BOTH, expand=1)
        self.product_table.bind("<ButtonRelease-1>", self.get_data)
        self.show()


    def fetch_cat_sup(self):
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")

        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT name FROM category")
            cat = cur.fetchall()

            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])

            cur.execute("SELECT name FROM supplier")
            sup = cur.fetchall()

            if len(sup) > 0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

        
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_cat.get() == "Select" or self.var_cat.get() == "Empty" or self.var_sup.get() == "Select" or self.var_name.get() == "":
                messagebox.showerror("Error", "Employee ID must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM product WHERE name=?", (self.var_name.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "The Product already assigned, try different", parent=self.root)
                else:
                    cur.execute("INSERT INTO product (category, supplier, name, price, qty, status) values (?, ?, ?, ?, ?, ?)", (
                        self.var_cat.get(),
                        self.var_sup.get(),

                        self.var_name.get(),
                        self.var_price.get(),

                        self.var_qty.get(),
                        self.var_status.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Product Added Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_pid.get() == "":
                messagebox.showerror("Error", "Please select the product from List", parent=self.root)
            else:
                cur.execute("SELECT * FROM product WHERE pid=?", (self.var_pid.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Product Name", parent=self.root)
                else:
                    cur.execute("UPDATE product SET Category=?, Supplier=?, name=?, price=?, qty=?, status=? WHERE pid=?", (
                        self.var_cat.get(),
                        self.var_sup.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_qty.get(),
                        self.var_status.get(),
                        self.var_pid.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Product Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_pid.get() == "":
                messagebox.showerror("Error", "Product must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM product WHERE pid=?", (self.var_pid.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Product ID", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op:
                        cur.execute("DELETE FROM product WHERE pid=?", (self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Product Deleted Successfully", parent=self.root)
                        self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def clear(self):

        self.var_cat.set("Select")
        self.var_sup.set("Select")
        self.var_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.var_status.set("Active")
        self.var_pid.set("")
        self.var_searchby.set("Select")
        self.var_searchtxt.set("")
        self.show()


    def get_data(self, ev):
        r = self.product_table.focus()
        content = self.product_table.item(r)
        row = content["values"]
        
        self.var_pid.set(row[0])
        self.var_cat.set(row[1])
        self.var_sup.set(row[2])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_qty.set(row[5])
        self.var_status.set(row[6])

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM product")
            rows = cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get() == "Select":
                messagebox.showerror("Error", "Select Search by Option", parent=self.root)
            elif self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Search parameter should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM product WHERE " + self.var_searchby.get() + " LIKE '%" + self.var_searchtxt.get() + "%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No Record Found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = ProductClass(root)
    root.mainloop()
