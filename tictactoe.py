# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 22:20:05 2015

@author: admin
"""
board={'tr':' ','tm':' ','tl':' ','mr':' ','mm':' ','ml':' ','lr':' ','lm':' ','ll':' '}
def display():
    print  board['tr'],
    print  "|",
    print  board['tm'],
    print "|",
    print  board['tl']
    bottom_lines()
    print board['mr'],
    print "|",
    print board['mm'],
    print "|",
    print board['ml']
    bottom_lines()
    print board['lr'],
    print "|",
    print board['lm'],
    print "|",
    print board['ll']
def bottom_lines():
    print '_',
    print '_',
    print '_',
    print '_',
    print '_'
def values():
    for i in board.itervalues():
        print i
print 'hi welcome to tictac toe'
display()
print 'enter your move'
