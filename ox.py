from tkinter import *
import tkinter as tk
from tkinter import messagebox


board = [' ' for _ in range(9)]

def minimax(board, depth, is_maximizing):
    if check_win(board, 'O'):
        return 1
    elif check_win(board, 'X'):
        return -1
    elif len(available_moves()) == 0:
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for move in available_moves():
            board[move] = 'O'
            score = minimax(board, depth + 1, False)
            board[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in available_moves():
            board[move] = 'X'
            score = minimax(board, depth + 1, True)
            board[move] = ' '
            best_score = min(score, best_score)
        return best_score

root = tk.Tk()
root.title("Tic Tac Toe")
root.config(background="#41B77F")
root.geometry("880x520")
root.minsize(500,500)


def make_move(move, player):
    board[move] = player

def check_win(board, player):
    if (
        (board[0] == player and board[1] == player and board[2] == player) or
        (board[3] == player and board[4] == player and board[5] == player) or
        (board[6] == player and board[7] == player and board[8] == player) or
        (board[0] == player and board[3] == player and board[6] == player) or
        (board[1] == player and board[4] == player and board[7] == player) or
        (board[2] == player and board[5] == player and board[8] == player) or
        (board[0] == player and board[4] == player and board[8] == player) or
        (board[2] == player and board[4] == player and board[6] == player)
    ):
        return True
    else:
        return False

def available_moves():
    moves = []
    for i in range(len(board)):
        if board[i] == ' ':
            moves.append(i)
    return moves

def reset_game():
    global board
    board = [' ' for _ in range(9)]
    draw_board()

def ai_move(available_moves_func):
    computer_move = None
    best_score = -float('inf')
    for move in available_moves_func():
        board[move] = 'O'
        score = minimax(board, 0, False)
        board[move] = ' '

        if score > best_score:
            best_score = score
            computer_move = move

    make_move(computer_move, 'O')
    draw_board()
    if check_win(board, 'O'):
        
        available_moves = []
        result_label = tk.Label(root, text="Game Over   Computer Wins!", font=("Courrier",20 ))
        result_label.grid()
        result_label.place(x=500, y=70)
        messagebox.showinfo("Game Over", "Computer Wins!")
        available_moves_func = lambda: []
        reset_game()
        
    elif len(available_moves_func()) == 0:
        resultt_label = tk.Label(root, text="Game Over   Tie Game!", font=("Courrier",30 ))
        resultt_label.grid()
        resultt_label.place(x=500, y=70)


def draw_board():
    for widget in root.winfo_children():
        widget.destroy()
    for i in range(3):
        for j in range(3):
            button = Button(root, text=board[3*i+j], font=('Helvetica', 48), width=3, height=1, 
                            command=lambda move=3*i+j: player_move(move))
            button.grid(row=i, column=j, sticky='N', padx=0, pady=0)
    
    submit_button = tk.Button(root, text="REPLAY", command=reset_game, font=('Helvetica', 18),bg='#41B77F',fg='white')
    submit_button.grid()
    submit_button.place(x=500, y=30)

def player_move(move):
    if board[move] == ' ':
        make_move(move, 'X')
        draw_board()
        if check_win(board, 'X'):
            messagebox.showinfo("Game Over", "You Win!")
        elif len(available_moves()) > 0:
            ai_move(available_moves)
    else:
        sult_label = tk.Label(root, text="Invalid Move", font=("Courrier",20 ))
        sult_label.grid()
        sult_label.place(x=500, y=100)


def main():
    draw_board()

main()
root.mainloop()
