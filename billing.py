from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import sqlite3
import time
class BillClass:
    def __init__(self, root) -> None:
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title('INVENTORY MANAGEMENT SYSTEM | PUCIT')

        icon_image = Image.open("images/title_icon.png")
        resized_icon_image = icon_image.resize((50, 50))  # Resize to 50x50 pixels
        self.icon_title = ImageTk.PhotoImage(resized_icon_image)
        # Variables
        self.product_id_entry = StringVar()
        self.label_name_entry = StringVar()
        self.customer_name_entry=StringVar()
        self.customer_contact_entry=StringVar()

        self.product_name_entry=StringVar()
        self.price_per_quantity_entry=StringVar()
        self.quantity_entry=StringVar()
        self.cart_list=[]
        self.stock=StringVar()
        # TITLE
        title = Label(self.root, text="INVENTORY MANAGEMENT SYSTEM",
                      font=("Georgia", 40, "bold"), bg="#1E3A5F", fg="white",
                      anchor='w', padx=20, image=self.icon_title, compound='left')
        title.place(x=0, y=0, relwidth=1, height=60)


        self.header2= Label(self.root, text="Welcome to BillClass\t\tDate:DD-MM-YYYY\t\tTime: JWANI DA",
                      font=("Georgia", 15),bd=2,relief=RIDGE, bg="black", fg="white")
        self.header2.place(x=0,y=60,relwidth=1,height=30)
        #product frame
        ProductFrame1=Frame(self.root,bd=4,relief=RIDGE,bg='white')
        ProductFrame1.place(x=10,y=110,width=400,height=550)
        ProductTitle1=Label(ProductFrame1,text='All Products',font=('Georgia',20,'bold'),bg='black',fg='white')
        ProductTitle1.pack(side=TOP,fill=X)

        ProductFrame2=Frame(ProductFrame1,bd=2,relief=RIDGE,bg='white')
        ProductFrame2.place(x=2,y=40,width=388,height=80)
        label_search=Label(ProductFrame2,text="Search Product by Name",font=('Georgia',12,'bold'),bg='white',fg='green')
        label_search.place(x=2,y=10)

        label_name=Label(ProductFrame2,text='Product Name',font=('Georgia',12,'bold'),bg='white')
        label_name.place(x=5,y=45)

        label_name_entry = Entry(ProductFrame2, textvariable=self.label_name_entry, font=("Georgia", 12), bg='lightyellow')
        label_name_entry.place(x=130, y=45, height=30, width=130)

        ProductFrame3=Frame(ProductFrame1,bd=2,relief=RIDGE,bg='white')
        ProductFrame3.place(x=2,y=120,width=388,height=420)

        scrolly = Scrollbar(ProductFrame3, orient=VERTICAL)
        scrollx = Scrollbar(ProductFrame3, orient=HORIZONTAL)

        self.product_table = ttk.Treeview(ProductFrame3, columns=("pid", "name", "price", "qty", "status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)


        self.product_table.heading("pid", text="PID")
        self.product_table.heading("name", text="Name")
        self.product_table.heading("price", text="Price")
        self.product_table.heading("qty", text="QTY")
        self.product_table.heading("status", text="Status")

        self.product_table['show']='headings'

        self.product_table.column("pid", width=50)
        self.product_table.column("name", width=100)
        self.product_table.column("price", width=70)
        self.product_table.column("qty", width=50)
        self.product_table.column("status", width=100)
        self.product_table.pack(fill=BOTH, expand=1)
        self.product_table.bind("<ButtonRelease-1>", self.get_data)

        self.show()
        #button
        button_showall=Button(ProductFrame2,text="Show All",command=self.show,font=("Georgia", 15, "bold"),cursor='hand2',bg="black",fg='white')
        button_showall.place(x=280,y=5,height=30,width=100)

        button_search=Button(ProductFrame2,text="Search",command=self.search,font=("Georgia", 15, "bold"),cursor='hand2',bg="black",fg='white')
        button_search.place(x=280,y=45,height=30,width=100)

        #Middle frame
        Customer_frame1=Frame(self.root,bd=4,relief=RIDGE,bg='white')
        Customer_frame1.place(x=410,y=110,width=500,height=550)
        CustomerTitle1=Label(Customer_frame1,text='Customer Details',font=('Georgia',15,'bold'),bg='black',fg='white')
        CustomerTitle1.pack(side=TOP,fill=X)

        Customer_frame2=Frame(Customer_frame1,bd=2,relief=RIDGE,bg='white')
        Customer_frame2.place(x=2,y=30,width=488,height=40)
        label_customer_name=Label(Customer_frame2,text="Name:",font=('Georgia',12,'bold'),bg='white',fg='black')
        label_customer_name.place(x=2,y=10)

        customer_name_entry = Entry(Customer_frame2, textvariable=self.customer_name_entry, font=("Georgia", 12), bg='white')
        customer_name_entry.place(x=60, y=10, height=25, width=140)
    

        label_customer_contact=Label(Customer_frame2,text="Contact no:",font=('Georgia',12,'bold'),bg='white',fg='black')
        label_customer_contact.place(x=202,y=10)

        customer_contact_entry = Entry(Customer_frame2, textvariable=self.customer_contact_entry, font=("Georgia", 12), bg='white')
        customer_contact_entry.place(x=310, y=10, height=25, width=170)

        Customer_frame3=Frame(Customer_frame1,bd=4,relief=RIDGE,bg='white')
        Customer_frame3.place(x=2,y=440,width=488,height=100)

        label_product_name=Label(Customer_frame3,text="Product Name",font=('Georgia',12,'bold'),bg='white',fg='black')
        label_product_name.place(x=2,y=5)

        product_name_entry = Entry(Customer_frame3, textvariable=self.product_name_entry, font=("Georgia", 12), bg='grey')
        product_name_entry.place(x=2, y=30, height=25, width=140)

        label_price_per_quantity=Label(Customer_frame3,text="Price/Qty",font=('Georgia',12,'bold'),bg='white',fg='black')
        label_price_per_quantity.place(x=180,y=5)

        price_per_quantity_entry = Entry(Customer_frame3, textvariable=self.price_per_quantity_entry, font=("Georgia", 12), bg='grey')
        price_per_quantity_entry.place(x=180, y=30, height=25, width=140)

        label_quantity=Label(Customer_frame3,text="Quantity",font=('Georgia',12,'bold'),bg='white',fg='black')
        label_quantity.place(x=340,y=5)

        quantity_entry = Entry(Customer_frame3, textvariable=self.quantity_entry, font=("Georgia", 12), bg='grey')
        quantity_entry.place(x=340, y=30, height=25, width=140)
        

        self.stock_label=Label(Customer_frame3,text='In Stock',font=('Georgia',12,'bold',),bg='white',fg='black')
        self.stock_label.place(x=2,y=70)
        #MiddleFrame buttons
        clear_btn = Button(Customer_frame3, text='Clear', command=self.clear,font=("Georgia", 12),
                             bg='black',fg='white', cursor='hand2')
        clear_btn.place(x=180, y=60, width=130)


        update_btn = Button(Customer_frame3, text='Add/Update Cart',command=self.add_update_cart, font=("Georgia", 12),
                             bg='black',fg='white', cursor='hand2')
        update_btn.place(x=320, y=60, width=160)

        #Calculator frame

        self.var_calculator_input=StringVar()
        calculator_frame=Frame(Customer_frame1,bd=4,relief=RIDGE,bg='white')
        calculator_frame.place(x=2,y=70,width=250,height=370)

        calculator_input_label=Entry(calculator_frame,textvariable=self.var_calculator_input,font=('Georgia',15,'bold'),width=16,bd=10,relief=GROOVE,state='readonly',justify=RIGHT)
        calculator_input_label.grid(row=0,columnspan=4)
        btn_7=Button(calculator_frame,text='7',font=('arial',15,'bold'),command=lambda: self.get_input(7),cursor='hand2',bd=5,width=4,pady=16).grid(row=1,column=0)
        btn_8=Button(calculator_frame,text='8',font=('arial',15,'bold'),command=lambda: self.get_input(8),cursor='hand2',bd=5,width=4,pady=16).grid(row=1,column=1)
        btn_9=Button(calculator_frame,text='9',font=('arial',15,'bold'),command=lambda: self.get_input(9),cursor='hand2',bd=5,width=4,pady=16).grid(row=1,column=2)
        btn_sum=Button(calculator_frame,text='+',font=('arial',15,'bold'),command=lambda: self.get_input('+'),cursor='hand2',bd=5,width=4,pady=16).grid(row=1,column=3)
       
       
        btn_4=Button(calculator_frame,text='4',font=('arial',15,'bold'),command=lambda: self.get_input(4),cursor='hand2',bd=5,width=4,pady=16).grid(row=2,column=0)
        btn_5=Button(calculator_frame,text='5',font=('arial',15,'bold'),command=lambda: self.get_input(5),cursor='hand2',bd=5,width=4,pady=16).grid(row=2,column=1)
        btn_6=Button(calculator_frame,text='6',font=('arial',15,'bold'),command=lambda: self.get_input(6),cursor='hand2',bd=5,width=4,pady=16).grid(row=2,column=2)
        btn_sub=Button(calculator_frame,text='-',font=('arial',15,'bold'),command=lambda: self.get_input('-'),cursor='hand2',bd=5,width=4,pady=16).grid(row=2,column=3)
        

        btn_1=Button(calculator_frame,text='1',font=('arial',15,'bold'),command=lambda: self.get_input(1),cursor='hand2',bd=5,width=4,pady=16).grid(row=3,column=0)
        btn_2=Button(calculator_frame,text='2',font=('arial',15,'bold'),command=lambda: self.get_input(2),cursor='hand2',bd=5,width=4,pady=16).grid(row=3,column=1)
        btn_3=Button(calculator_frame,text='3',font=('arial',15,'bold'),command=lambda: self.get_input(3),cursor='hand2',bd=5,width=4,pady=16).grid(row=3,column=2)
        btn_mul=Button(calculator_frame,text='*',font=('arial',15,'bold'),command=lambda: self.get_input('*'),cursor='hand2',bd=5,width=4,pady=16).grid(row=3,column=3)
        
        btn_0=Button(calculator_frame,text='0',font=('arial',15,'bold'),command=lambda: self.get_input(0),cursor='hand2',bd=5,width=4,pady=16).grid(row=4,column=0)
        btn_clear=Button(calculator_frame,text='C',font=('arial',15,'bold'),command=self.cal_clear,cursor='hand2',bd=5,width=4,pady=16).grid(row=4,column=1)
        btn_div=Button(calculator_frame,text='/',font=('arial',15,'bold'),command=lambda: self.get_input('/'),cursor='hand2',bd=5,width=4,pady=16).grid(row=4,column=2)
        btn_equal=Button(calculator_frame,text='=',font=('arial',15,'bold'),command=self.perform_cal,cursor='hand2',bd=5,width=4,pady=16).grid(row=4,column=3)
        #Cart Frame
        cart_frame=Frame(Customer_frame1,bd=4,relief=RIDGE,bg='white')
        cart_frame.place(x=252,y=70,width=240,height=370)
        self.cart_frame_label=Label(cart_frame,text="Cart        Total Products:0",font=('Georgia',14,),bg='grey',fg='white')
        self.cart_frame_label.pack(fill=X)

        scrolly = Scrollbar(cart_frame, orient=VERTICAL)
        scrollx = Scrollbar(cart_frame, orient=HORIZONTAL)

        self.cart_table = ttk.Treeview(cart_frame, columns=("pid", "name", "price", "qty"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.cart_table.xview)
        scrolly.config(command=self.cart_table.yview)


        self.cart_table.heading("pid", text="PID")
        self.cart_table.heading("name", text="Name")
        self.cart_table.heading("price", text="Price")
        self.cart_table.heading("qty", text="QTY")

        self.cart_table['show']='headings'

        self.cart_table.column("pid", width=50)
        self.cart_table.column("name", width=50)
        self.cart_table.column("price", width=50)
        self.cart_table.column("qty", width=50)
        self.cart_table.pack(fill=BOTH, expand=1)
        #self.cart_table.bind("<ButtonRelease-1>", self.get_data)

        #Blling Frame
        Billing_frame1=Frame(self.root,bd=4,relief=RIDGE,bg='white')
        Billing_frame1.place(x=910,y=110,width=430,height=550)
        

        Billing_label1=Label(Billing_frame1,text='Customer Billing Area',font=('Georgia',15,'bold'),bg='black',fg='white')
        Billing_label1.pack(fill=X)

        Billing_frame2=Frame(Billing_frame1,bd=4,relief=RIDGE,bg='white')
        Billing_frame2.place(x=0,y=30,width=420,height=450)

        scrolly = Scrollbar(Billing_frame2, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)
        
        self.Billing_text_area=Text(Billing_frame2,yscrollcommand=scrolly.set)
        self.Billing_text_area.pack(fill=BOTH,expand=1)
        #configuring y view
        scrolly.config(command=self.Billing_text_area.yview)

        Billing_frame3=Frame(Billing_frame1,bd=4,relief=RIDGE,bg='white')
        Billing_frame3.place(x=2,y=410,width=420,height=130)

        self.Bill_amount_label=Label(Billing_frame3,text='Bill Amount\n0',font=('Georgia',10,),
                                bg='#1E3A5F',fg='white')
        self.Bill_amount_label.place(x=0,y=0,width=138,height=70)
        
        self.Dicsount_label=Label(Billing_frame3,text='Dicsount\n5%',font=('Georgia',10,),
                                bg='#1E3A5F',fg='white')
        self.Dicsount_label.place(x=140,y=0,width=138,height=70)
        
        self.Net_pay_label=Label(Billing_frame3,text='Net Pay\n0',font=('Georgia',10,),
                                bg='#1E3A5F',fg='white')
        self.Net_pay_label.place(x=280,y=0,width=138,height=70)
        

        
        #Billing frame buttons
        Print_button=Button(Billing_frame3,text='Print',font=('Georgia',12),cursor='hand2',bg='black',fg='white')
        Print_button.place(x=2,y=75,width=138,height=45)

        Clear_all_button=Button(Billing_frame3,command=self.clear_all,text='Clear All',font=('Georgia',12),cursor='hand2',bg='black',fg='white')
        Clear_all_button.place(x=142,y=75,width=138,height=45)

        Print_button=Button(Billing_frame3,text='Generate &\nSave Bill',command=self.Generate_bill,font=('Georgia',12),cursor='hand2',bg='black',fg='white')
        Print_button.place(x=282,y=75,width=138,height=45)
        self.show()

        #date time updating
        self.update_date_time()
#===========functions================
    def get_input(self,num):
        num=self.var_calculator_input.get()+str(num)
        self.var_calculator_input.set(num)
    def clear(self):
        self.product_name_entry.set("")
        self.price_per_quantity_entry.set("")
        self.quantity_entry.set(0)
        self.customer_contact_entry.set("")
        self.customer_name_entry.set("")
    def cal_clear(self):
        self.var_calculator_input.set("")
    def perform_cal(self):
        result=self.var_calculator_input.get()
        self.var_calculator_input.set(eval(result))



    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:

            cur.execute("SELECT pid,name,price,qty,status FROM product where status='Active'")
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
            if self.label_name_entry.get() == "":
                messagebox.showerror("Error", "Search parameter should be required", parent=self.root)
            else:
                cur.execute("SELECT pid,name,price,qty,status FROM product WHERE name LIKE '%" + self.label_name_entry.get() + "%' and status='Active'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No Record Found\n or Product is Inactive.", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


    def get_data(self, ev):
        r = self.product_table.focus()
        content = self.product_table.item(r)
        row = content["values"]
        self.product_id_entry.set(row[0])
        self.product_name_entry.set(row[1])
        self.price_per_quantity_entry.set(row[2])
        self.stock.set(row[3])
        self.stock_label.config(text=f"In Stock :{self.stock.get()}")
        self.quantity_entry.set('1')
        


    def add_update_cart(self):
        if self.quantity_entry.get()=='' or self.quantity_entry.get()=='0':
            messagebox.showerror("Error","Quantity is Required",parent=self.root)
        elif self.product_id_entry.get()=='' :
            messagebox.showerror("Error","Select product from the list.",parent=self.root)
        elif int(self.quantity_entry.get())>int(self.stock.get()) :
            messagebox.showerror("Error","Stock unavailable for this quantity.",parent=self.root)
        else:
            price=self.price_per_quantity_entry.get()
            item_data=[self.product_id_entry.get(),self.product_name_entry.get(),price,
                                   self.quantity_entry.get(),self.stock.get()]
            
        #checking list to update if item already present
            available='no'
            index=0

            for row in self.cart_list:
                if self.product_id_entry.get()==row[0]:
                    available='yes'
                    break
                index+=1
            if available=='yes':
                op=messagebox.askyesno('Confirm',"Product already present in card list.\nDo you want to update or remove?",parent=self.root)
                if op==True:
                    if (self.quantity_entry.get()).strip()=='0':
                        self.cart_list.pop(index)
                    else:
                        self.cart_list[index][2]=price
                        self.cart_list[index][3]=self.quantity_entry.get()
            else:
                self.cart_list.append(item_data)
        self.show_cart()
        self.Bill_updating()
        self.cart_frame_label.config(text=f"Cart        Total Products:{len(self.cart_list)}")
    def show_cart(self):
        try:
            self.cart_table.delete(*self.cart_table.get_children())
            for row in self.cart_list:
                self.cart_table.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def Bill_updating(self):
        self.amount=0
        if len(self.cart_list)!=0:
            for row in self.cart_list:
                self.amount+=float(row[2])*float(row[3])
        self.net_amount=str(self.amount-(self.amount*0.05))
        self.Bill_amount_label.config(text=f'Bill Amount(Rs)\n{self.amount}')
        self.Net_pay_label.config(text=f'Net Pay(Rs)\n{self.net_amount}')
        self.discount=0.05*self.amount
    def Generate_bill(self):
        if self.customer_name_entry.get()=='' or self.customer_contact_entry.get()=='':
            messagebox.showerror("Error","Customer name and contact number are required")
            return
        elif len(self.cart_list)==0:
            messagebox.showerror("Error","Select the products for cart , first!")
        else:
            self.bill_top()
            self.bill_middle()
            self.bill_bottom()
            file=open(f"bill/{str(self.invoice)}.txt", 'w')
            file.write(self.Billing_text_area.get('1.0',END))
            file.close()
            messagebox.showinfo("Saved",'Bill saved successfully!',parent=self.root)
    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
        r=f'''
\t\tMetaverse-Inventory
\t Phone No. +92302***** , Lahore-0540
{str("="*47)}
 Customer Name: {self.customer_name_entry.get()}
 Ph no. :{self.customer_contact_entry.get()}
 Bill No. {str(self.invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}
{str("="*47)}
 Product Name\t\t\tQTY\tPrice
{str("="*47)}
        '''
        self.Billing_text_area.delete('1.0',END)
        self.Billing_text_area.insert('1.0',r)
    def bill_bottom(self):
        r=f'''
{str("="*47)}
 Bill Amount\t\t\t\tRs.{self.amount}
 Discount\t\t\t\tRs.{self.discount}
 Net Pay\t\t\t\tRs.{self.net_amount}
{str("="*47)}\n
        '''
        self.Billing_text_area.insert(END,r)
    def bill_middle(self): 
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            for row in self.cart_list:
                pid=row[0]
                name=row[1]
                qty=row[3]
                qty2=int(row[4])-int(qty)
                if int(qty)==int(row[4]):
                    st='Inactive'
                elif int(qty)!=int(row[4]):
                    st='Active'
                price=float(row[2])*int(row[3])
                price=str(price)
                self.Billing_text_area.insert(END,"\n "+name+"\t\t\t"+qty+"\tRs."+price)
                cur.execute("update product set qty=?,status=? where pid=?",(
                    qty2,st,pid
                ))
                con.commit()
            self.show()
            con.close()
        except Exception as e:
            messagebox.showerror("Error", f"Failed due to: {str(e)}", parent=self.root)

    def clear_all(self):
        self.clear()
        del self.cart_list[:]
        self.show()
        self.show_cart()
        self.cal_clear()
        self.cart_frame_label.config(text=f"Cart        Total Products: 0")
        self.Billing_text_area.delete('1.0',END)

    def update_date_time(self):
        tm = time.strftime("%I:%M:%S %p")  
        dt = time.strftime("%d-%m-%Y")    
        self.header2.config(text=f"Welcome to Metaverse_IMS\t\tDate: {str(dt)}\t\tTime: {str(tm)}")
        self.header2.after(1000, self.update_date_time)  


if __name__=="__main__":
    window=Tk()
    obj = BillClass(window)
    window.mainloop()