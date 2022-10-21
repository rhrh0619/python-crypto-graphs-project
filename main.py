Import tinter as tk
Import linecache
Import smtplib,ssl
Import random
Import os

win=tk.Tk()
win.configure(bg='black')
win.geometry('450x500')
win.title('CRYPTOGYAN')
line=tk.PhotoImage(file='bg4.png')
ln=tk.Label(win,image=line,bd=0)
ln.pack()
win.resizable(0,0)
fine=tk.PhotoImage(file='logbg.png')
tp=tk.PhotoImage(file='otp.png')
Def login():
    root=tk.Toplevel()
    root.geometry('300x200')
