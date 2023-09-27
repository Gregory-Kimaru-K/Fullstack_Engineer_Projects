import random

board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

gamerunning = True
winner = None
current_player = "X"

def printboard(board):
    print (' ' + board[0] + '|' + board[1] + '|' + board[2])
    print (' ' + board[3] + '|' + board[4] + '|' + board[5])
    print (' ' + board[6] + '|' + board[7] + '|' + board[8])

def user_input(board):

    inp = int(input("Choose between 1-9: "))
        
    if inp >= 1 or inp <= 9 or board[inp-1] != '-':
        board[inp-1] = current_player
        
    else:
        print ("Invalid input!")

def continue_play():
    while True:
        con = input("Do you want to continue playing (Y or N): ").upper()

        if con not in ('Y', 'N'):
            print ("Invalid input!")
        if con == 'Y':
            return True
        
        else:
            return False
    
def column_win(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != '-':
        winner = board[0]
        return True
    
    if board[3] == board[4] == board[5] and board[3] != '-':
        winner = board[3]
        return True
    
    if board[6] == board[7] == board[8] and board[6] != '-':
        winner = board[6]
        return True
    
def diagonal_win(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != '-':
        winner = board[0]
        return True
    
    if board[2] == board[4] == board[6] and board[2] != '-':
        winner = board[2]
        return True

def row_win(board):
    global winner

    if board[0] == board[3] == board[6] and board[0] != '-':
        winner = board[0]
        return True
    
    if board[1] == board[4] == board[7] and board[1] != '-':
        winner = board[1]
        return True
    
    if board[2] == board[5] == board[8] and board[2] != '-':
        winner = board[2]
        return True

def check_tie(board):
    global gamerunning

    if '-' not in board:
        printboard(board)
        print ("Great game its a tie")
        
        gamerunning = False

def check_win():
    global gamerunning
    if column_win(board) or row_win(board) or diagonal_win(board):
        printboard(board)
        print ("Congratulations player {winner}")

        gamerunning = False

def switch_player():
    global current_player

    if current_player == 'X':
        current_player = 'O'
    
    else:
        current_player = 'X'

def continue_play():
    con = None
    while con not in ('Y', 'N'):
        con = input("Do you want to continue playing (Y or N): ").upper()

        if con not in ('Y', 'N'):
            print ("Invalid input!")
        if con == 'Y':
            return True
        
        else:
            return False
        
def computer(board):
    while current_player == 'O':
        position = random.randint(0, 8)

        if board[position] == '-':
            board[position] = 'O'
            switch_player()

while gamerunning:
    printboard(board)
    user_input(board)
    check_win()
    check_tie(board)
    switch_player()
    computer(board)
    check_win()
    check_tie(board)