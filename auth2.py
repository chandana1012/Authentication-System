#Tkinter is the standard GUI library for Python.
#Python when combined with Tkinter provides a fast and easy way to create GUI applications.
from tkinter import*
import os

def application():
    global  screen4
    screen4=Toplevel(screen)
    screen4.geometry("300x300")
    screen4.configure(background="peachpuff")
    screen4.title("appication")
    Label(screen4,text="SUCCESSFULL LOGIN ",bg="orangered",width="300",height="2",font=("calibri",25)).pack()
    

def delete3():
    screen3.destroy()
    application()
    
def successfullb():
    screen33.destroy()
    delete3()
    
def unsuccessfullb():
    screen33.destroy()
    opengreen()
    
def verifyBlue():
    list_of_files=os.listdir()
    if username1 in list_of_files:
        file1=open(username1,"r")
        verify=file1.read().splitlines()
        file1.close
    if str(lbb) in verify:
        successfullb()
    else:
        unsuccessfullb()

def applb():
    lbb.append("lb130")
def appdsb():
    lbb.append( "lsb131")
def appcb():
    lbb.append("cb132")
def appdb():
    lbb.append("db134")
def apprb():
    lbb.append("rb135")
def apppb():
    lbb.append("pb136")
def appb():
    lbb.append("b137")
def appn():
    lbb.append("n138")
def applsb():
    lbb.append("lsb133") 
def openblue():
    global screen33,lbb
    screen33=Toplevel(screen3)
    screen33.title("blue")
    lbb=[]
    Button(screen33,width = 10, height= 5, bg="lightblue" ,command=applb).grid(row = 0,column = 0)
    Button(screen33,width = 10, height= 5, bg="deepskyblue" ,command=appdsb).grid(row = 0,column = 1)
    Button(screen33,width = 10, height= 5, bg="cornflowerblue",command=appcb).grid(row = 0,column = 2)
    Button(screen33,width = 10, height= 5, bg="dodgerblue" ,command=appdb).grid(row = 1,column = 0)
    Button(screen33,width = 10, height= 5, bg="royalblue",command=apprb ).grid(row =1 ,column = 1)
    Button(screen33,width = 10, height= 5, bg="powderblue" ,command=apppb).grid(row = 1,column = 2)
    Button(screen33,width = 10, height= 5, bg="blue",command=appb).grid(row = 2,column = 0)
    Button(screen33,width = 10, height= 5, bg="navy" ,command=appn).grid(row = 2,column = 1)
    Button(screen33,width = 10, height= 5, bg="lightskyblue" ,command=applsb).grid(row = 2,column = 2)
    Button(screen33,text="OK",bg="limegreen",width=10,height=1,command=verifyBlue).grid(row=3,column=1)    

def successfullg():
    screen32.destroy()
    openblue()
    
def unsuccessfullg():
    screen32.destroy()
    openred()        

def verifyGreen():
    list_of_files=os.listdir()
    if username1 in list_of_files:
        file1=open(username1,"r")
        verify=file1.read().splitlines()
        file1.close
    if str(lgg) in verify:
        successfullg()
    else:
        unsuccessfullg()
        
def appgy():
    lgg.append("gy140")
def appg():
    lgg.append("g141")
def apppg():
    lgg.append("pg142")
def appod():
    lgg.append("od144")
def appmsg():
    lgg.append("msg145")
def appsg():
    lgg.append("sg146")
def appyg():
    lgg.append("yg148")
def applig():
    lgg.append("lig147")
def appspg():
    lgg.append("spg143")

def opengreen():
    global screen32,lgg
    screen32=Toplevel(screen3)
    screen32.title("green")
    lgg=[]
    Button(screen32,width = 10, height= 5, bg="greenyellow" ,command=appgy).grid(row = 0,column = 0)
    Button(screen32,width = 10, height= 5, bg="green" ,command=appg).grid(row = 0,column = 1)
    Button(screen32,width = 10, height= 5, bg="palegreen",command=apppg).grid(row = 0,column = 2)
    Button(screen32,width = 10, height= 5, bg="olivedrab" ,command=appod).grid(row = 1,column = 0)
    Button(screen32,width = 10, height= 5, bg="mediumspringgreen",command=appmsg ).grid(row =1 ,column = 1)
    Button(screen32,width = 10, height= 5, bg="seagreen" ,command=appsg).grid(row = 1,column = 2)
    Button(screen32,width = 10, height= 5, bg="limegreen",command=applig ).grid(row = 2,column = 0)
    Button(screen32,width = 10, height= 5, bg="yellowgreen" ,command=appyg).grid(row = 2,column = 1)
    Button(screen32,width = 10, height= 5, bg="springgreen" ,command=appspg).grid(row = 2,column = 2)
    Button(screen32,text="OK",bg="limegreen",width=10,height=1,command=verifyGreen).grid(row=3,column=1)                

def successfullr():
    screen31.destroy()
    opengreen()
    
def unsuccessfullr():
    screen3.destroy()
    login()        
        
def verifyRed():
    list_of_files=os.listdir()
    if username1 in list_of_files:
        file1=open(username1,"r")
        verify=file1.read().splitlines()
        file1.close
    if str(lrr) in verify:
        successfullr()
    else:
        unsuccessfullr()

def appls():
    lrr.append("ls120")
def apps():
    lrr.append("s121")
def applc():
    lrr.append("lc122")
def appir():
    lrr.append("ir123")
def appds():
    lrr.append("ds124")
def appc():
    lrr.append("c125")
def appfb():
    lrr.append("fr126")
def appr():
    lrr.append("r127")
def appdr():
    lrr.append("dr128")

def openred():
    global screen31,lrr
    screen31=Toplevel(screen3)
    screen31.title("red")
    lrr=[]
    Button(screen31,width = 10, height= 5, bg="light salmon" ,command=appls).grid(row = 0,column = 0)
    Button(screen31,width = 10, height= 5, bg="salmon" ,command=apps).grid(row = 0,column = 1)
    Button(screen31,width = 10, height= 5, bg="light coral",command=applc).grid(row = 0,column = 2)
    Button(screen31,width = 10, height= 5, bg="indian red" ,command=appir).grid(row = 1,column = 0)
    Button(screen31,width = 10, height= 5, bg="dark salmon",command=appds).grid(row =1 ,column = 1)
    Button(screen31,width = 10, height= 5, bg="crimson" ,command=appc).grid(row = 1,column = 2)
    Button(screen31,width = 10, height= 5, bg="firebrick",command=appfb ).grid(row = 2,column = 0)
    Button(screen31,width = 10, height= 5, bg="red" ,command=appr).grid(row = 2,column = 1)
    Button(screen31,width = 10, height= 5, bg="darkred" ,command=appdr).grid(row = 2,column = 2)
    Button(screen31,text="OK",bg="limegreen",width=10,height=1,command=verifyRed).grid(row=3,column=1)

def delete2():
    screen2.destroy()
    
def level2password():
    global screen3
    screen3=Toplevel(screen)
    screen3.title("Graphical password")
    screen3.geometry("500x500")
    screen3.configure(background="antiquewhite")
    delete2()
    
    Label(screen3,text="ENTER COLOR PASSWORD ",bg="peachpuff",width="200",height="1",font=("calibri",13)).pack()
    Label(screen3,text="").pack()

    global lt
    lt=[]
    Button(screen3,bg="red",width=8,height=1,command=openred).pack()
    Button(screen3,bg="green",width=8,height=1,command=opengreen).pack()
    Button(screen3,bg="blue",width=8,height=1,command=openblue).pack()
    
    Label(screen3,text="").pack()
    Label(screen3,text="").pack()
    Button(screen3,text="verify",bg="limegreen",width=10,height=1,command=application).pack()

def login_success():
    Label(screen2,text="login successfull...",bg="floralwhite").pack()
    
def user_not_found():
    global screen01
    screen01=Toplevel(screen)
    screen01.title("user")
    screen01.geometry("150x100")
    Label(screen01,text="user does not exist",foreground="red").pack()
    Button(screen01,text="OK",command=delete01).pack()
    
def delete01():
    screen01.destroy()    

def password_not_recognised():
    global screen02
    screen02=Toplevel(screen)
    screen02.title("password")
    screen02.geometry("150x100")
    Label(screen02,text="wrong password",foreground="red").pack()
    Button(screen02,text="OK",command=delete02).pack()
    
def delete02():
    screen02.destroy()

def login_verify():
    global username1
    username1=username_verify.get()
    password1=password_verify.get()
    username_entry1.delete(0,END)
    password_entry1.delete(0,END)

    list_of_files=os.listdir()
    if username1 in list_of_files:
        file1=open(username1,"r")
        verify=file1.read().splitlines()
        if password1 in verify:
            login_success()
            level2password()
        else:
            password_not_recognised()
    else:
        user_not_found()

def login():
    global screen2
    screen2=Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("400x350")
    screen2.configure(background="antiquewhite")
    global username_verify
    global password_verify

    global username_entry1
    global password_entry1

    username_verify=StringVar()
    password_verify=StringVar()

    Label(screen2,text="LOGIN WITH VALID USERID",bg="peachpuff",width="200",height="1",font=("calibri",13)).pack()
    Label(screen2,text="").pack()
    Label(screen2,text="username * ",bg="floralwhite").pack()
    username_entry1=Entry(screen2,textvariable=username_verify)
    username_entry1.pack()
    Label(screen2,text="password * ",bg="floralwhite").pack()
    password_entry1=Entry(screen2,textvariable=password_verify)
    password_entry1.pack()
    Label(screen2,text="").pack()
    Button(screen2,text="Login",bg="limegreen",width=10,height=1,command=login_verify).pack()

def delete1():
    Label(screen1,text="successful registration......",bg="floralwhite").pack()
    screen1.destroy()
   
def de13():
    file=open(username_info,"a")
    file.write(str(lb)+'\n')
    file.close()
    code.set("*******")
    screen13.destroy()
    
def lit_blue():
    lb.append("lb130")
def lit_sblue():
    lb.append( "lsb131")
def corn_blue():
    lb.append("cb132")
def d_blue():
    lb.append("db134")
def r_blue():
    lb.append("rb135")
def pb_blue():
    lb.append("pb136")
def blue():
    lb.append("b137")
def navy():
    lb.append("n138")
def ls_blue():
    lb.append("lsb133")
    
#grid of 3X3 with shades of blue
def blue_code():
    global screen13,lb
    screen13=Toplevel(screen1)
    screen13.title("blue")
    lb=[]
    Button(screen13,width = 10, height= 5, bg="lightblue" ,command=lit_blue).grid(row = 0,column = 0)
    Button(screen13,width = 10, height= 5, bg="deepskyblue" ,command=lit_sblue).grid(row = 0,column = 1)
    Button(screen13,width = 10, height= 5, bg="cornflowerblue",command=corn_blue ).grid(row = 0,column = 2)
    Button(screen13,width = 10, height= 5, bg="dodgerblue" ,command=d_blue).grid(row = 1,column = 0)
    Button(screen13,width = 10, height= 5, bg="royalblue",command=r_blue ).grid(row =1 ,column = 1)
    Button(screen13,width = 10, height= 5, bg="powderblue" ,command=pb_blue).grid(row = 1,column = 2)
    Button(screen13,width = 10, height= 5, bg="blue",command=blue ).grid(row = 2,column = 0)
    Button(screen13,width = 10, height= 5, bg="navy" ,command=navy).grid(row = 2,column = 1)
    Button(screen13,width = 10, height= 5, bg="lightskyblue" ,command=ls_blue).grid(row = 2,column = 2)
    Button(screen13,text="OK",bg="limegreen",width=10,height=1,command=de13).grid(row=3,column=1)    

def de12():
    file=open(username_info,"a")
    file.write(str(lg)+'\n')
    file.close()
    code.set("*******")
    screen12.destroy()

def gy():
    lg.append("gy140")
def g():
    lg.append("g141")
def pg():
    lg.append("pg142")
def od():
    lg.append("od144")
def msg():
    lg.append("msg145")
def sg():
    lg.append("sg146")
def lig():
    lg.append("lig147")
def yg():
    lg.append("yg148")
def spg():
    lg.append("spg143")
    
#grid of 3X3 with shades of green   
def green_code():
    global screen12,lg
    screen12=Toplevel(screen1)
    screen12.title("green")
    lg=[]
    Button(screen12,width = 10, height= 5, bg="greenyellow" ,command=gy).grid(row = 0,column = 0)
    Button(screen12,width = 10, height= 5, bg="green" ,command=g).grid(row = 0,column = 1)
    Button(screen12,width = 10, height= 5, bg="palegreen",command=pg).grid(row = 0,column = 2)
    Button(screen12,width = 10, height= 5, bg="olivedrab" ,command=od).grid(row = 1,column = 0)
    Button(screen12,width = 10, height= 5, bg="mediumspringgreen",command=msg ).grid(row =1 ,column = 1)
    Button(screen12,width = 10, height= 5, bg="seagreen" ,command=sg).grid(row = 1,column = 2)
    Button(screen12,width = 10, height= 5, bg="limegreen",command=lig ).grid(row = 2,column = 0)
    Button(screen12,width = 10, height= 5, bg="yellowgreen" ,command=yg).grid(row = 2,column = 1)
    Button(screen12,width = 10, height= 5, bg="springgreen" ,command=spg).grid(row = 2,column = 2)
    Button(screen12,text="OK",bg="limegreen",width=10,height=1,command=de12).grid(row=3,column=1)

def de11():
    file=open(username_info,"a")
    file.write(str(lr)+'\n')
    file.close()
    code.set("*******")
    screen11.destroy()

def drkred():
    lr.append("dr128")
def drk_sal():
    lr.append("ds124")
def lit_sal():
    lr.append("ls120")
def sal():
    lr.append("s121")
def lit_cor():
    lr.append("lc122")
def indianred():
    lr.append("ir123")
def crimson():
    lr.append("c125")
def firebrick():
    lr.append("fr126")
def red():
    lr.append("r127")
      
#grid of 3X3 with shades of red     
def red_code():
    global screen11,lr
    lr=[]
    screen11=Toplevel(screen1)
    screen11.title("red")
    Button(screen11,width = 10, height= 5, bg="light salmon" ,command=lit_sal).grid(row = 0,column = 0)
    Button(screen11,width = 10, height= 5, bg="salmon" ,command=sal).grid(row = 0,column = 1)
    Button(screen11,width = 10, height= 5, bg="light coral",command=lit_cor ).grid(row = 0,column = 2)
    Button(screen11,width = 10, height= 5, bg="indian red" ,command=indianred).grid(row = 1,column = 0)
    Button(screen11,width = 10, height= 5, bg="dark salmon",command=drk_sal ).grid(row =1 ,column = 1)
    Button(screen11,width = 10, height= 5, bg="crimson" ,command=crimson).grid(row = 1,column = 2)
    Button(screen11,width = 10, height= 5, bg="firebrick",command=firebrick ).grid(row = 2,column = 0)
    Button(screen11,width = 10, height= 5, bg="red" ,command=red).grid(row = 2,column = 1)
    Button(screen11,width = 10, height= 5, bg="darkred" ,command=drkred).grid(row = 2,column = 2)
    Button(screen11,text="OK",bg="limegreen",width=10,height=1,command=de11).grid(row=3,column=1)

#entering username and password into file
def enter_user():
    global username_info
    global password_info
   
    username_info=username.get()
    password_info=password.get()
    list_of_files=os.listdir()
    if username_info in list_of_files:
        global s1
        s1=Toplevel(screen1)
        s1.title("user")
        s1.geometry("150x100")
        Label(s1,text="user already exist",foreground="red").pack()
        Button(s1,text="OK",command=d1).pack()
        username_entry.delete(0,END)
        password_entry.delete(0,END)
    else:
        file=open(username_info,"w")
        file.write(username_info+"\n")
        file.write(password_info+"\n")
        file.close()

def d1():
    s1.destroy()    

#registration     
def register():
    global screen1
    screen1=Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("500x500")
    screen1.configure(background="antiquewhite")
    
    global username
    global password

    
    
    global code

    
    global username_entry
    global password_entry

    username=StringVar()
    password=StringVar()
    code=StringVar()
    
    Label(screen1,text="ENTER DETAILS FOR LEVEL 1  AUTHENTICATION",bg="peachpuff",width="200",height="1",font=("calibri",13)).pack()
    Label(screen1,text="").pack()
    Label(screen1,text="Username:",bg="floralwhite").pack()
    username_entry=Entry(screen1,textvariable=username)
    username_entry.pack()
    Label(screen1,text="Password:",bg="floralwhite").pack()
    password_entry=Entry(screen1,textvariable=password)
    password_entry.pack()
    Label(screen1,text="").pack()

    Button(screen1,text="Enter",bg="limegreen",width=10,height=1,
           command=enter_user).pack()
    Label(screen1,text="").pack()
    
    Label(screen1,text="ENTER COLOR PASSWORD FOR LEVEL 2 AUTHENTICATION",bg="peachpuff",width="200",height="1",font=("calibri",13)).pack()
    Label(screen1,text="").pack()
    
    Button(screen1,bg="red",width=8,height=1,command=red_code).pack()
    Button(screen1,bg="green",width=8,height=1,command=green_code).pack()
    Button(screen1,bg="blue",width=8,height=1,command=blue_code).pack()
    Label(screen1,text="").pack()
    
    colorpassword_entry=Entry(screen1,textvariable=code)
    colorpassword_entry.pack()
    
    Label(screen1,text="").pack()
    Button(screen1,text="Submit",bg="limegreen",width=10,height=1,command=delete1).pack()

#main screen : HOME
#using tkinter Tk() , created a window (container) . 
def main_screen():
    global screen
    #The tkinter package (“Tk interface”) is the standard Python interface to the Tk GUI toolkit. 
    screen=Tk()
    screen.geometry("600x600")
    screen.configure(background="antiquewhite")
    screen.title("HOME")
    Label(text="AUTHENTICATION SYSTEM",bg="peachpuff",width="300",height="2",font=("calibri",13)).pack()
    Label(text="").pack()
    Label(text="").pack()
    Button(text="Login",bg="limegreen",height="2",width="30",command=login).pack()
    Label(text="").pack()
    Button(text="Register",bg="limegreen",height="2",width="30",command=register).pack()
    screen.mainloop()

#calling main_screen
main_screen()
