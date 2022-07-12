### Taken from https://chess.stackexchange.com/questions/18182/stockfish-evaluation-of-a-position-from-pgn god bless him

import chess
import chess.pgn
import sys

arguments = sys.argv
pgnfilename = str('tester.pgn')

#Read pgn file:
with open(pgnfilename) as f:
    game = chess.pgn.read_game(f)

#Go to the end of the game and create a chess.Board() from it:
#game = game.end()
board = game.board()
print(game)
#So if you want, here's also your PGN to FEN conversion:
print('FEN of the last position of the game: ', board.fen())

#or if you want to loop over all game nodes:
x=True
while x:
    try:
        node = game.variations[0]
        board = game.board() #print the board if you want, to make sure
        game = node         

        #Now we have our board ready, load your engine:
        #handler = chess.uci.InfoHandler()
        engine = chess.engine.SimpleEngine.popen_uci("C:\\Users\\viksp\\Documents\\Folder_of_Folders\\copyingaimchess\\chess_grind\\stockfish-windows-amd64.exe")#give correct address of your engine here
        #engine.info_handlers.append(handler)

        #give your position to the engine:
        info = engine.analyse(board, chess.engine.Limit(time=0.1))
        print("Score:", info["score"])
    except:
        x=False
        print("done")
print("done")