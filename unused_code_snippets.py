'''
# getting the moves only without move numbers
moves = games[0].moves[::2]

# adding move numbers
current_move_number = 0
for i in range(0, len(moves)):
    # if the move is the first, third, fifth... but not the game result
    if(i % 2 == 0 and moves[i] != "0-1" and moves[i] != "1/2-1/2" and moves[i] != "1-0"):
        current_move_number += 1
        moves[i] = str(current_move_number)+"."+moves[i]


# getting the timing of the moves
timings = games[0].moves[1::2]

# getting information about the game
white = games[0].white
black = games[0].black
result = games[0].result
termination = games[0].termination
time_control = games[0].timecontrol
x = 3
# print(moves)
#print(' '.join(moves))
# print(timings)

# read game with move numbers
game = parser.parse(' '.join(moves), actions=pgn.Actions())
print(game)
'''