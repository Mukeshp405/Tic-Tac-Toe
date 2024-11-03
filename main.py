# Tic Tac Toe

from tkinter import *
from tkinter import messagebox

game_end = False

# Main play function which sets up the game with the choosen symbol
def play(symbol):
    # set the turn as global variable
    global turn

    # Set the current turn symbol
    turn = symbol

    # Frame (f2) created
    f2 = Frame(root, bg="gray30" ,width=500, height=550)
    f2.place(x=0, y=0)

    # Display chosen symbol and turn information
    t1 = Label(f2, text=f"Your Symbol :- {symbol}", font="Arial 20 bold", bg="gray30", fg="burlywood1")
    t1.place(x=0,y=0)
    text_turn = Label(f2, text=f"{turn} Turn", font="Arial 24 bold", bg="gray30", fg="burlywood1")
    text_turn.place(x=380, y=0)

    # Initialize game board with empty spaces
    board = {1:" ", 2:" ", 3:" ",
             4:" ", 5:" ", 6:" ",
             7:" ", 8:" ", 9:" "}

    # Check for winner
    def checkForWin(player):
        # Check rows for win condition
        if board[1] == board[2] and board[2] == board[3] and board[3] == player:
            return True
        if board[4] == board[5] and board[5] == board[6] and board[6] == player:
            return True
        if board[7] == board[8] and board[8] == board[9] and board[9] == player:
            return True

        # Check columns for win condition
        if board[1] == board[4] and board[4] == board[7] and board[7] == player:
            return True
        if board[2] == board[5] and board[5] == board[8] and board[8] == player:
            return True
        if board[3] == board[6] and board[6] == board[9] and board[9] == player:
            return True

        # Check diagonals for win condition
        if board[1] == board[5] and board[5] == board[9] and board[9] == player:
            return True
        if board[3] == board[5] and board[5] == board[7] and board[7] == player:
            return True
        return False
    
    # Check if the game is Draw
    def checkForDraw():
        # If any cell is empty, reurn false (not a draw)
        for i in board:
            if board[i] == " ":
                return False
        return True
    
    # Restart Game
    def restartGame():
        global game_end
        game_end = False
        # Clear all buttons
        for button in buttons:
            button["text"] = " "
        
        # Reset board cells
        for i in board:
            board[i] = " "

    # Exit the Game
    def exitGame():
        root.quit() # Close the application

    # Function to handle button click events for each cell
    def click_event(event):
        global turn, game_end
        # if game has ended, ignore clicks
        if game_end:
            return
        btn = event.widget
        str_btn = str(btn)
        clicked_btn = str_btn[-1:]
        if clicked_btn == "n":
            clicked_btn = 1
        else:
            clicked_btn = int(clicked_btn)
        
        # If cell is empty, place symbol
        if btn["text"] == " ":
            btn["text"] = turn
            if turn == "X":
                btn["fg"] = "DeepSkyBlue2"
                btn["activeforeground"] = "DeepSkyBlue2"

                # Set board value
                board[clicked_btn] = turn

                # Check if current player wins
                if checkForWin(turn):
                    messagebox.showinfo(f"{turn}", f"{turn} Wins the Game")
                    game_end = True
                
                # Switch turn into "O"
                turn = "O"
                text_turn = Label(f2, text=f"{turn} Turn", font="Arial 24 bold", bg="gray30", fg="burlywood1")
                text_turn.place(x=380, y=0)
            else:
                btn["fg"] = "DarkOrange1"
                btn["activeforeground"] = "DarkOrange1"

                # Set board value
                board[clicked_btn] = turn 

                # Check if current player wins
                if checkForWin(turn):
                    messagebox.showinfo(f"{turn}", f"{turn} Wins the Game")
                    game_end = True
                
                # Switch turn into "X"
                turn = "X"
                text_turn = Label(f2, text=f"{turn} Turn", font="Arial 24 bold", bg="gray30", fg="burlywood1")
                text_turn.place(x=380, y=0) 

        if checkForDraw():
            messagebox.showinfo("Game Draw!!!", "Game Draw!!!")       
            
    # Buttons 
    b1 = Button(f2, text=" ", font="Arial 30 bold", borderwidth=5, relief=SUNKEN, width=5, height=2, bg="khaki1", activebackground="khaki1")
    b1.place(x=50, y=70)
    b1.bind("<Button-1>", click_event)
    
    b2 = Button(f2, text=" ", font="Arial 30 bold", borderwidth=5, relief=SUNKEN, width=5, height=2, bg="khaki1", activebackground="khaki1")
    b2.place(x=185, y=70)
    b2.bind("<Button-1>", click_event)
    
    b3 = Button(f2, text=" ", font="Arial 30 bold", borderwidth=5, relief=SUNKEN, width=5, height=2, bg="khaki1", activebackground="khaki1")
    b3.place(x=320, y=70)
    b3.bind("<Button-1>", click_event)

    b4 = Button(f2, text=" ", font="Arial 30 bold", borderwidth=5, relief=SUNKEN, width=5, height=2, bg="khaki1", activebackground="khaki1")
    b4.place(x=50, y=200)
    b4.bind("<Button-1>", click_event)

    b5 = Button(f2, text=" ", font="Arial 30 bold", borderwidth=5, relief=SUNKEN, width=5, height=2, bg="khaki1", activebackground="khaki1")
    b5.place(x=185, y=200)
    b5.bind("<Button-1>", click_event)

    b6 = Button(f2, text=" ", font="Arial 30 bold", borderwidth=5, relief=SUNKEN, width=5, height=2, bg="khaki1", activebackground="khaki1")
    b6.place(x=320, y=200)
    b6.bind("<Button-1>", click_event)

    b7 = Button(f2, text=" ", font="Arial 30 bold", borderwidth=5, relief=SUNKEN, width=5, height=2, bg="khaki1", activebackground="khaki1")
    b7.place(x=50, y=330)
    b7.bind("<Button-1>", click_event)

    b8 = Button(f2, text=" ", font="Arial 30 bold", borderwidth=5, relief=SUNKEN, width=5, height=2, bg="khaki1", activebackground="khaki1")
    b8.place(x=185, y=330)
    b8.bind("<Button-1>", click_event)

    b9 = Button(f2, text=" ", font="Arial 30 bold", borderwidth=5, relief=SUNKEN, width=5, height=2, bg="khaki1", activebackground="khaki1")
    b9.place(x=320, y=330)
    b9.bind("<Button-1>", click_event)

    # Restart Button
    reset_btn = Button(f2, text="Restart", font="Arial 15 bold", borderwidth=5, relief=RAISED, bg="sandy brown", command=restartGame)
    reset_btn.place(x=110, y=480)

    # Quit Button
    exit_btn = Button(f2, text="Quit", font="Arial 15 bold", borderwidth=5, relief=RAISED, command=exitGame,bg="sandy brown", width=5)
    exit_btn.place(x=310, y=480)

    # List of all buttons
    buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

# Function for when 'X' button is clicked
def xclick_event(event):
    play("X")

# Function for when 'O' button is clicked
def oclick_event(event):
    play("O")

# Function to choose X or O
def choose_func(event):
    # Frame {f1} (Choose X or O)
    f1 = Frame(root, bg="gray30", width=500, height=550)
    f1.place(x=0, y=0)

    # Choose your Symbol
    sym = Label(f1, text="Choose your Symbol...", font="Arial 32 bold", bg="gray30", fg="peach puff")
    sym.place(x=20, y=90)

    # Button X
    Xbtn = Button(f1, text="X", font="Arial 50 bold", bg="gray21", fg="DeepSkyBlue2", borderwidth=5)
    Xbtn.place(x=90, y=240)
    Xbtn.bind("<Button-1>", xclick_event)

    # Button O
    Obtn = Button(f1, text="O", font="Arial 50 bold", bg="gray21", fg="DarkOrange1", borderwidth=5)
    Obtn.place(x=300, y=240)
    Obtn.bind("<Button-1>", oclick_event)

# Main Frame (root)
root = Tk()
root.title("Tic Tac Toe")
root.minsize(500, 550)
root.maxsize(500, 550)

# set title logo
title_logo = PhotoImage(file="E:/laptop/Python_GUI/python_GUI_using_tkinter/tic_tac_toe/t3.png")
root.iconphoto(True, title_logo)


# set background image
back_img = PhotoImage(file="E:/laptop/Python_GUI/python_GUI_using_tkinter/tic_tac_toe/t2.png")
back_img_resize = back_img.subsample(1, 1)
back_img_pack = Label(root, image=back_img_resize)
back_img_pack.pack()

# set logo
logo_img = PhotoImage(file="E:/laptop/Python_GUI/python_GUI_using_tkinter/tic_tac_toe/t1.png")
logo_img_resize = logo_img.subsample(2, 2)
logo_img_pack = Label(root, image=logo_img_resize, background="white")
logo_img_pack.place(x=150, y=150)

# Start button
start_btn = Button(root, text="Start", font="Arial 19 bold", relief=RAISED, borderwidth=5, bg="gray21", activebackground="gray31",activeforeground="white", fg="white")
start_btn.place(x=205, y=380)
start_btn.bind("<Button-1>", choose_func)

root.mainloop()
