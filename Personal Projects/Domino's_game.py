
'''Project Domino
Split the full domino set between the players and the stock by random. You should get three parts:
Stock pieces (14 domino elements), Computer pieces (7 domino elements), and Player pieces (7 domino elements).'''

# The full set
full_domino_set = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [2, 2], [2, 3], [2, 4], [2, 5], [2,6], [3, 3], [3, 4], [3, 5], [3, 6], [4, 4], [4, 5], [4, 6], [5, 5], [5, 6], [6, 6]]

# shuffle the hands 
import random
from re import X
random.shuffle(full_domino_set)
l_stock = full_domino_set[14::] 

l_player1 = full_domino_set[0:7]

l_computer = full_domino_set[7:14]

# print the hands 

print("Stock pieces: ", l_stock)
print("Computer pieces: ", l_computer)
print("Player pieces: ", l_player1)

# find the biggest piece 
Player_big_Piece = max(l_player1)
big_piece_comp = max(l_computer)

if big_piece_comp > Player_big_Piece:
    l_computer.remove(big_piece_comp)
    print("Domino snake: ",big_piece_comp)
    print("Status: Player")

elif Player_big_Piece > big_piece_comp:
    l_player1.remove(Player_big_Piece)
    print("Domino snake: ",Player_big_Piece)
    print("Status: Computer")
