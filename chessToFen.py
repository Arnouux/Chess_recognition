import os

if __name__ == '__main__':
	plateau = [['.'] * 8 for i in range(8)]
	
	file = open("table.txt","r")
	for i in range(8):
		for j in range(8):
			plateau[i][j] = file.read(1)

	for i in range(8):
		print(plateau[i])

	fen = ''
	for i in range(8):
		c=0
		for j in range(8):
			
			if plateau[i][j] != '.' :
				if c != 0:
					fen += str(c)
					c=0
				fen += plateau[i][j]
			else:
				c += 1
		if c!=0:
			fen += str(c)
		fen += '/'

	fen = list(fen)
	fen[-1] = " "
	fen = ''.join(fen)
	
	fen += file.read(1)
  
  # basic parameters added
	fen += " KQkq - 0 1"
	print(fen)

	file = open("table.txt","w")
	file.write(fen)
