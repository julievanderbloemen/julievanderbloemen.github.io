# CS1210: HW1
######################################################################
# Complete the signed() function, certifying that:
#  1) the code below is entirely your own work, and
#  2) you have not shared it with anyone else.
#
# ToDo: Change the word "hawkid" between the two double quote marks to
# match your own hawkid. Your hawkid is the "login identifier" (not
# your email address) that you use to login to all University
# services.
#
def signed():
    return(["jevanderbloemen"])

######################################################################
# You will likely require one or more functions from the random module.
from random import *

######################################################################
# Specification: new(N) creates a representation of a fresh Hus board
# consisting of N*4 pits, conceptually arranged in four rows of N pits
# each. Selected pits initially contain 2 playing pieces; the rest are
# empty.
#
# We will represent our board as a list of 4N elements with the
# standard opening layout of tokens in the pits.
#
def new(N):
    '''returns list representing a new board with N pits in each row'''
    num = 3*N-N%2
    return [2]*(num//2)+[0]*((4*N-num)//2)+[2]*(num//2)+[0]*((4*N-num)//2)

######################################################################
# Specification: show(B) produces a string representation of B, a Hus
# board represented as a list of integers.
#
# Although the board B is really just a list of integers, it should be
# conceptually interpreted as four rows of pits, where the ith pit
# contains a number of playing pieces equal to the value of the ith
# element of the list.
#
# We'll index the board representation starting with pit 0 at the
# bottom left and proceeding counter-clockwise through the bottom two
# rows, each with N=len(B)//4 pits. The top two rows will be labeled
# starting from the top left and proceeding counter-clockwise through
# the top two rows. So, for len(B)=32:
#
#   ---------------------------------
#   | 23| 22| 21| 20| 19| 18| 17| 16|
#   ---------------------------------
#   | 24| 25| 26| 27| 28| 29| 30| 31|
#   =================================
# I | 15| 14| 13| 12| 11| 10|  9|  8|
#   ---------------------------------
# O |  0|  1|  2|  3|  4|  5|  6|  7|
#   ---------------------------------
#     a   b   c   d   e   f   g   h
#
# The lower half of the board represents the human player's POV
# ("point of view"). The 'O' and 'I' along with the lower case letters
# across the bottom are used to index the pits in this player's
# "inner" and "outer" rows (below the double line), so, for example,
# 'Id' corresponds to pit 12 (Note: the human player does not need to
# refer to pits in the opponent's rows, which are above the double
# line).
#
# When properly constructed, this function can still be fairly
# compact; review the use of the format() methods for strings from the
# Python documentation (your text documents an older, deprecated,
# version of this method), and recall the combination of the string
# join() method and list comprehensions can be a powerful
# combination. Also, you may wish to explore the chr() function for
# converting integers into alphabetic characters.
#
# Finally, to help in debugging, we'll include a "verbose" mode that
# provides pit indexes in the margins.
#
# Here's an example of how this function would work with the new()
# function above:
#
# >>> print(show(new(5)))
#   ---------------------
#   |  2|  2|  2|  2|  2|
#   ---------------------
#   |  2|  2|  0|  0|  0|
#   =====================
# I |  0|  0|  0|  2|  2|
#   ---------------------
# O |  2|  2|  2|  2|  2|
#   ---------------------
#     a   b   c   d   e   
# 

def show(B, verbose=False):
    '''returns string to display formatted board (B)'''
    #sets varibles to inital vaules
    n = len(B)//4
    index = list(range(n*3-1, n*2-1, -1)) + list(range(n*3,n*4))
    index += list(range(n*2-1, n-1, -1)) + list(range(n))
    printing= ["   "+"-"*(n*4+1)+"\n   "]
    count = 0
    left = index[0]

    #loops through index by number
    for i in index:
        count+=1
   
        printing += "|{:>3g}".format(B[i])

        if count%n == 0:    #aka if end of line
            if verbose:
                printing += "|    [pits: range({},{},{})]".format(left, i, (-1)**(i+1))
                if count < n*4:
                    left = index[count]
            #print next line depend on which line
            if count == n*2:
                printing += "|\n   "+"="*(n*4+1)+"\n I "
            elif count == n*3:
                printing += "|\n   "+"="*(n*4+1)+"\n O "
            else:
                printing += "|\n   "+"-"*(n*4+1)+"\n   "


    #add letters
    printing += " "
    for x in range(n):    
        printing += "{:^4s}".format(chr(97+x))
        
    return "".join(printing)
    
######################################################################
# Specification: Given a pit index, player(B, i) returns 0 if the
# specified pit is in player 0's "orbit" (i.e., the lower half of
# board) and 1 if pit is in player 1's "orbit" (i.e., the upper half
# of the board).
#
# Recall B is a 4*N array representing the four rows of the Hus
# board. Assume i is a legal index of B.
#
def player(B, i):
    '''returns player assigned given pit(i)'''
    return ( i//(len(B)//2) )

######################################################################
# Specification: Given a pit index, next(B, i) returns the next pit
# index in the appropriate player's "orbit."
#
# Recall B is a 4*N array representing the four rows of the Hus
# board. Assume i is a legal index of B, and feel free to use
# player(B, i) as appropriate.
#
def next(B, i):
    '''returns index of pit after given pit(i) for same player'''
    if player(B, i+1)== player(B, i):
        return i+1
    else:
        return (len(B)//2)*(player(B, i))

######################################################################
# Specification: Given a pit index, inner(B, i) returns True if it is
# an inner pit. Note that being an inner pit is independent of player;
# it simply reflects if the index is in the innermost rows of the
# board. 
#
# Recall B is a 4*N array representing the four rows of the Hus
# board. Assume i is a legal index of B, and feel free to use
# player(B, i) as appropriate.
#
def inner(B, i):
    '''returns True if given pit(i) is an inner pit'''
    return len(B)//4 <= i < len(B)//2 or len(B)*3//4 <= i < len(B)

######################################################################
# Specification: outer(B, i) returns the corresponding outer pit for
# any given inner pit i. 
#
# Recall B is a 4*N array representing the four rows of the Hus
# board. Assume i is a legal inner-pit index of B (either player).
#
def outer(B, i):
    '''return index of the corresponding outer pit of inner pit(i)'''
    setB = {len(B)//2-1-x:x for x in range(len(B)//4)}
    setB.update({len(B)-1-x:len(B)//2+x for x in range(len(B)//4)})
    return setB[i]

######################################################################
# Specification: other(B, i) returns the opponent's corresponding
# inner pit for any given inner pit i. Assumes i is a legal inner pit.
#
# Recall B is a 4*N array representing the four rows of the Hus
# board. Assume i is a legal inner-pit index of B (either player).
#
def other(B, i):
    '''returns index of opponents corresponding inner pit to given inner pit(i)'''
    oSetB = {len(B)*3//4+x:len(B)//2-1-x for x in range(len(B)//4)}
    oSetB.update({len(B)//2-1-x:len(B)*3//4+x for x in range(len(B)//4)})
    return oSetB[i]

######################################################################
# Specification: clear(B, i) empties pit i and returns the number of
# tokens removed. Assume i is a legal index of B.
#
def clear(B, i):
    '''empties given pit(i) and return number of tokens removed'''
    B.insert(i, 0)
    return B.pop(i+1)

######################################################################
# Specification: Return a list of pit indexes having at least 2 tokens
# for given board B and player P. Returns the empty list if player P
# has no legal moves remaining. Note: as for player(B, i), P==0
# corresponds to the "lower" player, while P==1 corresponds to the
# "upper" player. So:
#    >>> legal(new(5), 0)
#    [0, 1, 2, 3, 4, 5, 6]
#    >>> legal(new(5), 1)
#    [10, 11, 12, 13, 14, 15, 16]
#
def legal(B, P):
    '''returns list of legal moves for player(P)'''
    if P == 1:
        rng = range(len(B)//2, len(B))
    else:
        rng = range(0, len(B)//2)
    moves = []
    for i in rng:
        if B[i] >= 2:
            moves.append(i)
    return moves
            

######################################################################
# Specification: Choose a random legal move for player P from board B;
# returns the index of the selected pit. Relies on implementation of
# legal(). Modifies B, returning a (pit, count) tuple after clearing
# the pit of count tokens.
#
def chooseAutomatic(B, P):
    '''randomly selects a legal move for player(P)
returns tuple of index and tokens from selected move'''
    pick = choice(legal(B, P))
    return (pick, clear(B, pick))

######################################################################
# Specification: Ask the user (always player P==0) to select a move
# for given board B: returns the selected pit index. Relies on
# implementation of legal(); rejects illegal moves and prompts the
# user to try again.
#
# Note that moves are specified as two-letter strings, where the first
# letter is either I or O (for "inner" or "outer") and the second
# indicates the column. So, for example, 'Oa' indicates the first
# player's home position. Other examples of legal moves include 'Ic',
# 'oE', 'ib' (as long as the board is at least 5 pits wide).
#
# Modifies B and returns a (pit, count) tuple after clearing the pit
# of count tokens. 
#
def chooseManual(B):
    '''users selects a legal move for player 0
returns tuple of index and tokens from selected move'''
    
    while True:
        #pick inputed form user
        pick = input("Enter move: ").lower()
        
        #translate letter to corresponding number
        charNum = "abcdefghijklmnopqrstuvwxyz".index(pick[1])
        
        #if letter in width of board
        if charNum < len(B)//4:
            #outer loop
            if pick[0] == 'o':
                numPick = charNum
            #inner loop
            elif pick[0] == 'i':
                numPick = len(B)//2-charNum-1
            else:   #if not outer or inner, restarts loop
                print("Try again!")
                continue
        else:   #if not within width, restarts loop
            print("Try again.")
            continue
        
        #check if legal and solve 
        if numPick in legal(B, 0):
            return (numPick, clear(B, numPick))
        else:
            print("Not a legal choice. Try again.")

######################################################################
# Specificiation: takes a board, B, and distributes count tokens
# counter-clockwise starting at pit i for player P. Performs capture
# and (recursive) relay sowing as appropriate, and returns total
# number of tokens captured.
#
# This function must be recursive, and should respect the verbose
# flag.
#
# Hint: first, write the function so that it sows correctly, and
# ignores captures. Once you are sure you have done this correctly,
# add capturing from the opponent's inner pit. Only once you are
# convince that's correct, complete the function to consider capturing
# also from the outer pit.
#
# Incorporate reasonable verbose feedback.
#
def sow(B, i, count=0, captured=0, verbose=False):
    '''drops tokens in pit (i) recursivly until out of tokens (count==0) and either
captures tokens from opponent or pit landed in (recursive)
or lands on empty pits (base case)
returns total tokens captured'''
    
    if legal(B,(player(B, i)+1)%2):     #checks other player has legal move
        #recursive step
        if count > 1:   
            B[i] += 1
            captured = sow(B, next(B, i), count-1, captured, verbose)
        
        else:
            #capture & recursive step
            if B[i] != 0:
                grab = 0 #amount capture on this turn alone
                #inner capture
                if inner(B, i):
                    #outer capture
                    if B[other(B, i)] != 0:
                        grab += clear(B, outer(B, other(B, i)))
                    grab += clear(B, other(B, i))
                    count += grab
                    
                if verbose:
                    print("Landed on bin {} [{} + {}]: resowing.".format(i, B[i]+1, grab))
                count += clear(B, i)
                captured = sow(B, next(B, i), count, captured+grab, verbose)
            #base case when land on 0
            else:
                B[i] += 1
                if verbose:
                    print("Landed on empty bin {}.".format(i))
                    
    return captured
######################################################################
# Game driver. Flag verbose to see inner workings. Returns None.  The
# only thing you need to do here is provide a reasonable doc string.
#
def play(N=8, verbose=False):
    '''alternates players moves, counting total captures until
player has no legal moves left, and loses'''

    # Create new board of specified size.
    B = new(N)

    # Turn counter (determines which player moves next). The human
    # player always gets to go first.
    player = 0
    # Keep track of captures.
    captures = [0, 0]

    while(legal(B, player)):
        # Show the board and announce who is up next.
        print(show(B, verbose))
        if player == 0:
            (pit, count) = chooseManual(B)
        else:
            (pit, count) = chooseAutomatic(B, player)
        print("Player {} chooses pit {}".format(player, pit))
        # Execute the move.
        captures[player] += sow(B, next(B, pit), count, verbose=verbose)
        print("End of turn: current score is {}\n".format(captures))
        # Advance to next player.
        player = (player+1)%2
    else:
        print("Player {} loses!".format(player))

    # Print final score.
    print("Congratulations player {}!".format((player+1)%2))
    print(show(B))
    print("Final balance: {}".format(captures))

