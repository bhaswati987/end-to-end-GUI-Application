#!/usr/bin/env python
# coding: utf-8

# In[15]:


from tkinter import * 
from tkinter import ttk 
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3
 
w1=Tk() 
w1.title("QUIZZIT") 
w1.configure(background="dim gray") 
w1.geometry("380x310") 
 
#importing images 
 
nq=Image.open("quizzit.jpeg") 
nqr=nq.resize((350,200),Image.ANTIALIAS) 
quizzit=ImageTk.PhotoImage(nqr) 
ns=Image.open("student.jpeg") 
nsr=ns.resize((160,70),Image.ANTIALIAS) 
student=ImageTk.PhotoImage(nsr) 
nt=Image.open("teacher.jpeg") 
ntr=nt.resize((170,70),Image.ANTIALIAS) 
teacher=ImageTk.PhotoImage(ntr)
global ami
nc=Image.open("add1.jpeg")
ncr=nc.resize((350,200),Image.ANTIALIAS)
ami=ImageTk.PhotoImage(ncr)
 
def win_teacher(): 
    t1=Toplevel(w1) 
    t1.title("TEACHER LOGIN") 
    t1.configure(background="dim gray") 
    t1.geometry("380x400") 

    def add_result():
        t2=Toplevel(t1) 
        t2.title("ADD QUES/SEE RESULTS") 
        t2.configure(background="dim gray") 
        t2.geometry("380x400") 
        nq=Image.open("add1.jpeg") 
        nqr=nq.resize((350,200),Image.ANTIALIAS) 
        add=ImageTk.PhotoImage(nqr) 
 
        l111=Label(t2,image=add)
        
 
        
        def ques_add():
            
            if e6.get()!= str(4) :
                messagebox.showinfo("ERROR!!!","Enter 4 in No. of options")
            else:
                
                t3=Toplevel(t2)  
                t3.title("Please add your questions")  
                t3.configure(background="dim gray")  
                t3.geometry("200x400")
           
            
            
                def go():
                    t5=Toplevel(t3) 
                    t5.geometry("270x140") 
                    t5.configure(background="dim gray") 
                    t5.title("Question status")
                    Tablename=e5.get() 
                    db=sqlite3.connect('QuestionSet.db')  
                    cursor=db.cursor() 
                    cursor.execute(f"SELECT COUNT(QuesNo) FROM [{Tablename}] ") 
                    x=cursor.fetchone() 
                    db.commit() 
                    db.close 
                    def teacher_exit(): 
                        t5.destroy() 
                        t3.destroy() 
                        t2.destroy() 
                        t1.destroy() 
                        w1.destroy() 
                    def create_new(): 
                        t5.destroy() 
                        t3.destroy() 
                        e5.delete(0,END) 
                        e6.delete(0,END) 
                    l151=Label(t5,text= e5.get()+ " Question set created with "+ str(x[0]) + " Questions") 
                    l151.place(x=20,y=20) 
                    bt4=Button(t5,text="EXIT!",height=2,width=7,bg= "pale green",fg="dim gray",command=teacher_exit) 
                    bt4.place(x=40,y=80) 
                    bt5=Button(t5,text="CREATE NEW!",height=2,width=11,bg= "pale green",fg="dim gray",command=create_new) 
                    bt5.place(x=150,y=80) 
                    t5.mainloop() 
                def add(): 
                    global count 
                    count = count + 1 
                    t4=Toplevel(t3) 
                    t4.title("Question goes here") 
                    t4.geometry("260x450") 
                    t4.configure(background="dim gray") 
                    def done():
                        Tablename=e5.get() 
                        given=e7.get(1.0,END) 
                        option1 = e8.get() 
                        option2 = e9.get() 
                        option3 = e10.get() 
                        option4 = e11.get() 

                        corr_Ans=lst.get()
                         

                        db=sqlite3.connect('QuestionSet.db')  
                        cursor=db.cursor()  
                        cursor.execute(f"CREATE TABLE IF NOT EXISTS [{Tablename}](QuesNo INTEGER PRIMARY KEY AUTOINCREMENT,Question TEXT,optionA TEXT,optionB TEXT,optionC TEXT,optionD TEXT,Correct_Option TEXT)")   
                        cursor.execute(f"INSERT INTO [{Tablename}](Question,optionA,optionB,optionC,optionD,Correct_Option) VALUES('"+given+"','"+option1+"','"+option2+"','"+option3+"','"+option4+"','"+corr_Ans+"')")
                        db.commit()  
                        db.close() 
                        for i in range(1,count): 
                            l132=Label(t3,text="Question"+" "+str(i),font=20)  
                            l132.grid(row=i,column=1)  
                            t4.destroy() 
                    l131=Label(t4,text="QUESTION"+" "+str(count-1),font=20)  
                    l131.place(x=10,y=10)  
                    def click1(event): 
                        e8.configure(state=NORMAL) 
                        e8.delete(0,END) 
                    def click2(event):
                        e9.configure(state=NORMAL) 
                        e9.delete(0,END) 
                    def click3(event):
                        e10.configure(state=NORMAL) 
                        e10.delete(0,END)
                    def click4(event):
                        e11.configure(state=NORMAL) 
                        e11.delete(0,END)
                    def click5(event):
                        e12.configure(state=NORMAL) 
                        e12.delete(0,END) 
                    e7=Text(t4,height=11,width=33) 
                    e7.place(x=10,y=50) 
                    e8=Entry(t4) 
                    e8.insert(0,'option a') 
                    e8.config(state=DISABLED) 
                    e8.bind("<Button-1>",click1) 
                    e8.place(x=10,y=250) 
                    e9=Entry(t4) 
                    e9.insert(0,'option b') 
                    e9.config(state=DISABLED) 
                    e9.bind("<Button-1>",click2) 
                    e9.place(x=150,y=250) 
                    e10=Entry(t4) 
                    e10.insert(0,'option c') 
                    e10.config(state=DISABLED) 
                    e10.bind("<Button-1>",click3) 
                    e10.place(x=10,y=290) 
                    e11=Entry(t4) 
                    e11.insert(0,'option d') 
                    e11.config(state=DISABLED) 
                    e11.bind("<Button-1>",click4) 
                    e11.place(x=150,y=290) 
                    l133=Label(t4,text="Correct Answer",bg= "pale green",fg="dim gray")  
                    l133.place(x=10,y=350) 

                    options=["option a","option b","option c","option d"]
                    lst=StringVar(t4)
                    lst.set("Select correct option")
                    opt_menu=OptionMenu(t4,lst,*options)
                    opt_menu.place(x=130,y=350)
                    

                    bt2=Button(t4,text="DONE!",command=done,bg= "pale green",fg="dim gray")  
                    bt2.place(x=120,y=400) 



                l121=Label(t3,text=e5.get() ,font=30,bg= "pale green",fg="dim gray")  
                l121.grid(row=0,column=1)  
                 
                bt1=Button(t3,text="ADD",command=add,bg= "pale green",fg="dim gray")  
                bt1.grid(row=20,column=1) 
                bt3=Button(t3,text="GO",command=go,bg= "pale green",fg="dim gray")  
                bt3.grid(row=21,column=1)  
                
                t3.mainloop()
        
        l111=Label(t2,image=ami)
        l111.place(x=10,y=10) 
        l112=Label(t2,text="Subject Name",font= ('arial',14),bg= "dim gray",fg="gray1").place(x=10,y=220) 
        l113=Label(t2,text="No. of options",font= ('arial',14),bg= "dim gray",fg="gray1").place(x=10,y=250)
        global e5
        e5=Entry(t2)
        e5.place(x=210,y=225) 
        global e6
        e6=Entry(t2)
        e6.place(x=210,y=255)
        def student_result():
            t6=Toplevel(t2)
            Table=e5.get()
            l161=Label(t6,text="Serial No",font= ('arial',14),bg= "pale green",fg="dim gray").grid(row=0,column=1)
            l161=Label(t6,text="Name of Student",font= ('arial',12),bg= "pale green",fg="dim gray").grid(row=0,column=2)
            l161=Label(t6,text="Registration no",font= ('arial',12),bg= "pale green",fg="dim gray").grid(row=0,column=3)
            l161=Label(t6,text="Marks obtained",font= ('arial',12),bg= "pale green",fg="dim gray").grid(row=0,column=4)
            conn=sqlite3.connect('StudentScore.db')
            cursor=conn.cursor()
            cursor.execute(f"SELECT * FROM [{Table}]")
            r=cursor.fetchall()
            def tclose():
                t1.destroy()
                t2.destroy()
                t6.destroy()
                w1.destroy()
            def thome():
                t1.destroy()
                t2.destroy()
                t6.destroy()
            def tback():
                t6.destroy()
            def tlog():
                t2.destroy()
                t6.destroy()
            
            b162=Button(t6,text="CLOSE",command=tclose,height=4,width=17,bg= "pale green",fg="dim gray")
            b162.grid(row=20,column=4)
            b163=Button(t6,text="LOG IN",command=tlog,height=4,width=17,bg= "pale green",fg="dim gray")
            b163.grid(row=20,column=2)
            b164=Button(t6,text="HOME",command=thome,height=4,width=17,bg= "pale green",fg="dim gray")
            b164.grid(row=20,column=3)
            b165=Button(t6,text="BACK",command=tback,height=4,width=17,bg= "pale green",fg="dim gray")
            b165.grid(row=20,column=1)
            num=3
            for i in r:
                Ser=Label(t6,text=i[0])
                Ser.grid(row=num,column=1,padx=10,pady=10)
                stu=Label(t6,text=i[1])
                stu.grid(row=num,column=2,padx=10,pady=10)
                regs=Label(t6,text=i[2])
                regs.grid(row=num,column=3,padx=10,pady=10)
                mark=Label(t6,text=i[3])
                mark.grid(row=num,column=4,padx=10,pady=10)
                num+=1
            t6.mainloop()
        
        b112=Button(t2,text="ADD!",command=ques_add,height=4,width=17,bg= "pale green",fg="dim gray").place(x=30,y=320) 
        b113=Button(t2,text="RESULTS",height=4,width=18,bg= "pale green",fg="dim gray",command=student_result).place(x=220,y=320)


            
    nq1=Image.open("quizzit.jpeg") 
    nqr1=nq1.resize((350,200),Image.ANTIALIAS) 
    quizzit1=ImageTk.PhotoImage(nqr1) 
    l11=Label(t1,image=quizzit1)
    
    l11.place(x=10,y=10) 
    l12=Label(t1,text="USERNAME",font= ('arial',18),bg= "dim gray",fg="steel blue").place(x=10,y=220) 
    l13=Label(t1,text="PASSWORD",font= ('arial',18),bg= "dim gray",fg="steel blue").place(x=10,y=250) 
    e1=Entry(t1)
    e1.insert(0,"teacher123")
    e1.place(x=170,y=225)
    e2=Entry(t1)
    e2.insert(0,"pass123")
    e2.configure(show="*")
    e2.place(x=170,y=255)

    
    b12=Button(t1,text="LOGIN!",height=4,width=20,bg= "pale green",fg="dim gray",command=add_result).place(x=130,y=320) 
 
    t1.mainloop() 

def win_student(): 
    s1=Toplevel(w1) 
    s1.title("STUDENT LOGIN") 
    s1.configure(background="dim gray") 
    s1.geometry("380x400") 
    nq=Image.open("quizzit.jpeg") 
    nqr=nq.resize((350,200),Image.ANTIALIAS) 
    quizzit=ImageTk.PhotoImage(nqr)
    
    def win_s2():
        s2=Toplevel(s1)
        s2.title("Welcome") 
        s2.geometry("330x220") 
        s2.configure(bg="dim gray")
        def ready():
            s3=Toplevel(s2)   
            s3.configure(bg="dim gray")   
            subj=subject_list.get()   
            Subject=subj[2:len(subj)-3]  
            l221=Label(s3,text=Subject,font=20,bg= "pale green",fg="dim gray")  
            l221.grid(row=0,column=1)  
            db=sqlite3.connect('QuestionSet.db')     
            cursor=db.cursor()
            cursor.execute(f"SELECT QuesNo FROM [{Subject}]")   
            m=cursor.fetchall()  
            global d 
            d=[item for t in m for item in t] 
            def action(i):
                s4=Toplevel(s3) 
                conn=sqlite3.connect('QuestionSet.db')   
                cursor=conn.cursor()
                
                
                
                def check():
                    cursor.execute(f"SELECT Correct_Option FROM [{Subject}] where QuesNo=?",(d[k],))
                    z=cursor.fetchall()
                    c=[item for t in z for item in t]
                    cor_ans=c[0]
                    if v.get()==cor_ans:
                         marks()
                            
                def marks():
                    global score
                    score=score+1
                    
                   
                
                
                def score_stud():  
                    namestud=e3.get()  
                    reg=e4.get()
                    db=sqlite3.connect('StudentScore.db')  
                    cursor=db.cursor()  
                    cursor.execute(f"CREATE TABLE IF NOT EXISTS [{Subject}](Number INTEGER PRIMARY KEY AUTOINCREMENT,Name_Of_Student TEXT,Registration_no TEXT,Marks_obtained INTEGER)")   
                    cursor.execute(f"INSERT INTO [{Subject}](Name_Of_Student,Registration_no,Marks_obtained) VALUES('"+namestud+"','"+reg+"','"+str(score)+"')")
                    db.commit()  
                    s5=Toplevel(s3)
                    s5.configure(bg="dim gray")
                    
                    l251=Label(s5,text="Congratulations!!!"+e3.get()).place(x=10,y=10)
                    l252=Label(s5,text="You scored "+ str(score)+" out of " +str(len(d))).place(x=10,y=50)
                    def new_quiz():
                        e3.delete(0,END)
                        e4.delete(0,END)
                        s2.destroy()
                        s3.destroy()
                        s5.destroy()
                    def stud_exit():
                        s5.destroy()
                        s3.destroy()
                        s2.destroy()
                        s1.destroy()
                        w1.destroy()
                        
                    b251=Button(s5,text="START NEW QUIZ",command=new_quiz,bg= "pale green",fg="dim gray").place(x=10,y=150)
                    b252=Button(s5,text="Exit",command=stud_exit,bg= "pale green",fg="dim gray").place(x=150,y=150)
                    db.close() 
                    s5.mainloop()
                b220=Button(s3,text="GO",bg= "pale green",fg="dim gray",command=score_stud).grid(row=11,column=1) 
                        
                        
                       
                for j in range(len(d)):
                    quest="Question"+str(d[j])
                    if btns[i].cget('text') == quest:
                        global cnt
                        cnt = cnt + 1
                        for k in range(j,cnt):
                            cursor.execute(f"SELECT * FROM [{Subject}] where QuesNo=?",(d[k],))
                            z=cursor.fetchall()
                            c=[item for t in z for item in t]
                            l231=Label(s4,text=c[0]).grid(row=1,column=1) 
                            l232=Label(s4,text=c[1]).grid(row=1,column=2)
                            v=StringVar(value="x")
                            
                            b233=Radiobutton(s4,text=c[2],variable=v,value='option a',command=lambda:check())
                            b233.grid(row=3,column=2)
                            b234=Radiobutton(s4,text=c[3],variable=v,value='option b',command=lambda:check())
                            b234.grid(row=4,column=2)
                            b235=Radiobutton(s4,text=c[4],variable=v,value='option c',command=lambda:check())
                            b235.grid(row=5,column=2)
                            b236=Radiobutton(s4,text=c[5],variable=v,value='option d',command=lambda:check())
                            
                            b236.grid(row=6,column=2)
                            break
                        
                        def done():
                            btns[i].configure(bg="sandy brown")
                            s4.destroy()
                        b237=Button(s4,text="Done",command=done).grid(row=7,column=2)
                        
               
            btn_nr = -1
            btns = []

            for x in range(len(d)):
                for y in range(len(d)):
                    btn_nr += 1
                    btns.append(Button(s3,text="Question"+str(d[x]), command=lambda x=btn_nr: action(x)))
                    btns[btn_nr].grid(row=x+1, column=1)
            
                    
            
    
        
        cnt=0
        l211=Label(s2,text="WELCOME! "+e3.get(),font= ('arial',17,'bold'),bg= "pale green",fg="dim gray")
        l211.place(x=10,y=10) 
        conn=sqlite3.connect('QuestionSet.db') 
        cursor=conn.cursor() 
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'") 
        lst=cursor.fetchall() 
        subject_list=StringVar() 
        subject_list.set("Select a subject") 
        menu=OptionMenu(s2,subject_list,*lst) 
        menu.place(x=100,y=100)   
        b211=Button(s2,text="READY",bg= "pale green",fg="dim gray",command=ready).place(x=150,y=170)   
        
        
 
    l21=Label(s1,image=quizzit)
    
    l21.place(x=10,y=10) 
    l22=Label(s1,text="Enter Name",font= ('arial',14),bg= "dim gray",fg="gray1").place(x=10,y=220) 
    l23=Label(s1,text="Enter Registration no.",font= ('arial',14),bg= "dim gray",fg="gray1").place(x=10,y=250) 
    e3=Entry(s1)
    e3.place(x=210,y=225) 
    e4=Entry(s1)
    e4.place(x=210,y=255) 
    b22=Button(s1,text="START",command=win_s2,height=4,width=20,bg= "pale green",fg="dim gray").place(x=130,y=320) 
 
    s1.mainloop() 
     
l1=Label(w1,image=quizzit) 

l1.place(x=10,y=10) 
count=1 
cnt=1
score=0
b1=Button(w1,image=student,command=win_student).place(x=10,y=220) 
b2=Button(w1,image=teacher,command=win_teacher).place(x=190,y=220) 

 
w1.mainloop()


# In[ ]:




