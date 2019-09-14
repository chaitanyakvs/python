import random
import tkinter
#import tkMessageBox

a=[1, 4, 8, 10, 3]
def fun(x):
    print("removed")
    a.remove(x)
    
def fun1():
    print("not removed")
b=random.choice(a)
print (b)
top = tkinter.Tk()
frame=tkinter.Frame(top)
frame.pack()
c = tkinter.Button(frame, text ="removed", command = fun(b))
c.pack(side=tkinter.LEFT)
d =  tkinter.Button(frame, text ="not removed",command = fun1())
d.pack(side=tkinter.LEFT)
e= tkinter.Button(frame, text ="quit",command = quit)
e.pack(side=tkinter.LEFT)
print(a)
top.mainloop()

