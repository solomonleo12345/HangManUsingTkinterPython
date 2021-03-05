def hangman():
    global ss,ll,ss1,n,ffdata,temps,first
    first = inpp.get().lower()
    input1.delete(0,END)
    if(n>0):
        if(first in ss):
            for i in range(ss1):
                if(ss[i] == first and ll[i] == '*'):
                    ll.pop(i)
                    ll.insert(i,ss[i])
                    xx = ''.join(ll)
                    ss = list(ss)
                    ss.pop(i)
                    ss.insert(i,"*")
                    wordlabel.configure(text=xx)
                    if(xx==temps):
                        ans.configure(text='Congratulations You won The game......')
                        res = messagebox.askyesno("Notification",'Congratulations You won The game......\n want to play again ?')
                        if(res==True):
                            chooseword()
                        else:
                            root.destroy()
                    else:
                        break
        else:
            n -= 1
            leftchances.configure(text='Left = {}'.format(n))
    if(n<=0):
        ans.configure(text='OOps You Loss The game......')
        res = messagebox.askyesno("Notification", 'OOps You Loss The game......\n want to play again ?')
        if (res == True):
            chooseword()
        else:
            root.destroy()


def jj(event):
    hangman()

#tkinter imported
from tkinter import *
# messagebox imported
from tkinter import messagebox
# random imported
import random
from PIL import Image, ImageTk
# our wordlist
worldlist = ['mumbai','pune','delhi','bangaluru','kolkata','chennai','jaipur']
# creating a window
root = Tk()
im = Image.open('MatrixPic.png')
tkimage = ImageTk.PhotoImage(im)
myvar=Label(root,image = tkimage)
myvar.place(x=0, y=0, relwidth=1, relheight=1)
root.geometry('800x500')
root.minsize(width=800, height=500)
root.maxsize(width=800, height=500)

root.title('Hangman Game')

#---------------------------------------------------------------------------  Labels
introlabel = Label(root,text='Welcome to Hangman Game',font=('charlesworth',20,'bold'),bg='chartreuse4', relief="groove",
                   borderwidth=10)
introlabel.pack()
introlabel1 = Label(root,text='A random Indian metro City is generated, try to guess it',
                    font=('charlesworth',20,'bold'),bg='chartreuse4', relief="groove",
                   borderwidth=10)
introlabel1.pack(pady=10)

wordlabel = Label(root,text='',font=('arial',40,'bold'),bg='chartreuse4', relief="groove", borderwidth=10)
wordlabel.pack(pady=50)

leftchances = Label(root,text='',font=('arial',25,'bold'),bg='chartreuse4', relief="groove", borderwidth=10)
leftchances.place(x=650,y=120)

ans = Label(root,text='',font=('arial',25,'bold'),bg='chartreuse4', relief="groove", borderwidth=10)
ans.place(x=100,y=440)

#---------------------------------------------------------------------------- Entry Box

inpp = StringVar()
input1 = Entry(root,font=('arial',25,'bold'),relief='groove',bd=5,bg='chartreuse4',justify='center',borderwidth=10, fg='white',textvariable=inpp)
input1.focus_set()
input1.place(x=210,y=270)
#------------------------------------------------------------------------------------- Button
bt1 = Button(root,text='Submit',font=('arial',15,'bold'),width=15,bd=5,bg='chartreuse4',activebackground='olivedrab1'
             ,activeforeground='white',command=hangman)
bt1.place(x=300,y=350)
root.bind("<Return>",jj)
#------------------------------------------------------- World Select Function
def chooseword():
    global ss,ll,ss1,n,ffdata,temps
    ss = random.choice(worldlist)
    ll = ["*" for i in ss]
    ss1 = len(ss)
    n = ss1
    temps = ss
    leftchances.configure(text='Left = {}'.format(n))
    ffdata = ''
    for i in ll:
        ffdata += i+' '
    wordlabel.configure(text=ffdata)
    ans.configure(text='')


chooseword()
root.mainloop()