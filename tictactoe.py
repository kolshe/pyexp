# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 22:20:05 2015

@author: admin
"""
valid_moves=1
valid_token = 0
board={1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}

def line_values(i):
    temp=[]
    for i in range(i,i+3):
        temp.append(board[i])
    print("|".join(temp))

def display():
    for i in range(1,10,3):
        print(board[i],"|",board[i+1],"|",board[i+2])
        if i < 7:
            print("---------")

def replace(inp_move,cor_mov):
    try:
        idx, val = inp_move.split(':')
    except Exception:
        print('invalid format')
        return
    else:
        if idx.isnumeric() and 0 < int(idx) <= 9:
            if val == cor_mov:
                if board[int(idx)] is not 'o':
                    if board[int(idx)] is not 'x':
                        board[int(idx)] = val
                        global valid_moves
                        valid_moves+=1
                    else:
                        print("invalid.the position is already filled")
                else:
                    print("invalid.the position is already filled")
            else:
                print(f"invalid. move should be '{cor_mov}' ")
        else:
            print("invalid.position should be number between 1 and 9")

def token_validation(value):
    if value == 'o':
        players[1] = 'o'
        players[2] = 'x'
        global valid_token
        valid_token = 1
    elif value == 'x':
        players[1] = 'x'
        players[2] = 'o'
        valid_token = 1
    else:
        print("invalid. enter 'x' or 'o' ")

def check_board(players):
    player1 = players[1]*3
    player2 = players[2]*3
    if "".join([board[1],board[2],board[3]]) == player1:
        global valid_moves
        valid_moves = 10
        print('player1 wins')
    if "".join([board[1],board[2],board[3]]) == player2:
        valid_moves = 10
        print('player2 wins')
    if "".join([board[4],board[5],board[6]]) == player1:
        valid_moves = 10
        print('player1 wins')
    if "".join([board[4],board[5],board[6]]) == player2:
        valid_moves = 10
        print('player2 wins')
    if "".join([board[7],board[8],board[9]]) == player1:
        valid_moves = 10
        print('player1 wins')
    if "".join([board[7],board[8],board[9]]) == player2:
        valid_moves = 10
        print('player2 wins')
    if "".join([board[1],board[5],board[9]]) == player1:
        valid_moves = 10
        print('player1 wins')
    if "".join([board[1],board[5],board[9]]) == player2:
        valid_moves = 10
        print('player2 wins')
    if "".join([board[3],board[5],board[7]]) == player1:
        valid_moves = 10
        print('player1 wins')
    if "".join([board[3],board[5],board[7]]) == player2:
        valid_moves = 10
        print('player2 wins')
    if "".join([board[1],board[4],board[7]]) == player1:
        valid_moves = 10
        print('player1 wins')
    if "".join([board[1],board[4],board[7]]) == player2:
        valid_moves = 10
        print('player2 wins')
    if "".join([board[2],board[6],board[8]]) == player1:
        valid_moves = 10
        print('player1 wins')
    if "".join([board[2],board[6],board[8]]) == player2:
        valid_moves = 10
        print('player2 wins')
    if "".join([board[3],board[7],board[9]]) == player1:
        valid_moves = 10
        print('player1 wins')
    if "".join([board[3],board[7],board[9]]) == player2:
        valid_moves = 10
        print('player2 wins')
#line_values(1)
print('hi welcome to tictac toe')
print('this is a 2 player game')
players={1:'',2:''}
while valid_token < 1:
    token_validation(input('player1 choose either "x" or "o"'))
while valid_moves < 10:
    display()
    print('your move should be in format of "number:token" ')
    if valid_moves%2 !=0:
        print(f"player1 turn. please enter 'number:{players[1]}'")
        replace(input('enter your move: '),players[1])
    else:
        print(f"player2 turn. please enter 'number:{players[2]}'")
        replace(input('enter your move: '),players[2])
    if valid_moves > 4:
        check_board(players)
print("game finished")
display()