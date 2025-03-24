from tkinter import Tk, Toplevel, Label, Frame, Entry, Checkbutton, Button, IntVar, END
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3

class Register:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Registration Window")
        self.root.config(bg="#e0f7fa")

        # Load and resize the BG image
        self.bg_image = Image.open("images/SK3.jpg")
        self.bg_image = self.bg_image.resize((1350, 700))
        self.bg = ImageTk.PhotoImage(self.bg_image)

        bg = Label(self.root, image=self.bg)
        bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Load and resize the left image
        self.left_image = Image.open("images/OIG2.vr.jpg")
        self.left_image = self.left_image.resize((400, 500))
        self.left = ImageTk.PhotoImage(self.left_image)

        lef = Label(self.root, image=self.left)
        lef.place(x=80, y=100, width=400, height=500)

        # Register Frame
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)

        # Register Title
        title = Label(frame1, text="Register Here", font=("times new roman", 20, "bold"), bg="white", fg="green")
        title.place(x=50, y=30)

        # Names Data
        f_name = Label(frame1, text="Full Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        f_name.place(x=50, y=100)

        self.txt_fname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_fname.place(x=50, y=130, width=250)

        username = Label(frame1, text="User Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        username.place(x=370, y=100)

        self.txt_username = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_username.place(x=370, y=130, width=250)

        # Contact Data
        contact = Label(frame1, text="Contact No.", font=("times new roman", 15, "bold"), bg="white", fg="black")
        contact.place(x=50, y=170)

        self.txt_contact = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_contact.place(x=50, y=200, width=250)

        # Email Data
        email = Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=170)

        self.txt_email = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=370, y=200, width=250)

        # Security questions
        sec_ques = Label(frame1, text="Security Question", font=("times new roman", 15, "bold"), bg="white", fg="black")
        sec_ques.place(x=50, y=240)

        self.cmb_quest = ttk.Combobox(frame1, font=("times new roman", 13), state='readonly', justify="center")
        self.cmb_quest['values'] = ("Select", "Your First Pet Name", "Your Birth Place", "Your Best Friend Name")
        self.cmb_quest.place(x=50, y=270, width=250)
        self.cmb_quest.current(0)

        # Security answers
        sec_ans = Label(frame1, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
        sec_ans.place(x=370, y=240)

        self.txt_sec_ans = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_sec_ans.place(x=370, y=270, width=250)

        # Password
        password = Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        password.place(x=50, y=310)

        self.txt_password = Entry(frame1, font=("times new roman", 15), bg="lightgray", show='*')
        self.txt_password.place(x=50, y=340, width=250)

        # Confirm Password
        c_password = Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        c_password.place(x=370, y=310)

        self.txt_c_password = Entry(frame1, font=("times new roman", 15), bg="lightgray", show='*')
        self.txt_c_password.place(x=370, y=340, width=250)

        # Checkbutton
        self.var_chk = IntVar()
        chk = Checkbutton(frame1, text='I Agree The Terms And Conditions', variable=self.var_chk, onvalue=1, offvalue=0, bg="white", font=("times new roman", 12))
        chk.place(x=50, y=380)

        # Buttons
        btn_reg = Button(frame1, text="Register", font=("times new roman", 15, "bold"), bg="green", fg="white", cursor="hand2", command=self.register_data)
        btn_reg.place(x=50, y=420, width=180, height=40)

        btn_login = Button(frame1, command=self.login_call, text="Login", font=("times new roman", 15, "bold"), bg="red", fg="white", cursor="hand2")
        btn_login.place(x=370, y=420, width=180, height=40)

    def clear(self):
        self.txt_fname.delete(0, END)
        self.txt_username.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.cmb_quest.current(0)
        self.txt_sec_ans.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_c_password.delete(0, END)
        self.var_chk.set(0)

    def register_data(self):
        if (self.txt_fname.get() == "" or
                self.txt_username.get() == "" or
                self.txt_contact.get() == "" or
                self.txt_email.get() == "" or
                self.cmb_quest.get() == "Select" or
                self.txt_sec_ans.get() == "" or
                self.txt_password.get() == "" or
                self.txt_c_password.get() == ""):
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        elif self.txt_password.get() != self.txt_c_password.get():
            messagebox.showerror("Error", "Password and Confirm Password should be same", parent=self.root)
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error", "Please Agree to our Terms and Conditions", parent=self.root)
        else:
            try:
                conn = sqlite3.connect("ims.db")
                cur = conn.cursor()
                cur.execute("""
                    INSERT INTO register (f_name, username, contact, email, sec_ques, sec_ans, password)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (
                    self.txt_fname.get(),
                    self.txt_username.get(),
                    self.txt_contact.get(),
                    self.txt_email.get(),
                    self.cmb_quest.get(),
                    self.txt_sec_ans.get(),
                    self.txt_password.get()
                ))
                conn.commit()
                conn.close()
                self.clear()
                messagebox.showinfo("Success", "Registration Successful", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error due to: {str(e)}", parent=self.root)

    def login_call(self):
        self.root.destroy()
        newwind = Tk()
        from login import Login_System
        obj = Login_System(newwind)
        newwind.mainloop()

if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()
