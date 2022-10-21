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
    root.title('Login')

    
    log=tk.Label(root,image=fine)
    log.place(x=0,y=0)

    usname=tk.Entry(root)
    usname.place(x=120,y=87,height=25)
    usname.configure(bd=2)

    pswd=tk.Entry(root,show='*')
    pswd.place(x=120,y=117,height=25)
    pswd.configure(bd=2)


    Def log():

        olduser=usname.get()
        oldpwd=pswd.get()
        With open('info.txt',"r") as userchk:
            For line in userchk:
                If older in line:
                    pwdchk=linecache.getline(olduser+'.txt',2)
                    If (oldpwd+'\n')==(pwdchk) :
                        root.destroy()
                        win.destroy()
                        Import can
                    Else:
                        notm=tk.Label(root,text='The Password did not match, Please try again.')
                        notm.place(x=0,y=155,width=300,height=15)
