from stockfishpy.stockfishpy import *

file = open("table.txt","r")
fen = file.read()
file.close()

#starting fen
#fen = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1"

chessEngine = Engine("stockfish-10-linux/Linux/stockfish_10_x64", param={'Threads':2, 'Ponder': 'true'})

#print chessEngine.uci()

chessEngine.ucinewgame()

chessEngine.setposition(fen)

move = chessEngine.bestmove()
print move['bestmove']

file = open("table.txt","w")
file.write(move['bestmove'])
file.close()
