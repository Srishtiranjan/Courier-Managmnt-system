
# coding: utf-8

# In[1]:


import tkinter as tk                # python 3
from tkinter import font  as tkfont# python 3
import sqlite3
from tkinter import messagebox
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='CopperblGoth Bd Bt', size=20, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, admins, mainn, Trackconsignment):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        m=tk.Message(self, text='Courier Managemen System',width=2000,font=controller.title_font, fg='green')
        b1=tk.Button(self, text='Admins', width=15, height=2,bg='blue',fg='white',command=lambda: controller.show_frame("admins"))
        b2=tk.Button(self, text='Login', width=15, height=2,bg='blue',fg='white', command=lambda: controller.show_frame("PageOne"))
        b3=tk.Button(self, text='Register', width=15, height=2,bg='blue',fg='white', command=lambda: controller.show_frame("PageTwo"))
        
        #self.b1=Button(self.f, text='', width=15, height=2)
        m.pack(side="top",fill="x", pady=10)
        b1.pack()
        b2.pack()
        b3.pack()
        m.pack(side="top",fill="x", pady=10)
        #label = tk.Label(self, text="This is the start page", font=controller.title_font)
        #label.pack(side="top", fill="x", pady=10)

        #button1 = tk.Button(self, text="Go to Page One",
         #                   command=lambda: controller.show_frame("PageOne"))
        #button2 = tk.Button(self, text="Go to Page Two",
                           # command=lambda: controller.show_frame("PageTwo"))
        #button1.pack()
        #button2.pack()
class admins(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        a1=tk.Label(self,text='Login Module:', width=25, height=3, fg='blue', font=controller.title_font )
        a2=tk.Label(self,text='Srishti Ranjan', width=15, fg='red', font=controller.title_font )
        a3=tk.Label(self,text='11807941', width=15,fg='red', font=controller.title_font )
        a4=tk.Label(self,text='Registration module:', width=25, height=3, fg='blue', font=controller.title_font )
        a5=tk.Label(self,text='Sri Hari Rai', width=15, fg='red', font=controller.title_font )
        a6=tk.Label(self,text='11807979', width=15, fg='red', font=controller.title_font )
        a7=tk.Label(self,text='Track Consignment Module:', width=25, height=3, fg='blue', font=controller.title_font )
        a8=tk.Label(self,text='Sai Krishna Lohith Adi', width=25, fg='red', font=controller.title_font )
        a9=tk.Label(self,text='11******', width=20, height=2, fg='red', font=controller.title_font )
        b1=tk.Button(self,text='home',bg='blue',fg='white',command=lambda: controller.show_frame("StartPage"))
        a1.pack()
        a2.pack()
        a3.pack()
        a4.pack()
        a5.pack()
        a6.pack()
        a7.pack()
        a8.pack()
        a9.pack()
        b1.pack()
        
        
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        l1=tk.Label(self,text='Enter Registration No:')
        l2=tk.Label(self,text='Enter password:')
        label_0 = tk.Label(self, text="Login",width=2000,font=controller.title_font,fg='green')
        label_0.pack(side="top",fill="x", pady=10)

        #create entry widget fro user name
        self.var1=tk.StringVar()
        self.var2=tk.StringVar()
        self.e1=tk.Entry(self, width=25, fg='white', bg='blue',  textvar=self.var1,font=('Arial', 14))

        #create entry widget for password, the text in widget
        #replace by *

       
        self.e2=tk.Entry(self, width=25, fg='white', bg='blue',textvar=self.var2,
                      font=('Arial', 14),show='*')

        #when user press enter, bind that event to display method

        self.e1.bind('button2')
        self.e2.bind('button2')

        #place labels and entry widgets in teh frame
        l1.place(x=75,y=100)
        l2.place(x=75,y=150)
        self.e1.place(x=200,y=100)
        self.e2.place(x=200,y=150)
        
        #label = tk.Label(self, text="This is page 1", font=controller.title_font)
        #label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Home",bg='blue',fg='white',
                           command=lambda: controller.show_frame("StartPage"))
        str1=self.var1.get()
        button2 = tk.Button(self, text="login",bg='blue',fg='white', command=self.des)
        
        
        button1.place(x=350,y=200)
        button2.place(x=250,y=200)
        
    
    def des(self):
        with sqlite3.connect('Form.db') as db:
            c = db.cursor()
            #Find user If there is any take proper action
        find_user = ('SELECT * FROM Student2 WHERE Registration = ? and Passw = ?')
        c.execute(find_user,[(self.var1.get()),(self.var2.get())])
        result = c.fetchall()
        if result:
            app.show_frame("mainn")
        else:
            
            messagebox.showinfo("Error", "Wrong user name or password")
        
        

    


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #conn = sqlite3.connect('test.db')
        #label = tk.Label(self, text="This is page 2", font=controller.title_font)
        #label.pack(side="top", fill="x", pady=10)
        self.name1=tk.StringVar()
        self.reg1=tk.IntVar()
        self.gender1=tk.IntVar()
        self.mobile1=tk.StringVar()
        self.email1=tk.StringVar()
        self.pass1=tk.StringVar()
        button = tk.Button(self, text="Home",
                           command=lambda: controller.show_frame("StartPage"))
        
        label_0 = tk.Label(self, text="Registration form",width=20,font=controller.title_font,fg='green')
        #label_0.place(x=90,y=53)
        label_0.pack(side="top",fill="x", pady=10)


        label_1 = tk.Label(self, text="FullName",width=20,font=("bold", 10))
        label_1.place(x=80,y=130)

        entry_1 = tk.Entry(self, width=25,textvar=self.name1, fg='white', bg='blue',font=('Arial', 14))
        entry_1.place(x=240,y=130)

        label_2 = tk.Label(self, text="Registration No.",width=20,font=("bold", 10))
        label_2.place(x=68,y=180)

        entry_2 = tk.Entry(self,width=25, fg='white',textvar=self.reg1, bg='blue',font=('Arial', 14))
        entry_2.place(x=240,y=180)

        label_3 = tk.Label(self, text="Gender",width=20,font=("bold", 10))
        label_3.place(x=70,y=230)
        self.var = tk.IntVar()
        tk.Radiobutton(self, text="Male",padx = 5, variable='var', value=1).place(x=235,y=230)
        tk.Radiobutton(self, text="Female",padx = 20, variable='var', value=2).place(x=290,y=230)
        label_7 = tk.Label(self, text="Mobile",width=20,font=("bold", 10))
        label_7.place(x=70,y=280)

        entry_7 = tk.Entry(self, width=25, fg='white',textvar=self.mobile1, bg='blue',font=('Arial', 14))
        entry_7.place(x=240,y=280)
        label_8 = tk.Label(self, text="Email ID",width=20,font=("bold", 10))
        label_8.place(x=70,y=330)

        entry_8 = tk.Entry(self, width=25, fg='white',textvar=self.email1, bg='blue',font=('Arial', 14))
        entry_8.place(x=240,y=380)
        label_8 = tk.Label(self, text="Create Password",width=20,font=("bold", 10))
        label_8.place(x=70,y=380)

        entry_8 = tk.Entry(self, width=25, fg='white',textvar=self.pass1, bg='blue',font=('Arial', 14))
        entry_8.place(x=240,y=330)

        

        b2=tk.Button(self, text='Submit',width=20,bg='blue',fg='white',command=self.database)
        b2.place(x=180,y=420)
        button.pack()
    def database(self):
        conn = sqlite3.connect('Form.db')
        c=conn.cursor()
        find_user = ('SELECT * FROM Student2 WHERE Registration = ?')
        c.execute(find_user,[(self.reg1.get())])        
        if c.fetchall():
            messagebox.showinfo("Error", "user name is taken")
        else:
            
            name=self.name1.get()
            regn1=self.reg1.get()
            gender=self.var.get()
            mobile=self.mobile1.get()
            email=self.email1.get()
            password=self.pass1.get()

            with conn:
                cursor=conn.cursor()
                cursor.execute('CREATE TABLE IF NOT EXISTS Student2 (Fullname TEXT,Registration TEXT,Gender TEXT,Mobile TEXT,Email TEXT,Passw TEXT)')
                cursor.execute('INSERT INTO Student2 (FullName,Registration,Gender,Mobile,Email,Passw) VALUES(?,?,?,?,?,?)',(name,regn1,gender,mobile,email,password,))
            conn.commit()
            conn.close()
        messagebox.showinfo("success", "your account is created")
class mainn(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.var1=tk.StringVar()
        
        
        label_8 = tk.Label(self, text='welcome user',width=20,font=controller.title_font)
        label_9 = tk.Label(self, text='we are here to help you with your courier we provide the best service for a best user experiance',fg='blue', width=50,font=('bremen bd bt',40))
        label_10 = tk.Label(self, text='you can track your consignment by clicking track consignment button ',width=50,fg='blue',font=('bremen bd bt',40))
        label_11= tk.Label(self, text='you can navigate to home by clicking home button',width=50,fg='blue',font=('bremen bd bt',40))
        button1 = tk.Button(self, text="Home",bg='blue',fg='white',
                           command=lambda: controller.show_frame("StartPage"))
        button2 = tk.Button(self, text="Track consignment",bg='blue',fg='white',
                           command=lambda: controller.show_frame("Trackconsignment"))
        label_8.pack()
        label_9.pack()
        label_10.pack()
        label_11.pack()
        
        
        button1.place(x=300,y=300)
        button2.place(x=400,y=300)
class Trackconsignment(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        lbll=tk.Label(self,text='Track Your Package',width=2000,font=controller.title_font,fg='green')
        self.mn=tk.StringVar()
        self.cn=tk.StringVar()
        lb1=tk.Label(self,text='mobile number:', width=20, font=('bold',10) )
        lb2=tk.Label(self,text='consignment number:', width=20, font=('bold',10) )
        self.et1=tk.Entry(self, width=25, fg='white',textvar=self.mn, bg='blue',font=('Arial', 14))
        self.et2=tk.Entry(self, width=25, fg='white',textvar=self.cn, bg='blue',font=('Arial', 14))
        bt1=tk.Button(self, text='track', bg='blue', fg='white',command=self.diss)
        bt2 = tk.Button(self, text="Home",bg='blue', fg='white',command=lambda: controller.show_frame("StartPage"))
        lb1.place(x=50,y=50)
        lb2.place(x=50,y=100)
        self.et1.place(x=200,y=50)
        self.et2.place(x=200,y=100)
        bt1.place(x=200,y=150)
        bt2.place(x=275,y=150)
        lbll.pack()
    def diss(self):
        self.var11=tk.StringVar()
        with sqlite3.connect('Form.db') as db:
            c = db.cursor()
            #Find user If there is any take proper action
        find_user = ('SELECT * FROM Student2 WHERE Mobile=?')
        c.execute(find_user,[(self.var11.get())])
        result = c.fetchall()
        str11=self.et2.get()
        str22=self.et1.get()
        if str22==result:
            if str11=='lp00001':
                messagebox.showinfo("update", "your package is dispached")
            elif str11=='lp00002':
                messagebox.showinfo("update", "your package is on the way we will update you shortly")
            elif str11=='lp00003':
                messagebox.showinfo("update", "your package is ready for pickup")
            elif str11=='lp00004':
                messagebox.showinfo("update", "your package is about to delivery")
            elif str11=='lp00005':
                messagebox.showinfo("update", "your package is dispached")
            elif str11=='lp00006':
                messagebox.showinfo("update", "your package is on the way")
            elif str11=='lp00007':
                messagebox.showinfo("update", "your package is about to delivery")
            elif str11=='lp00008':
                messagebox.showinfo("update", "your package is cancelled by user")
                    
            elif str11=='lp00009':
                messagebox.showinfo("update", "your package is cancelled by user")
                        
            
            elif str11=='lp00010':
                messagebox.showinfo("update", "your package is returned due to incorrect address")
            else:
                messagebox.showinfo("Error", "invalid details")
        else:
            messagebox.showinfo("Error",'Wrong details')

            
        


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()


# In[94]:


import sqlite3
conn = sqlite3.connect('Form.db')
cursor=conn.execute('SELECT Fullname,Registration,email,mobile FROM Student2')
#data=cursor.fetchall()
for row in cursor:
    print ("ID =", row[0])
    print ("NAME = ", row[1])
    print ("ADDRESS = ", row[2])
    print ("SALARY = ", row[3], "\n")
conn.close()

