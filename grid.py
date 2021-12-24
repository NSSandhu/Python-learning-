"""This module contains a code example related to 

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
Copyright 2015 Allen Downey
License: http://creativecommons.org/licenses/by/4.0/

My grid creating python solution is given below
"""

def box_print_adv(r,c):   #pass argument of how many rows and columns needed
    print("Grid",r,"x",c) 
    st_end_row = ("+ - - - - "*c + "+") #create the starting row variable with correct no. of columns
    for i in range(r):
        print(st_end_row)              #print the top border and 
        box_bet_rows(c)                 #then print the inner areas using box_bet_rows function to which the column number is passed as argument 
    print(st_end_row)                   #close off by bottom border.
    
def box_bet_rows(c):
    between_row = ("|         "*c + '|') #print row with appropriate repetition and close
    for i in range(4):
        print(between_row)
    
box_print_adv(4,4)
