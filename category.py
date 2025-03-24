from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class Category_class:
    def __init__(self, root) -> None:
        self.root = root
        self.root.geometry("1100x500+230+120")
        self.root.title("Product Categories")
        self.root.focus_force()
        
        # Variables
        self.cat_id = StringVar()
        self.cat_name = StringVar()
        
        # Title
        title = Label(self.root, text="Manage Product Categories", bd=2, relief=RIDGE,
                      font=("Georgia", 30, "bold"), bg='#1E3A5F', fg='white')
        title.pack(side=TOP, fill=X, padx=10, pady=20)
        
        # Category Name
        cat_name = Label(self.root, text="Enter Category Name:", font=("Georgia", 20))
        cat_name.place(x=50, y=110)
        
        cat_name_entry = Entry(self.root, textvariable=self.cat_name, font=("Georgia", 20), bg='lightyellow')
        cat_name_entry.place(x=50, y=150, height=50, width=400)
        
        # Buttons
        cat_add_btn = Button(self.root, text='ADD', command=self.add, font=("Georgia", 20),
                             bg='#FFD700', cursor='hand2')
        cat_add_btn.place(x=50, y=220, width=150)
        
        cat_delete_btn = Button(self.root, text='DELETE', font=("Georgia", 20),command=self.delete, bg='#FFD700', cursor='hand2')
        cat_delete_btn.place(x=220, y=220, width=150)
        
        # Preview
        cat_frame = Frame(self.root, bd=2, relief=RIDGE)
        cat_frame.place(x=470, y=100, width=600, height=300)
        
        scrollx = Scrollbar(cat_frame, orient=HORIZONTAL)
        scrolly = Scrollbar(cat_frame, orient=VERTICAL)
        
        self.cat_table = ttk.Treeview(cat_frame, columns=("Category ID", "Name"),
                                      yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.cat_table.xview)
        scrolly.config(command=self.cat_table.yview)
        
        self.cat_table.heading("Category ID", text="CATEGORY ID")
        self.cat_table.heading("Name", text="NAME")
        self.cat_table["show"] = 'headings'
        self.cat_table.column("Category ID", width=100)
        self.cat_table.column("Name", width=100)
        self.cat_table.pack(fill=BOTH, expand=1)
        
        # Image
        cat_image = Image.open("images/CATEGORY.jpg")
        self.cat_image = cat_image.resize((400, 200), Image.LANCZOS)
        self.cat_image = ImageTk.PhotoImage(self.cat_image)
        self.label_cat_image = Label(self.root, image=self.cat_image, bd=2, relief=RIDGE)
        self.label_cat_image.place(x=50, y=280)
        self.cat_table.bind("<ButtonRelease-1>",self.get_data)
        self.show()
    
    # Function to add a category
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.cat_name.get() == "":
                messagebox.showerror("Error", "NAME IS REQUIRED", parent=self.root)
            else:
                cur.execute("SELECT * FROM category WHERE Name=?", (self.cat_name.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Category already exists, try a different name", parent=self.root)
                else:
                    cur.execute("INSERT INTO category (Name) VALUES (?)", (self.cat_name.get(),))
                    con.commit()
                    messagebox.showinfo("Success", "Category added successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()
    
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from category")
            rows=cur.fetchall()
            self.cat_table.delete(*self.cat_table.get_children())
            for row in rows:
                self.cat_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    def get_data(self,ev):
        f=self.cat_table.focus()
        content=(self.cat_table.item(f))
        row=content["values"]
        self.cat_id.set(row[0])
        self.cat_name.set(row[1])
    
    def delete(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()
        try:
            if self.cat_id.get()=="":
                messagebox.showerror("Error","Select category from list!",parent=self.root)
            else:
                cur.execute("select * from category where Category_ID=?",(self.cat_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Try Again!!!")
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from category where Category_ID=?",(self.cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Category deleted successfuly!",parent=self.root)
                        self.show()
                        self.cat_id.set('')
                        self.cat_name.set('')
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

if __name__ == "__main__":
    window = Tk()
    obj = Category_class(window)
    window.mainloop()
