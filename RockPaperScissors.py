from tkinter import *
import random

window=Tk()
Label(window,text="Your Choice:").grid(row=0,column=0)
Label(window,text="Computer Choice:").grid(row=0,column=1)
result_label=Label(window,text="")
UserChoice=Label(window,text="")
ComputerAns=Label(window,text="")


result_label.grid(row=2,column=0,columnspan=2)
UserChoice.grid(row=1,column=0)
ComputerAns.grid(row=1,column=1)

def WinnerDec(userChoice):
    computerChoice=random.randint(1,3)
    if userChoice == 1 :
        UserChoice.config(text="👊Rock")
    elif userChoice ==2:
        UserChoice.config(text="📄paper")
    else :
         UserChoice.config(text="✂️scissor")
         
    if computerChoice == 1 :
        ComputerAns.config(text="👊Rock")
    elif computerChoice ==2:
        ComputerAns.config(text="📄paper")
    else :
         ComputerAns.config(text="✂️scissor")
    
    if userChoice == computerChoice:
        result="Tie"
    elif (userChoice == 1 and computerChoice == 3) or \
     (userChoice == 2 and computerChoice == 1) or \
     (userChoice == 3 and computerChoice == 2):
     result = "You win"
    else:
        result = "You lose"

    result_label.config(text=result)
        
Button(window,text="👊Rock",command=lambda : WinnerDec(1)).grid(row=3,column=0)
Button(window,text="📄paper",command=lambda : WinnerDec(2)).grid(row=3,column=1)
Button(window,text="✂️scissor",command=lambda : WinnerDec(3)).grid(row=3,column=2)


window.mainloop()