from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Tik Tak To")

Label(window, text="Tik Tak To", font=("Helvetica", 18, "bold"), padx=10, pady=10).grid(row=0, column=0, columnspan=3)
Label(window, text="Player 1:", font=("Arial", 12), padx=5, pady=5).grid(row=1, column=0)
Label(window, text="Player 2:", font=("Arial", 12), padx=5, pady=5).grid(row=1, column=1)
Label(window, text="X", font=("Arial", 12, "bold"), padx=5, pady=5).grid(row=2, column=0)
Label(window, text="O", font=("Arial", 12, "bold"), padx=5, pady=5).grid(row=2, column=1)


main = Frame(window)
main.grid(row=3, column=0, columnspan=3, pady=10)

turn = [0]  
buttons = [  
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

def check_winner():

    wins = [
        [(0,0), (0,1), (0,2)],  
        [(1,0), (1,1), (1,2)],  
        [(2,0), (2,1), (2,2)],  
        [(0,0), (1,0), (2,0)],  
        [(0,1), (1,1), (2,1)],  
        [(0,2), (1,2), (2,2)],  
        [(0,0), (1,1), (2,2)],  
        [(0,2), (1,1), (2,0)]   
    ]


    for combo in wins:
        a, b, c = combo
        if buttons[a[0]][a[1]]["text"] == buttons[b[0]][b[1]]["text"] == buttons[c[0]][c[1]]["text"] != "":
            winner = buttons[a[0]][a[1]]["text"]
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_game()
            return


    if all(buttons[i][j]["text"] != "" for i in range(3) for j in range(3)):
        messagebox.showinfo("Game Over", "It's a draw!")
        reset_game()

def eventhandler(button, i, j):
    player = "X" if turn[0] % 2 == 0 else "O"
    button.config(text=player, state=DISABLED)
    turn[0] += 1
    check_winner()

def reset_game():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state=NORMAL)
    turn[0] = 0

for i in range(3):
    for j in range(3):
        btn = Button(
            main,
            text="",
            font=("Helvetica", 16, "bold"),
            width=5,
            height=2,
            padx=10,
            pady=10,
        )
        btn.config(command=lambda b=btn, i=i, j=j: eventhandler(b, i, j))
        btn.grid(row=i, column=j, padx=5, pady=5)
        buttons[i][j] = btn 

window.mainloop()
