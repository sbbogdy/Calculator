from tkinter import *
from PIL import Image,ImageTk
from calc import *
from tkinter import ttk
from ttkthemes import ThemedStyle
import sys


try:

    import Tkinter as tk

except ImportError:

    import tkinter as tk


try:

    import ttk

    py3 = False
except ImportError:

    import tkinter.ttk as ttk

    py3 = True

#import unknown_support


def vp_start_gui():





    global val, w, root

    root = tk.Tk()

    top = Toplevel1(root)

    #unknown_support.init(root, top)
    root.mainloop()
w = None



def create_Toplevel1(rt, *args, **kwargs):





    global w, w_win, root

    root = rt

    w = tk.Toplevel(root)

    style = ThemedStyle(w)
    style.set_theme("scidgrey")

    top = Toplevel1(w)

    #unknown_support.init(w, top, *args, **kwargs)

    return (w, top)



def destroy_Toplevel1():

    global w

    w.destroy()

    w = None



class Toplevel1:


    def __init__(self, top=None):



        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'

        _fgcolor = '#000000'  # X11 color: 'black'

        _compcolor = '#d9d9d9'  # X11 color: 'gray85'

        _ana1color = '#d9d9d9'  # X11 color: 'gray85'

        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        top.geometry("600x800+252+87")

        top.resizable(0, 0)

        top.title("Calculator")
        #bg = ImageTk.PhotoImage(Image.open("background.png"))
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")

        top.configure(highlightcolor="black")


        self.Font_tuple = ("Comic Sans MS", 13, "bold")


        #self.background_label = Label(top, image=bg)
        #self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        #self.w = Label(root, image=bg)
        #self.w.pack()
        self.list=[]
        self.Canvas1 = tk.Canvas(top)

        self.Canvas1.place(relx=0, rely=0, relheight=1, relwidth = 1)

        self.Canvas1.configure(background="#000000")

        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")

        self.Canvas1.configure(highlightcolor="black")

        self.Canvas1.configure(insertbackground="black")

        self.Canvas1.configure(relief="ridge")

        self.Canvas1.configure(selectbackground="blue")

        self.Canvas1.configure(selectforeground="white")

        self.Bequal = tk.Button(self.Canvas1)

        self.Bequal.place(relx=0.8, rely=0.85, relheight=0.075, relwidth=0.1)

        self.Bequal.configure(activebackground="#ececec")

        self.Bequal.configure(activeforeground="#000000")

        self.Bequal.configure(background="#df9953")

        self.Bequal.configure(disabledforeground="#d5b771")

        self.Bequal.configure(foreground="#000000")

        self.Bequal.configure(highlightbackground="#d9d9d9")

        self.Bequal.configure(highlightcolor="black")

        self.Bequal.configure(pady="0")

        self.Bequal.configure(text='''=''', font=self.Font_tuple)

        self.Bequal.configure(command=lambda:self.result())

        self.B1 = tk.Button(self.Canvas1)

        self.B1.place(relx=0.35, rely=0.45, relheight=0.075, relwidth=0.1)

        self.B1.configure(activebackground="#ececec")

        self.B1.configure(activeforeground="#000000")

        self.B1.configure(background="#d9d9d9")

        self.B1.configure(disabledforeground="#a3a3a3")

        self.B1.configure(foreground="#000000")
        self.B1.configure(highlightbackground="#d9d9d9")

        self.B1.configure(highlightcolor="black")

        self.B1.configure(pady="0")

        self.B1.configure(text='''1''', font=self.Font_tuple)

        self.B1.configure(command=lambda:(self.listappend('1')))

        self.B2 = tk.Button(self.Canvas1)

        self.B2.place(relx=0.5, rely=0.45, relheight=0.075, relwidth=0.1)

        self.B2.configure(activebackground="#ececec")

        self.B2.configure(activeforeground="#000000")

        self.B2.configure(background="#d9d9d9")

        self.B2.configure(disabledforeground="#a3a3a3")

        self.B2.configure(foreground="#000000")

        self.B2.configure(highlightbackground="#d9d9d9")

        self.B2.configure(highlightcolor="black")

        self.B2.configure(pady="0")

        self.B2.configure(text='''2''', font=self.Font_tuple)
        self.B2.configure(command=lambda: (self.listappend('2')))

        self.B3 = tk.Button(self.Canvas1)

        self.B3.place(relx=0.65, rely=0.45, relheight=0.075, relwidth=0.1)

        self.B3.configure(activebackground="#ececec")

        self.B3.configure(activeforeground="#000000")

        self.B3.configure(background="#d9d9d9")

        self.B3.configure(disabledforeground="#a3a3a3")

        self.B3.configure(foreground="#000000")

        self.B3.configure(highlightbackground="#d9d9d9")
        self.B3.configure(highlightcolor="black")

        self.B3.configure(pady="0")

        self.B3.configure(text='''3''', font=self.Font_tuple)
        self.B3.configure(command=lambda: (self.listappend('3')))
        self.B4 = tk.Button(self.Canvas1)

        self.B4.place(relx=0.35, rely=0.55, relheight=0.075, relwidth=0.1)

        self.B4.configure(activebackground="#ececec")

        self.B4.configure(activeforeground="#000000")

        self.B4.configure(background="#d9d9d9")

        self.B4.configure(disabledforeground="#a3a3a3")
        self.B4.configure(foreground="#000000")
        self.B4.configure(highlightbackground="#d9d9d9")

        self.B4.configure(highlightcolor="black")

        self.B4.configure(pady="0")

        self.B4.configure(text='''4''', font=self.Font_tuple)
        self.B4.configure(command=lambda: (self.listappend('4')))
        self.B5 = tk.Button(self.Canvas1)

        self.B5.place(relx=0.5, rely=0.55, relheight=0.075, relwidth=0.1)

        self.B5.configure(activebackground="#ececec")

        self.B5.configure(activeforeground="#000000")

        self.B5.configure(background="#d9d9d9")

        self.B5.configure(disabledforeground="#a3a3a3")

        self.B5.configure(foreground="#000000")

        self.B5.configure(highlightbackground="#d9d9d9")

        self.B5.configure(highlightcolor="black")

        self.B5.configure(pady="0")

        self.B5.configure(text='''5''', font=self.Font_tuple)
        self.B5.configure(command=lambda: (self.listappend('5')))
        self.B6 = tk.Button(self.Canvas1)

        self.B6.place(relx=0.65, rely=0.55, relheight=0.075, relwidth=0.1)

        self.B6.configure(activebackground="#ececec")

        self.B6.configure(activeforeground="#000000")

        self.B6.configure(background="#d9d9d9")

        self.B6.configure(disabledforeground="#a3a3a3")

        self.B6.configure(foreground="#000000")

        self.B6.configure(highlightbackground="#d9d9d9")

        self.B6.configure(highlightcolor="black")

        self.B6.configure(pady="0")

        self.B6.configure(text='''6''', font=self.Font_tuple)
        self.B6.configure(command=lambda: (self.listappend('6')))
        self.B7 = tk.Button(self.Canvas1)

        self.B7.place(relx=0.35, rely=0.65, relheight=0.075, relwidth=0.1)

        self.B7.configure(activebackground="#ececec")

        self.B7.configure(activeforeground="#000000")

        self.B7.configure(background="#d9d9d9")

        self.B7.configure(disabledforeground="#a3a3a3")

        self.B7.configure(foreground="#000000")

        self.B7.configure(highlightbackground="#d9d9d9")

        self.B7.configure(highlightcolor="black")

        self.B7.configure(pady="0")

        self.B7.configure(text='''7''', font=self.Font_tuple)
        self.B7.configure(command=lambda: (self.listappend('7')))
        self.B8 = tk.Button(self.Canvas1)

        self.B8.place(relx=0.5, rely=0.65, relheight=0.075, relwidth=0.1)

        self.B8.configure(activebackground="#ececec")

        self.B8.configure(activeforeground="#000000")

        self.B8.configure(background="#d9d9d9")

        self.B8.configure(disabledforeground="#a3a3a3")

        self.B8.configure(foreground="#000000")

        self.B8.configure(highlightbackground="#d9d9d9")

        self.B8.configure(highlightcolor="black")

        self.B8.configure(pady="0")

        self.B8.configure(text='''8''', font=self.Font_tuple)
        self.B8.configure(command=lambda: (self.listappend('8')))
        self.B9 = tk.Button(self.Canvas1)

        self.B9.place(relx=0.65, rely=0.65, relheight=0.075, relwidth=0.1)

        self.B9.configure(activebackground="#ececec")

        self.B9.configure(activeforeground="#000000")

        self.B9.configure(background="#d9d9d9")

        self.B9.configure(disabledforeground="#a3a3a3")

        self.B9.configure(foreground="#000000")

        self.B9.configure(highlightbackground="#d9d9d9")

        self.B9.configure(highlightcolor="black")

        self.B9.configure(pady="0")

        self.B9.configure(text='''9''', font=self.Font_tuple)
        self.B9.configure(command=lambda: (self.listappend('9')))
        self.B0 = tk.Button(self.Canvas1)

        self.B0.place(relx=0.5, rely=0.75, relheight=0.075, relwidth=0.1)

        self.B0.configure(activebackground="#ececec")

        self.B0.configure(activeforeground="#000000")

        self.B0.configure(background="#d9d9d9")

        self.B0.configure(disabledforeground="#a3a3a3")

        self.B0.configure(foreground="#000000")

        self.B0.configure(highlightbackground="#d9d9d9")

        self.B0.configure(highlightcolor="black")

        self.B0.configure(pady="0")

        self.B0.configure(text='''0''', font=self.Font_tuple)
        self.B0.configure(command=lambda: (self.listappend('0')))
        self.Bop = tk.Button(self.Canvas1)
        self.Bop.place(relx=0.35, rely=0.75, relheight=0.075, relwidth=0.1)

        self.Bop.configure(activebackground="#ececec")

        self.Bop.configure(activeforeground="#000000")

        self.Bop.configure(background="#d9d9d9")

        self.Bop.configure(disabledforeground="#a3a3a3")

        self.Bop.configure(foreground="#000000")

        self.Bop.configure(highlightbackground="#d9d9d9")

        self.Bop.configure(highlightcolor="black")

        self.Bop.configure(pady="0")

        self.Bop.configure(text='''(''', font=self.Font_tuple)
        self.Bop.configure(command=lambda: (self.listappend('(')))
        self.Bcl = tk.Button(self.Canvas1)
        self.Bcl.place(relx=0.65, rely=0.75, relheight=0.075, relwidth=0.1)

        self.Bcl.configure(activebackground="#ececec")

        self.Bcl.configure(activeforeground="#000000")

        self.Bcl.configure(background="#d9d9d9")

        self.Bcl.configure(disabledforeground="#a3a3a3")

        self.Bcl.configure(foreground="#000000")

        self.Bcl.configure(highlightbackground="#d9d9d9")

        self.Bcl.configure(highlightcolor="black")

        self.Bcl.configure(pady="0")

        self.Bcl.configure(text=''')''', font=self.Font_tuple)
        self.Bcl.configure(command=lambda: (self.listappend(')')))

        self.Bplus = tk.Button(self.Canvas1)

        self.Bplus.place(relx=0.8, rely=0.45, relheight=0.075, relwidth=0.1)

        self.Bplus.configure(activebackground="#ececec")

        self.Bplus.configure(activeforeground="#000000")

        self.Bplus.configure(background="#d9d9d9")

        self.Bplus.configure(disabledforeground="#a3a3a3")

        self.Bplus.configure(foreground="#000000")

        self.Bplus.configure(highlightbackground="#d9d9d9")

        self.Bplus.configure(highlightcolor="black")

        self.Bplus.configure(pady="0")

        self.Bplus.configure(text='''+''', font=self.Font_tuple)
        self.Bplus.configure(command=lambda: (self.listappend('+')))
        self.Bminus = tk.Button(self.Canvas1)

        self.Bminus.place(relx=0.8, rely=0.55, relheight=0.075, relwidth=0.1)

        self.Bminus.configure(activebackground="#ececec")

        self.Bminus.configure(activeforeground="#000000")

        self.Bminus.configure(background="#d9d9d9")

        self.Bminus.configure(disabledforeground="#a3a3a3")

        self.Bminus.configure(foreground="#000000")

        self.Bminus.configure(highlightbackground="#d9d9d9")

        self.Bminus.configure(highlightcolor="black")

        self.Bminus.configure(pady="0")

        self.Bminus.configure(text='''-''', font=self.Font_tuple)
        self.Bminus.configure(command=lambda: (self.listappend('-')))
        self.Bmult = tk.Button(self.Canvas1)

        self.Bmult.place(relx=0.8, rely=0.65, relheight=0.075, relwidth=0.1)

        self.Bmult.configure(activebackground="#ececec")

        self.Bmult.configure(activeforeground="#000000")

        self.Bmult.configure(background="#d9d9d9")

        self.Bmult.configure(disabledforeground="#a3a3a3")

        self.Bmult.configure(foreground="#000000")

        self.Bmult.configure(highlightbackground="#d9d9d9")

        self.Bmult.configure(highlightcolor="black")

        self.Bmult.configure(pady="0")

        self.Bmult.configure(text='''*''', font=self.Font_tuple)
        self.Bmult.configure(command=lambda: (self.listappend('*')))
        self.Bdiv = tk.Button(self.Canvas1)

        self.Bdiv.place(relx=0.8, rely=0.75, relheight=0.075, relwidth=0.1)

        self.Bdiv.configure(activebackground="#ececec")

        self.Bdiv.configure(activeforeground="#000000")

        self.Bdiv.configure(background="#d9d9d9")

        self.Bdiv.configure(disabledforeground="#a3a3a3")

        self.Bdiv.configure(foreground="#000000")

        self.Bdiv.configure(highlightbackground="#d9d9d9")

        self.Bdiv.configure(highlightcolor="black")

        self.Bdiv.configure(pady="0")

        self.Bdiv.configure(text='''/''', font=self.Font_tuple)
        self.Bdiv.configure(command=lambda: (self.listappend('/')))
        self.Bpow = tk.Button(self.Canvas1)

        self.Bpow.place(relx=0.65, rely=0.85, relheight=0.075, relwidth=0.1)

        self.Bpow.configure(activebackground="#ececec")

        self.Bpow.configure(activeforeground="#000000")

        self.Bpow.configure(background="#d9d9d9")

        self.Bpow.configure(disabledforeground="#a3a3a3")

        self.Bpow.configure(foreground="#000000")

        self.Bpow.configure(highlightbackground="#d9d9d9")

        self.Bpow.configure(highlightcolor="black")

        self.Bpow.configure(pady="0")

        self.Bpow.configure(text='''^''', font=self.Font_tuple)
        self.Bpow.configure(command=lambda: (self.listappend('^')))

        self.Bpoint = tk.Button(self.Canvas1)

        self.Bpoint.place(relx=0.5, rely=0.85, relheight=0.075, relwidth=0.1)

        self.Bpoint.configure(activebackground="#ececec")

        self.Bpoint.configure(activeforeground="#000000")

        self.Bpoint.configure(background="#d9d9d9")

        self.Bpoint.configure(disabledforeground="#a3a3a3")

        self.Bpoint.configure(foreground="#000000")

        self.Bpoint.configure(highlightbackground="#d9d9d9")

        self.Bpoint.configure(highlightcolor="black")

        self.Bpoint.configure(pady="0")

        self.Bpoint.configure(text='''.''', font=self.Font_tuple)
        self.Bpoint.configure(command=lambda: (self.listappend('.')))

        self.Canvas2 = tk.Canvas(self.Canvas1)

        self.Canvas2.place(relx=0.1, rely=0.11, relheight=0.25, relwidth = 0.8)

        self.Canvas2.configure(background="#ffffff")

        self.Canvas2.configure(borderwidth="2")

        self.Canvas2.configure(highlightbackground="#d9d9d9")

        self.Canvas2.configure(highlightcolor="black")

        self.Canvas2.configure(insertbackground="black")

        self.Canvas2.configure(relief="ridge")

        self.Canvas2.configure(selectbackground="blue")

        self.Canvas2.configure(selectforeground="white")

        self.Clear = tk.Button(self.Canvas1)

        self.Clear.place(relx=0.2, rely=0.45, relheight=0.075, relwidth=0.1)

        self.Clear.configure(activebackground="#ececec")

        self.Clear.configure(activeforeground="#000000")

        self.Clear.configure(background="#d9d9d9")

        self.Clear.configure(disabledforeground="#a3a3a3")

        self.Clear.configure(foreground="#000000")

        self.Clear.configure(highlightbackground="#d9d9d9")

        self.Clear.configure(highlightcolor="black")

        self.Clear.configure(pady="0")

        self.Clear.configure(text='''Clear''', font=self.Font_tuple)
        self.Clear.configure(command=lambda:self.clearList())

        self.Back = tk.Button(self.Canvas1)

        self.Back.place(relx=0.2, rely=0.55, relheight=0.075, relwidth=0.1)

        self.Back.configure(activebackground="#ececec")

        self.Back.configure(activeforeground="#000000")

        self.Back.configure(background="#d9d9d9")

        self.Back.configure(disabledforeground="#a3a3a3")

        self.Back.configure(foreground="#000000")

        self.Back.configure(highlightbackground="#d9d9d9")

        self.Back.configure(highlightcolor="black")

        self.Back.configure(pady="0")

        self.Back.configure(text='''Back''', font=self.Font_tuple)
        self.Back.configure(command=lambda:(self.Canvas2.delete('result'),self.list.pop(-1),self.printList()))

    def listappend(self, m):
        if len(self.list) < 25:
            self.list.append(m)
        self.printList()

    def printList(self):
        self.Canvas2.delete('text')
        self.Canvas2.delete('result')
        g=""
        for i in self.list:
            g+=i
        self.Canvas2.create_text(440,150,text=g,tag='text', font=("Comic Sans MS", 20, "bold"), anchor ="e")

    def clearList(self):
        self.Canvas2.delete('text')
        self.Canvas2.delete('result')
        self.list.clear()

    def printResult(self,m):
        self.Canvas2.delete('text')
        self.Canvas2.delete('result')
        g=str(m)
        self.Canvas2.create_text(440, 80, text=g, tag='result', font=("Comic Sans MS", 20, "bold"), anchor ="e")
        self.list.clear()


    def result(self):
        postv = []
        stiva = []
        stivaval = []
        sirsemn = []
        paran = [0] * 100
        c = 0
        nr = -1
        ok = 0
        ok1 = 0
        zec = 1
        v = self.list
        if len(v) == 1 and v[0] in "-+":
            self.printResult("ERROR")
            return "ERROR"
        for i in range(len(v)):
            if v[i].isdigit():
                for j in range(c+1):
                    paran[j] = 0
            elif v[i] == '(':
                if v[i-1].isdigit() and i != 0:
                    stiva.append('*')
                    stivaval.append(Application.calcval(self, c, '*'))
                c += 1
                paran[c] = 1
            elif v[i] == ')':
                c -= 1
            elif v[i] in "*/^":
                if v[i - 1] in "-+*/^.(":
                    self.printResult("ERROR")
                    return "ERROR"
                stiva.append(v[i])
                stivaval.append(Application.calcval(self, c, v[i]))
            elif v[i] == '+' and i != 0:
                if v[i - 1] in "-+*/^.":
                    self.printResult("ERROR")
                    return "ERROR"
                stiva.append(v[i])
                stivaval.append(Application.calcval(self, c, v[i]))
            elif v[i] == '-' and not ((i == 0 and v[i] == '-') or (v[i] == '-' and v[i - 1] == '(')):
                if v[i - 1] in "-+*/^.":
                    self.printResult("ERROR")
                    return "ERROR"
                stiva.append(v[i])
                stivaval.append(Application.calcval(self,c, v[i]))
        if c != 0 or paran[1] == 1:
            self.printResult("ERROR")
            return "ERROR"
        p = 0
        for i in range(len(v)):
            if (i == 0 and v[i] == '-') or (v[i] == '-' and v[i - 1] == '('):
                ok = 1
            elif v[i] == '.':
                if nr == -1:
                    nr = 0
                ok1 = 1
            elif v[i].isdigit():
                if nr == -1:
                    nr = 0
                if ok1 == 0:
                    nr = nr * 10 + int(v[i])
                else:
                    zec *= 10
                    nr = nr + int(v[i]) / zec
            else:
                if nr != -1:
                    if ok == 1:
                        nr *= -1
                    postv.append(nr)
                    nr = -1
                    ok = 0
                    ok1 = 0
                    zec = 1
                    postv.extend(sirsemn)
                    sirsemn = []
                if v[i] in "-+*/^":
                    for j in range(p, -1, -1):
                        if j + 2 < len(stiva):
                            v1 = stivaval[j]
                            v2 = stivaval[j + 1]
                            v3 = stivaval[j + 2]
                            if v1 >= v2 and v2 < v3:
                                sirsemn.append(stiva[j])
                                stiva.pop(j)
                                stivaval.pop(j)
                                p -= 1
                        elif j + 1 == len(stiva) - 1:
                            v1 = stivaval[j]
                            v2 = stivaval[j + 1]
                            if v1 > v2:
                                sirsemn.append(stiva[j])
                                stiva.pop(j)
                                stivaval.pop(j)
                                p -= 1
                        else:
                            break
                    p += 1
        if nr != -1:
            if ok == 1:
                nr *= -1
            postv.append(nr)
        for j in range(len(stiva) - 1, -1, -1):
            postv.append(stiva[j])
        i=0
        while i < len(postv):
            if(postv[i]=='+'):
                try:
                    postv[i]=Application.sum(self,postv[i-2],postv[i-1])
                except:
                    self.printResult("ERROR")
                    return "ERROR"
                postv.pop(i-1)
                postv.pop(i-2)
                i-=2
            elif (postv[i] == '-'):
                try:
                    postv[i] = Application.subtract(self,postv[i-2],postv[i-1])
                except:
                    self.printResult("ERROR")
                    return "ERROR"
                postv.pop(i - 1)
                postv.pop(i - 2)
                i -= 2
            elif (postv[i] == '*'):
                try:
                    postv[i] = Application.multiply(self,postv[i-2],postv[i-1])
                except:
                    self.printResult("ERROR")
                    return "ERROR"
                postv.pop(i - 1)
                postv.pop(i - 2)
                i -= 2
            elif (postv[i] == '/'):
                try:
                    postv[i] = Application.divide(self,postv[i-2],postv[i-1])
                except:
                    self.printResult("ERROR")
                    return "ERROR"
                postv.pop(i - 1)
                postv.pop(i - 2)
                i -= 2
            elif (postv[i] == '^'):
                if postv[i-2]==0 and postv[i-1]==0:
                    self.printResult("ERROR")
                    return "ERROR"
                try:
                    postv[i] = Application.power(self,postv[i-2],postv[i-1])
                except:
                    self.printResult("ERROR")
                    return "ERROR"
                postv.pop(i - 1)
                postv.pop(i - 2)
                i -= 2
            i+=1
        if len(postv) > 1:
            self.printResult("ERROR")
            return "ERROR"
        self.printResult(postv[0])

if __name__ == '__main__':

    vp_start_gui()
