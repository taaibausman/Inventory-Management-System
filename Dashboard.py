from tkinter import *
from tkinter import ttk, messagebox
import time 
from PIL import Image, ImageTk
from category import Category_class
from Employee import EmployeeClass
from Supplier import supplierClass
from Product import ProductClass
from sales import salesClass
from billing import BillClass
import sqlite3
import os


class IMS:
    def __init__(self, root) -> None:
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title('INVENTORY MANAGEMENT SYSTEM | PUCIT')


        bg_image = Image.open("images/bg image.jpg")
        bg_image = bg_image.resize((1350, 700))
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        self.canvas = Canvas(self.root, width=1350, height=700)
        self.canvas.create_image(0, 0, anchor=NW, image=self.bg_photo)
        self.canvas.pack(fill=BOTH, expand=YES)
        # TITLE
        title = Label(self.root, text="INVENTORY MANAGEMENT SYSTEM",
                      font=("Georgia", 40, "bold"), bg="#1E3A5F", fg="white",
                      anchor='w', padx=20)
        title.place(x=0, y=0, relwidth=1, height=60)

        # Logout button
        button_logout = Button(self.root, command=self.logout,text="LOGOUT", font=("Georgia", 10, "bold"), cursor='hand2', bg="#FFD700", fg="#333333")
        button_logout.place(x=1200, y=10, height=40, width=140)

        # Header 2
        self.header2 = Label(self.root, text="Welcome to IMS\t\tDate:DD-MM-YYYY\t\tTime: JWANI DA",
                             font=("Georgia", 15), bd=2, relief=RIDGE, bg="#1E3A5F", fg="white")
        self.header2.place(x=0, y=60, relwidth=1, height=30)

        # LEFT MENU
        Left_Menu = Frame(self.root, bd=2, relief=RIDGE, bg="#E8EAF6")
        Left_Menu.place(x=0, y=90, width=200, height=475)

        # Buttons
        button_Home = Button(Left_Menu, text="HOME", font=("Georgia", 20), bg="#1E3A5F", fg="white", bd=5, cursor='hand2')
        button_Home.pack(side=TOP, fill=X)
        button_Employee = Button(Left_Menu, text="Employee", font=("Georgia", 20), command=self.Employee_call, bd=5, bg="#1E3A5F", fg="white", cursor='hand2')
        button_Employee.pack(side=TOP, fill=X)
        button_Supplier = Button(Left_Menu, text="Supplier", font=("Georgia", 20), command=self.Supplier_call, bd=5, bg="#1E3A5F", fg="white", cursor='hand2')
        button_Supplier.pack(side=TOP, fill=X)
        button_Category = Button(Left_Menu, text="Category", font=("Georgia", 20), command=self.category_call, bd=5, bg="#1E3A5F", fg="white", cursor='hand2')
        button_Category.pack(side=TOP, fill=X)
        button_Products = Button(Left_Menu, text="Products", font=("Georgia", 20), command=self.Product_call, bd=5, bg="#1E3A5F", fg="white", cursor='hand2')
        button_Products.pack(side=TOP, fill=X)
        button_Sales = Button(Left_Menu, text="Sales", command=self.Sales_call, font=("Georgia", 20), bd=5, bg="#1E3A5F", fg="white", cursor='hand2')
        button_Sales.pack(side=TOP, fill=X)
        button_Bill = Button(Left_Menu, text="Bill", command=self.Billing_call, font=("Georgia", 20), bd=5, bg="#1E3A5F", fg="white", cursor='hand2')
        button_Bill.pack(side=TOP, fill=X)
        button_Exit = Button(Left_Menu, text="Exit", command=self.exit, font=("Georgia", 20), bd=5, bg="#1E3A5F", fg="white", cursor='hand2')
        button_Exit.pack(side=TOP, fill=X)

        # Containers
        self.label_employee = Label(self.root, text='Total Employee\n[0]', bd=5, relief=RIDGE, font=("Georgia", 20), bg="#1E3A5F", fg="white")
        self.label_employee.place(x=300, y=120, height=150, width=300)
        self.label_suppliers = Label(self.root, text='Total Suppliers\n[0]', bd=5, relief=RIDGE, font=("Georgia", 20), bg="#1E3A5F", fg="white")
        self.label_suppliers.place(x=650, y=120, height=150, width=300)
        self.label_category = Label(self.root, text='Total Categories\n[0]', bd=5, relief=RIDGE, font=("Georgia", 20), bg="#1E3A5F", fg="white")
        self.label_category.place(x=1000, y=120, height=150, width=300)
        self.label_products = Label(self.root, text='Total Products\n[0]', bd=5, relief=RIDGE, font=("Georgia", 20), bg="#1E3A5F", fg="white")
        self.label_products.place(x=300, y=350, height=150, width=300)
        self.label_sales = Label(self.root, text='Total Sales\n[0]', bd=5, relief=RIDGE, font=("Georgia", 20), bg="#1E3A5F", fg="white")
        self.label_sales.place(x=650, y=350, height=150, width=300)

        self.updating_data()

    def category_call(self):
        self.new_window = Toplevel(self.root)
        self.new_obj = Category_class(self.new_window)

    def Employee_call(self):
        self.new_window = Toplevel(self.root)
        self.new_obj = EmployeeClass(self.new_window)

    def Supplier_call(self):
        self.new_window = Toplevel(self.root)
        self.new_obj = supplierClass(self.new_window)

    def Product_call(self):
        self.new_window = Toplevel(self.root)
        self.new_obj = ProductClass(self.new_window)

    def Sales_call(self):
        self.new_window = Toplevel(self.root)
        self.new_obj = salesClass(self.new_window)

    def Billing_call(self):
        new_window = Toplevel(self.root)
        new_obj = BillClass(new_window)

    def exit(self):
        self.root.destroy()

    def updating_data(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from product")
            products = cur.fetchall()
            self.label_products.config(text=f'Total Products\n{len(products)}')
            cur.execute("select * from category")
            categories = cur.fetchall()
            self.label_category.config(text=f'Total Categories\n{len(categories)}')
            cur.execute("select * from employee")
            employee = cur.fetchall()
            self.label_employee.config(text=f'Total Employee\n{len(employee)}')
            sales = os.listdir("bill")
            self.label_sales.config(text=f'Total Sales\n{len(sales)}')
            cur.execute("select * from supplier")
            suppliers = cur.fetchall()
            self.label_suppliers.config(text=f'Total Suppliers\n{len(suppliers)}')

            # Updating time
            tm = time.strftime("%I:%M:%S %p")
            dt = time.strftime("%d-%m-%Y")
            self.header2.config(text=f"Welcome to Metaverse_IMS\t\tDate: {str(dt)}\t\tTime: {str(tm)}")
            self.header2.after(1000, self.updating_data)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
    def logout(self):
        self.root.destroy()
        from login import Login_System
        login_window=Tk()
        login_obj=Login_System(login_window)
        login_window.mainloop()

if __name__ == "__main__":
    window = Tk()
    obj = IMS(window)
    window.mainloop()
