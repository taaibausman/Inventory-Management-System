from tkinter import *
from Dashboard import IMS
from login import Login_System
from register import Register
def main():
    window = Tk()
    register_obj = Register(window)
    window.mainloop()

main()