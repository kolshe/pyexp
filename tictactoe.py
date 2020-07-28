# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 22:20:05 2015

@author: admin
"""

valid_moves = 1
valid_token = 0
board = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
         6: '6', 7: '7', 8: '8', 9: '9'}


def display():
    # displays board in cli
    for i in range(1, 10, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 7:
            print("---------")


def replace(ind, val):
    # replacing board value with the move
    board[int(ind)] = val
    global valid_moves
    valid_moves += 1


def inp_validation(inp_move, cor_mov):
    # para : input string and correct token corresponding
    #       to the player
    try:
        idx, val = inp_move.split(':')
    except Exception:
        print('invalid format')
        return
    else:
        if idx.isnumeric() and 0 < int(idx) <= 9:
            if val == cor_mov:
                if board[int(idx)] != 'o' and board[int(idx)] != 'x':
                    replace(idx, val)
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


def check_board(players_sym):
    # check if a player won
    # para : dictionary containing players
    player1_streak = players_sym[1] * 3
    player2_streak = players_sym[2] * 3

    data = list(board.values())
    columns = [1, 2, 3]
    rows = [1, 4, 7]
    total_data_set = []
    # populate total win possibilities
    # rows and columns
    for i in rows:
        total_data_set.append("".join(data[i-1: i+2]))
    for i in columns:
        total_data_set.append(f'{data[i-1]}{data[i+2]}{data[i+5]}')
    # diagonals
    total_data_set.append(f'{data[0]}{data[4]}{data[8]}')
    total_data_set.append(f'{data[2]}{data[4]}{data[6]}')
    # if pattern present, print winner
    if player1_streak in total_data_set:
        print('Player1 is the winner')
        global valid_moves
        valid_moves = 10
        return
    if player2_streak in total_data_set:
        print('player2 is the winner')
        valid_moves = 10
        return


print('hi welcome to tictac toe')
print('this is a 2 player game')
players = {1: '', 2: ''}
# selecting player1 token
while valid_token < 1:
    token_validation(input('player1 choose either "x" or "o"'))
# main logic
while valid_moves < 10:
    display()
    print('your move should be in format of "number:token" ')
    if valid_moves % 2 != 0:
        print(f"player1 turn. please enter 'number:{players[1]}'")
        inp_validation(input('enter your move: '), players[1])
    else:
        print(f"player2 turn. please enter 'number:{players[2]}'")
        inp_validation(input('enter your move: '), players[2])
    if valid_moves > 4:
        check_board(players)
print("game finished")
display()
