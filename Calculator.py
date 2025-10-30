from tkinter import *

window=Tk()
window.title("Calculator")
# window.geometry("400x500")

def eventhandler(value):
    Display.insert(END,value)

def Clear():
    Display.delete(0,END)

def submitEvent():
    text=Display.get()
    print(text)
    try:
        value=eval(text)
        Clear()
        Display.insert(END,value)
    except Exception:
        Clear()
        Display.insert(END,"Error")

Display=Entry(window,width=30)
value9=Button(window,text="9",width=10,height=2  ,command= lambda: eventhandler("9"))
value8=Button(window,text="8",width=10,height=2  ,command= lambda: eventhandler("8"))
value7=Button(window,text="7",width=10,height=2  ,command= lambda: eventhandler("7"))
value6=Button(window,text="6",width=10,height=2 ,command=  lambda: eventhandler("6"))
value5=Button(window,text="5",width=10,height=2  ,command= lambda: eventhandler("5"))
value4=Button(window,text="4",width=10,height=2 , command= lambda: eventhandler("4"))
value3=Button(window,text="3",width=10,height=2 ,command=  lambda: eventhandler("3"))
value2=Button(window,text="2",width=10,height=2 ,command=  lambda: eventhandler("2"))
value1=Button(window,text="1",width=10,height=2  ,command=  lambda: eventhandler("1"))
value0=Button(window,text="0",width=10,height=2 , command=  lambda: eventhandler("0"))
clear=Button(window,text="clear",width=20,height=2,command=Clear)
add=Button(window,text="+",width=10,height=2,command=lambda : eventhandler("+"))
submit=Button(window,text="=",width=20,height=2,command=submitEvent)
sub=Button(window,text="-",width=10,height=2,command=lambda : eventhandler("-"))
mul=Button(window,text="*",width=10,height=2,command=lambda : eventhandler("*"))
div=Button(window,text="/",width=10,height=2,command=lambda : eventhandler("/"))

Display.grid(row=0,column=0,columnspan=3,pady=10)
value9.grid(row=1,column=0)
value8.grid(row=1,column=1)
value7.grid(row=1,column=2)
value6.grid(row=2,column=0)
value5.grid(row=2,column=1)
value4.grid(row=2,column=2)
value3.grid(row=3,column=0)
value2.grid(row=3,column=1)
value1.grid(row=3,column=2)
value0.grid(row=4,column=0)
clear.grid(row=4,column=1,columnspan=2)
add.grid(row=5,column=0)
submit.grid(row=5,column=1,columnspan=2)
sub.grid(row=6,column=0)
mul.grid(row=6,column=1)
div.grid(row=6,column=2)
window.mainloop()