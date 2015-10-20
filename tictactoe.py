# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 22:20:05 2015

@author: admin
"""
board={'tl':' ','tm':' ','tr':' ','ml':' ','mm':' ','mr':' ','ll':' ','lm':' ','lr':' '}
def display():
    print " | | "
    print "_____"
    print " | | "
    print "_____"
    print " | | "
def values():
    for i in board.itervalues():
        print i
print 'hi welcome to tictac toe'
display()