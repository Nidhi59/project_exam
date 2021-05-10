import tkinter.ttk as tkrtk
import threading
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql
import random

question = ["Ques. In the shell, by default, all variables are considered and stored as",
   "Ques. Which is the core of the operating system?",
   "Ques. Applications communicate with kernel by using:", 
   "Ques. Which of the following enables multi-tasking in UNIX?",
   "Ques. Which of the following is considered as the super daemon in Unix?",
   "Ques. Which command is used to set terminal IO characteristic?",
   "Ques. Which command is used to print a file",
   "Ques. Which option of ls command used to view file inode number",
   "Ques. Which command is used to view compressed text file contents",
   "Ques. Which command is used to extract intermediate result in a pipeline",
   "Ques. Which option of rm command is used to remove a directory with all its \n subdirectories",
   "Ques. Command used to determine the path of an executable file is",
   "Ques. Which of the following command output contains userid?",
   "Ques. Which of the following commands can be used to change default permissions \n for files and directories at the time of creation",
   "Ques. Write the command to display the current date in the form dd/mm/yyyy.",
   "Ques. Which one shows the name of the operating system?",
   "Ques. How to execute ls command inside a vi editor?",
   "Ques. Which represents the user home directory",
   "Ques. How do you rename file “new” to file “old”?",
   "Ques. If two files on same partition point to the same inode structure they are called",
   "Ques. Which command is used to change permissions of files and directories?",
   "Ques. The directory file contains:",
   "Ques. Which directory contain device special files?",
   "Ques. Which command is used to bring the background process to forground?",
   "Ques. How to run a process in the background?",
   "Ques. When a child process exits before the parent process exits, which of the \n following is true:",
   "Ques. A user can change the default log-in shell using",
   "Ques. User id 0 is",
   "Ques. While executing a command, the shell",
   "Ques. Hidden files are" ]

answers_choice =[
      ["string","integer","character","float"],
      ["Shell","Kernel","Commands","Script"],
      ["System Calls","C Programs","Shell Script","Shell"],
      ["Time Sharing","Multi programming","Multi user","Modularity"],
      ["sysinit","init","inetd","proc"],
      ["tty","ctty","ptty","stty"],
      ["print","ptr","lpr","none of the mentioned"],
      ["–l","-o","–a","–i"],
      ["cat","type","zcat","print"],
      ["tee","extract","exec","none of the mentioned"],
      ["–b","–o","–p","–r"],
      ["which","where","wexec","what"],
      ["ls","help","date","ls –l"],
      ["Chmod","Chown","Umask","Chgrp"],
      ["date +%d/%m/%Y","date +”%d/%m/%Y”","date +/%d/%m/20%y","date +”/%d/%m/20%y”"],
      ["uname -n","uname -r","uname -o","uname –m"],
      ["!ls",":ls",":!ls","we can’t execute"],
      ["/",".","..","~"],
      ["mv new old","move new old","cp new old","rn new old"],
      ["Soft links","Hard links","Alias","Special files"],
      ["mv","chgrp","chmod","set"],
      ["File names & File Sizes","File names & Inode Numbers","File names & Address","File names & Permissions"],
      ["/etc","/etc/dev","/root/bin","/dev"],
      ["bg","fg","background","forground"],
      ["&","*","?","|"],
      ["the child process becomes defunct","the parent process becomes defunct",
      "if the parent process does not handle SIGCHLD, the child process becomes a zombie","none of the mentioned"],
      ["chmod","chsh","rmsh","tchsh"],
      ["An invalid user id","The id of the root user","The id of a user when the user’s account is deleted","None of the mentioned"],
      ["Executes it in the same process (as shell)","Creates a child shell to execute it",
      "Loads a special program to take care of the execution","None of the mentioned"],
      ["Those whose ‘read’ bit is set to ‘h’","Permitted for (can be accessed) only superusers",
      "Files that begin with a ‘.’","Files that cannot be opened by ordinary user for writing"],]

#answers=[1,2,1,1,2,4,3,4,3,1,4,1,4,3,1,3,3,4,1,2,3,2,4,2,1,3,2,2,2,3]
answers= [0,1,0,0,1,3,2,3,2,0,3,0,3,2,0,2,2,3,0,1,2,1,3,1,0,2,1,1,1,2]

user_answer = []

indexes=[]
ques = 1
#score=0
number = 0
end_value=900
#Progress_Bar[]


   

class Login:

   def __init__(self,root):

      self.root=root
      self.root.title(" Online Examination System")
      self.root.geometry("1200x700+100+50")
      self.root.resizable(False,False)
      self.loginform()
      
   def loginform(self):

      image1 = Image.open("C:\\Users\\NIDHI KUSHWAHA\\Documents\\image4_background.jpg")
      image1 = image1.resize((1200, 700), Image.ANTIALIAS)
      self.bg=ImageTk.PhotoImage(image1)
      self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0)

      frame_input=Frame(self.root,bg='white')
      frame_input.place(x=380,y=70,height=500,width=450)

      label1=Label(frame_input,text=" Login Details Here",font=('Goudy old style',40,'bold'),fg='blue',bg="white")
      LabelFrame=Label(frame_input,text="Student's Login Area",font=('Goudy old style',20),fg='blue',bg="white")
      label1.grid()
      LabelFrame.grid()
      
      label2=Label(frame_input,text="USERNAME",font=('Goudy old style',16,'bold'),fg='BLACK',bg="white")
      label2.place(x=40,y=170)

      self.username=Entry(frame_input,font=('Times new roman',12),bg="light grey",bd=0)
      self.username.place(x=40,y=200,height=30,width=350)

      label3=Label(frame_input,text="PASSWORD",font=('Goudy old style',16,'bold'),fg='BLACK',bg="white")
      label3.place(x=40,y=260)

      self.password=Entry(frame_input,font=('Times new roman',12),bg="light grey",bd=0)
      self.password.place(x=40,y=290,height=30,width=350)
    
      btn2=Button(frame_input,command=self.login,text="Login",cursor='hand2',font=('Goudy old style',20,'bold'),fg='white',bg="blue",bd=0)
      btn2.place(x=140,y=370,height=40,width=170)        

      btn3=Button(frame_input,command=self.Register,text="Not Registered ? Register",cursor='hand2',font=('Goudy old style',15,'bold'),fg='blue',bg="white",bd=0)
      btn3.place(x=120,y=430,height=30,width=230)


   def login(self):

      if self.username.get()=="" or self.password.get()=="":
         messagebox.showerror("Error","All fields are required",parent=self.root)

      else:
         try:
            con=pymysql.connect(host='localhost',user='root',password='sqlserver',database='logindatabase')
            cur=con.cursor()
            cur.execute('select * from register where username=%s and password=%s',(self.username.get(),self.password.get()))
            row=cur.fetchone()

            if row==None:
               messagebox.showerror('Error','Invalid Username And Password',parent=self.root)
               self.loginclear()
               self.username.focus()

            else:
               self.appscreen()
               #self.startispressed()
               con.close()

         except Exception as es:
            messagebox.showerror('Error',f'Error Due to : {str(es)}',parent=self.root)

            

   def Register(self):

     
      image2 = Image.open("C:\\Users\\NIDHI KUSHWAHA\\Documents\\image4_background.jpg")
      image2 = image2.resize((1200, 700), Image.ANTIALIAS)
      self.bg2=ImageTk.PhotoImage(image2)
      self.bg_image2=Label(self.root,image=self.bg2).place(x=0,y=0)

      
      frame_input2=Frame(self.root,bg='white')
      frame_input2.place(x=150,y=70,height=500,width=900)

      label1=Label(frame_input2,text="Register Here !",font=('Goudy old style',40,'bold'),fg='blue',bg="white")
      label1.place(x=280,y=20)

      label2=Label(frame_input2,text="USERNAME",font=("Goudy old style",15,"bold"),fg='black',bg='white')
      label2.place(x=120,y=120)

      self.entry=Entry(frame_input2,font=("times new roman",15,"bold"), bg='light grey',bd=0)
      self.entry.place(x=60,y=160,width=320,height=35)

      label3=Label(frame_input2,text="PASSWORD",font=("Goudy old style",15,"bold"),fg='black',bg='white')
      label3.place(x=120,y=210)

      self.entry2=Entry(frame_input2,font=("times new roman",15,"bold"),bg='light grey',bd=0)
      self.entry2.place(x=60,y=250,width=320,height=35)

      label4=Label(frame_input2,text="EMAIL-ID",font=("Goudy old style",15,"bold"),fg='black',bg='white')
      label4.place(x=600,y=120)

      self.entry3=Entry(frame_input2,font=("times new roman",15,"bold"),bg='light grey',bd=0)
      self.entry3.place(x=480,y=160,width=320,height=35)

      label5=Label(frame_input2,text="CONFIRM PASSWORD",font=("Goudy old style",15,"bold"),fg='black',bg='white')
      label5.place(x=560,y=210)

      self.entry4=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray',bd=0)
      self.entry4.place(x=480,y=250,width=320,height=35)

      btn2=Button(frame_input2,command=self.register,text="Register" ,cursor="hand2",font=("Goudy old style",20,"bold"),fg="white", bg="blue",bd=0,width=12,height=1)
      btn2.place(x=330,y=360)

      btn3=Button(frame_input2,command=self.loginform,text="Already Registered ? Login",cursor="hand2",font=("Goudy old style",18,"bold"),bg='white',fg="blue",bd=0)
      btn3.place(x=300,y=425)

   def register(self):

      if self.entry.get()==""or self.entry2.get()==""or self.entry3.get()==""or self.entry4.get()=="":

         messagebox.showerror("Error","All Fields Are Required",parent=self.root)

      elif self.entry2.get()!=self.entry4.get():

         messagebox.showerror("Error","Password and Confirm Password Should Be Same",parent=self.root)

      else:

         try:
            con=pymysql.connect(host="localhost",user="root",password="sqlserver",database="logindatabase")
            cur=con.cursor()
            cur.execute("select * from register where emailid=%s",self.entry3.get())
            row=cur.fetchone()

            if row!=None:

               messagebox.showerror("Error","User already Exist,Please try with another Email",parent=self.root)
               self.regclear()
               self.entry.focus()

            else:

               cur.execute("insert into register values(%s,%s,%s,%s)",(self.entry.get(),self.entry3.get(),self.entry2.get(),self.entry4.get()))
               con.commit()
               con.close()

               messagebox.showinfo("Success","Register Succesfull",parent=self.root)
               self.regclear()

         except Exception as es:

            messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)

   


   def appscreen(self):

      Frame_login=Frame(self.root,bg="white")
      Frame_login.place(x=0,y=0,height=700,width=1200)

      labelhello=Label(Frame_login,text="Hello " + self.username.get()+ " ! Get ready for the Exam ",font=('Goudy old style',35,'bold'),fg="blue",bg='white')
      labelhello.place(x=230,y=100)

      labelread=Label(Frame_login,text="Read the instructions carefully!",font=('Goudy old style',22,'bold'),fg="blue",bg='white')
      labelread.place(x=400,y=200)

      labelclick=Label(Frame_login,text="Click on the start button once you are ready",font=('Goudy old style',22,'bold'),fg="blue",bg='white')
      labelclick.place(x=330,y=240)

     
      btnlogout=Button(Frame_login,text="Logout",command=self.loginform,cursor="hand2",font=("times new roman",18,'bold'),fg="white",bg="red",bd=0,width=12,height=1)
      btnlogout.place(x=1000,y=15)

      btnstart=Button(Frame_login,text="START",command=self.startispressed,cursor="hand2",font=("times new roman",18,'bold'),fg="white",bg="green",bd=0,width=12,height=1)
      btnstart.place(x=480,y=350)

      Frame_logindown=Frame(self.root,bg="blue")
      Frame_logindown.place(x=0,y=500,height=200,width=1200)
      
      labelinst=Label(Frame_logindown,text="INSTRUCTIONS !",font=('Goudy old style',22,'bold'),fg="white",bg='blue')
      labelinst.place(x=470,y=10)

      labelinst1=Label(Frame_logindown,text=" 1.) This examination will contain 30 questions in total.",font=('Goudy old style',15,'bold'),fg="white",bg='blue')
      labelinst1.place(x=25,y=50)

      labelinst2=Label(Frame_logindown,text=" 2.) There will be a timing limit of 15 minutes to complete the examination.It is compulsory to answer all the questions"
      ,font=('Goudy old style',15,'bold'),fg="white",bg='blue')
      labelinst2.place(x=25,y=90)

      labelinst3=Label(Frame_logindown,text=" 3.) Each question will carry 1 mark . There will be  NO NEGATIVE  marking."
      ,font=('Goudy old style',15,'bold'),fg="white",bg='blue')
      labelinst3.place(x=25,y=130)

      labelinst4=Label(Frame_logindown,text=" 4.) Once you select a radio button that will be a final choice."
      ,font=('Goudy old style',15,'bold'),fg="white",bg='blue')
      labelinst4.place(x=25,y=170)

   def gen(self):
      global indexes
      while(len(indexes) < 30):
         x=random.randint(0,29)
         if x in indexes:
            continue
         else:
            indexes.append(x)
      #print (indexes) 

   def amount(self,number):
      global Progress_Bar
      Progress_Bar["value"]=number


   def showresult(self,score):
      #global Frame_start

      lblques.destroy()
      r1.destroy()
      r2.destroy()
      r3.destroy()
      r4.destroy()

      Frame_result=Frame(self.root,bg="white")
      Frame_result.place(x=0,y=0,height=700,width=1200)
      
      
      lblimage=Label(Frame_result,bg="white",border=0)
      lblimage.place(x=350,y=170)

      #lblimage1=Label(Frame_start,bg="white",border=0)
      #lblimage1.pack(pady=30)


      labelresulttext=Label(Frame_result,font=('Goudy old style',38,'bold'),fg="red",bg='white')
      labelresulttext.place(x=110,y=450)

      #labelresulttext1=Label(Frame_start,font=('Goudy old style',38,'bold'),fg="red",bg='white')
      #labelresulttext1.pack(pady=30)


      if score >= 25:

         lblscore=Label(Frame_result,text="HEY ! " + self.username.get()+ " HERE IS YOUR SCORE BOARD ",font=('Goudy old style',35,'bold'),fg="white",bg='red')
         lblscore.place(x=0,y=0,height=150,width=1200)
 
         img1 = Image.open("great2.jpg")
         img1 = img1.resize((550, 220), Image.ANTIALIAS)
         self.imggreat=ImageTk.PhotoImage(img1)
         lblimage.configure(image=self.imggreat)
         lblimage.image=self.imggreat
         #labelresulttext.configure(text=" YOU SCORED " +str(score)+ " OUT OF 30 ! \n \n  YOU ARE EXCELLENT!")
         labelresulttext=Label(Frame_result,text=" YOU SCORED " +str(score)+ " OUT OF 30 ! \n \n  YOU ARE EXCELLENT!",font=('Goudy old style',38,'bold'),fg="red",bg='white')
         labelresulttext.place(x=250,y=450)

      
      elif( score>=15 and score<25):
         lblscore=Label(Frame_result,text="HEY ! " + self.username.get()+ " HERE IS YOUR SCORE BOARD ",font=('Goudy old style',35,'bold'),fg="white",bg='red')
         lblscore.place(x=0,y=0,height=150,width=1200)
 
         img2 = Image.open("good1.jpg")
         img2 = img2.resize((400, 210), Image.ANTIALIAS)
         self.imggood=ImageTk.PhotoImage(img2)
         lblimage.configure(image=self.imggood)
         lblimage.image=self.imggood
         #labelresulttext.configure(text=" YOU SCORED " +str(score)+ " OUT OF 30 ! \n \n  YOU CAN DO BETTER !")
         labelresulttext=Label(Frame_result,text="YOU SCORED " +str(score)+ " OUT OF 30 ! \n \n GOOD , YOU CAN DO BETTER !",font=('Goudy old style',38,'bold'),fg="red",bg='white')
         labelresulttext.place(x=180,y=450)

      else:
         lblscore=Label(Frame_result,text="HEY ! " + self.username.get()+ " HERE IS YOUR SCORE BOARD ",font=('Goudy old style',35,'bold'),fg="white",bg='red')
         lblscore.place(x=0,y=0,height=150,width=1200)
 
         img3 = Image.open("bad1.jpg")
         img3 = img3.resize((500, 300), Image.ANTIALIAS)
         self.imgbad=ImageTk.PhotoImage(img3)
         lblimage.configure(image=self.imgbad)
         lblimage.image=self.imgbad
         #labelresulttext.configure(text=" YOU SCORED " +str(score)+ " OUT OF 30 ! \n \n  YOU REALLY NEED IMPROVEMENT !")
         labelresulttext=Label(Frame_result,text=" YOU SCORED " +str(score)+ " OUT OF 30 ! \n \n  YOU REALLY NEED IMPROVEMENT !",font=('Goudy old style',38,'bold'),fg="red",bg='white')
         labelresulttext.place(x=130,y=460)



   def calc(self):
      global indexes,user_answer,answers
      x=0
      score = 0
      for i in indexes:
         if user_answer[x] == answers[i]:
            score=score+1
         x += 1
      print (score)
      self.showresult(score)      



   def selected(self):
      global radiovar,user_answer,ques,number,Frame_start
      global lblques,r1,r2,r3,r4
      x= radiovar.get()
      user_answer.append(x)
      radiovar.set(-1)
      #print(x)
      #user_answer.append()
      if ques < 30:
         
         lblques.config(text=question[indexes[ques]])
         r1['text']=answers_choice[indexes[ques]][0]
         r2['text']=answers_choice[indexes[ques]][1]
         r3['text']=answers_choice[indexes[ques]][2]
         r4['text']=answers_choice[indexes[ques]][3]
         ques +=1

      else:
         print(indexes)
         print(user_answer)
         Progress_Bar.destroy()
         #self.hideprogressbar()
         #Frame_start.destroy()
         self.calc()

         

   def progressshow(self):
      global number,Progress_Bar
      def amount():
         
         Progress_Bar["value"]=number

      Progress_Bar=tkrtk.Progressbar(Frame_start ,orient="horizontal",length=1000,mode="determinate")
      Progress_Bar.pack(side="bottom",pady=40)
      Progress_Bar["value"]=number
      Progress_Bar["maximum"]=end_value

      for i in range(1,901):
         number=number+1
         print(str(number*10)+"%")
         Progress_Bar.after(1000,amount())
         Progress_Bar.update()
      Progress_Bar.pack_forget() 
      #self.calc()
      #btnforward=Button(Frame_start,text="forward",command=self.calc,cursor="hand2",font=("times new roman",18,'bold'),fg="white",bg="green",bd=0,width=12,height=1)
      #btnforward.pack()

            
               

   def startquiz(self):
   
      global Frame_start,lblques,r1,r2,r3,r4

      lblscore=Label(Frame_start,text=" Timer : 15 mins",font=('Goudy old style',20,'bold'),fg="white",bg='blue')
      lblscore.place(x=0,y=600,height=150,width=1200)
 
         
      lblques=Label(Frame_start,text= question[indexes[0]]
      ,font=('Goudy old style',23,'bold'),fg="black",bg='white')
      lblques.place(x=90,y=60)
      
      global radiovar
      radiovar= IntVar()
      radiovar.set(-1)

      r1=Radiobutton(Frame_start,text=answers_choice[indexes[0]][0],font=('Goudy old style',20,'bold'),fg="black",bg='white',value=0,
      variable=radiovar,command=self.selected)
      r1.place(x=90,y=150)

      r2=Radiobutton(Frame_start,text=answers_choice[indexes[0]][1],font=('Goudy old style',20,'bold'),fg="black",bg='white',
      value=1,variable=radiovar,command=self.selected)
      r2.place(x=90,y=200)

      r3=Radiobutton(Frame_start,text=answers_choice[indexes[0]][2],font=('Goudy old style',20,'bold'),fg="black",bg='white',
      value=2,variable=radiovar,command=self.selected)
      r3.place(x=90,y=250)

      r4=Radiobutton(Frame_start,text=answers_choice[indexes[0]][3],font=('Goudy old style',20,'bold'),fg="black",bg='white',
      value=3,variable=radiovar,command=self.selected)
      r4.place(x=90,y=300)

      threading.Thread(self.progressshow())
      


      
   def startispressed(self):
      global Frame_start

      Frame_start=Frame(self.root,bg="white")
      Frame_start.place(x=0,y=0,height=700,width=1200)
      
      
      self.gen()
      self.startquiz()


   def regclear(self):

      self.entry.delete(0,END)
      self.entry2.delete(0,END)
      self.entry3.delete(0,END)
      self.entry4.delete(0,END)


   def loginclear(self):

      self.email_txt.delete(0,END)
      self.password.delete(0,END)

   

root=Tk()
ob=Login(root)
root.mainloop()

 