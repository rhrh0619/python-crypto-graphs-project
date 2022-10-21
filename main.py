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
                        notm.configure(bg='#dbcdab',fg='#1B263B')
                
                Else:
                    notm=tk.Label(root,text='The account doesnot exist.')
                    notm.place(x=0,y=150,width=300,height=15)
                    notm.configure(bg='#dbcdab',fg='#1B263B')
                    but2=tk.Button(root,text='CREATE AN ACCOUNT',bg='#dbcdab',fg='#1B263B',command=cacc)
                    but2.configure(bd=0,font=('fixed sys',20))
                    but2.place(x=0,y=165,width=300,height=35)
    but=tk.Button(root,text='LOGIN',bg='#dbcdab',fg='#1B263B',command=log)
    but.configure(bd=0,font=('fixedsys',20))
    but.place(x=0,y=165,width=300,height=35)
    root.resizable(0,0)
    #but1.place(x=1330,y=25,height=20)

cacbg=tk.PhotoImage(file='cacbg.png')


def cacc():
    root=tk.Toplevel()
    root.geometry('400x300')
    root.title('Create an account')

    log=tk.Label(root,image=cacbg,bd=0)
    log.place(x=0,y=0)
    
    usnamen=tk.Entry(root)
    usnamen.place(x=200,y=110,height=25)
    usnamen.configure(bd=2)
    
    
    pswdn=tk.Entry(root,show='*')
    pswdn.place(x=200,y=140,height=25)
    pswdn.configure(bd=2)

    pswdcn=tk.Entry(root,show='*')
    pswdcn.place(x=200,y=170,height=25)
    pswdcn.configure(bd=2)

    seck=tk.Entry(root)
    seck.place(x=200,y=200,height=25)
    seck.configure(bd=2)

        else:
            notm=tk.Label(root,text='The Password did not match, Please try again.')
            notm.place(x=0,y=250,width=400,height=15)
            notm.configure(bg='#dbcdab',fg='#1B263B')
            
                
    but=tk.Button(root,text='CREATE ACCOUNT',bg='#dbcdab',fg='#1B263B',command=get)
    but.configure(bd=0,font=('fixedsys',20))
    but.place(x=0,y=265,width=400,height=35)
    root.resizable(0,0)
    #but1.place(x=1330,y=25,height=20)

                
def c():
    win.destroy()
    import cannot    
     

    
    

but1=tk.Button(win,text='LOGIN ',bg='#dbcdab',fg='#1B263B',command=login)
but1.configure(bd=0,font=('fixedsys',20))
but1.place(x=0,y=300,width=450,height=35)

but2=tk.Button(win,text='CREATE AN ACCOUNT',bg='#dbcdab',fg='#1B263B',command=cacc)
but2.configure(bd=0,font=('fixedsys',20))
but2.place(x=0,y=360,width=450,height=35)

but3=tk.Button(win,text='ENTER AS GUEST',bg='#dbcdab',fg='#1B263B',command=c)
but3.configure(bd=0,font=('fixedsys',20))
but3.place(x=0,y=420,width=450,height=35)



win.mainloop()
