from tkinter import * 
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
from Dashboard import IMS

class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Login_System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#e0f7fa")

        # Load and resize the BG image
        self.bg_image = Image.open("images/SK3.jpg")
        self.bg_image = self.bg_image.resize((1350, 700))
        self.bg = ImageTk.PhotoImage(self.bg_image)

        bg = Label(self.root, image=self.bg)
        bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Load and resize the left image
        self.left_image = Image.open("images/images.jpg")
        self.left_image = self.left_image.resize((400, 500))
        self.left = ImageTk.PhotoImage(self.left_image)

        lef = Label(self.root, image=self.left)
        lef.place(x=200, y=100, width=400, height=500)

        # Login Frame
        login_frame = Frame(self.root, bd=3, relief=RIDGE)
        login_frame.place(x=620, y=100, width=400, height=500)

        # Login Title
        title = Label(login_frame, text="Login System", font=("Elephant", 30, "bold"), bg="white", fg="black")
        title.place(x=50, y=30)

        # User Name
        lbl_uname = Label(login_frame, text="User Name", font=("Andalus", 15, "bold"), bg="white", fg="black")
        lbl_uname.place(x=50, y=100)
        self.txt_uname_Entry=StringVar()
        self.txt_uname = Entry(login_frame,textvariable=self.txt_uname_Entry, font=("times new roman", 15), bg="lightgray")
        self.txt_uname.place(x=50, y=140, width=280)

        # Password
        lbl_password = Label(login_frame, text="Password", font=("Andalus", 15, "bold"), bg="white", fg="black")
        lbl_password.place(x=50, y=200)
        self.txt_password_Entry=StringVar()
        self.txt_password = Entry(login_frame, textvariable=self.txt_password_Entry,font=("times new roman", 15), bg="lightgray", show="*")
        self.txt_password.place(x=50, y=240, width=280)

        # Login Button
        btn_login = Button(login_frame, text="Login", font=("Arial Rounded MT Bold", 15), bg="green",
                           activebackground="green", fg="white", activeforeground="white", cursor="hand2", command=self.login)
        btn_login.place(x=50, y=300, width=280, height=40)

        hr = Label(login_frame, bg="lightgrey")
        hr.place(x=50, y=360, width=280, height=4)
        or_ = Label(login_frame, text="OR", bg="white", fg="#00759B", font=("times new roman", 15, "bold"))
        or_.place(x=172, y=348)

        # Forgot Password
        btn_forgot = Button(login_frame, text="Forgot Password?", font=("times new roman", 13), bg="white",
                            fg="#00759B", bd=0, activebackground="white", activeforeground="#00759B")
        btn_forgot.place(x=50, y=380, width=280, height=40)

        # Register Frame
        register_frame = Frame(self.root, bd=3, relief=RIDGE)
        register_frame.place(x=630, y=520, width=380, height=70)

        lbl_reg = Label(register_frame, text="Don't have an Account?", font=("times new roman", 13), bg="white")
        lbl_reg.place(x=40, y=14)

        btn_signup = Button(register_frame, text="Register Here?", font=("times new roman", 13),
                            bg="white", fg="#00759B", bd=0, activebackground="white", activeforeground="#00759B")
        btn_signup.place(x=210, y=12)

    def login(self):
        username = self.txt_uname_Entry.get()
        password = self.txt_password_Entry.get()

        if username == "" or password == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                con = sqlite3.connect('ims.db')
                cur = con.cursor()
                cur.execute("SELECT * FROM register WHERE username = ? AND password = ?", (username, password))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Username or Password", parent=self.root)
                else:
                    messagebox.showinfo("Success", f"Welcome {username}", parent=self.root)
                    self.root.destroy()
                    dashboard_window = Tk()
                    IMS(dashboard_window)
                    dashboard_window.mainloop()
                    
                con.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)
if __name__ == "__main__":
    root = Tk()
    obj = Login_System(root)
    root.mainloop()
