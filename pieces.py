import board


class piece():
	def __init__(self, color, x, y):
		self.color = color
		self.x  = x
		self.y  = y
		self.current = [x,y]
		self.moved = None
		self.state = "Active"
		self.moves = None
		self.orthogonal = None
		self.diagonal = None
		self.L_shaped = None

	def set_current(self, coordinate):
		self.current = [self.x,self.y]

	def compile(self):
		arr = []
		if self.orthogonal != None:
			for o in self.orthogonal:
				arr.append(o)

		if self.diagonal != None:
			for d in self.diagonal:
				arr.append(d)

		if self.L_shaped != None:
			for l in self.L_shaped:
				arr.append(l)

		self.moves = arr

	def check_surrounding(self):
		pass

	def check_orthogonal(self, chess_board):
		x = self.x
		y = self.y

		pin_1 = abs(0-x)
		pin_2 = abs(7-x)
		pin_3 = abs(0-y)
		pin_4 = abs(7-y)

		pins = [pin_1, pin_2, pin_3, pin_4]
		moves = []
		
		#pin_1 is for movement 'up'
		for i in range(1,pin_1+1):
			piece = chess_board.board[x-i][y]
			if piece == 0:
				moves.append([x-i,y])
			elif piece.color != self.color:
				moves.append([x-i,y])
				break
			else:
				break

		for j in range(1, pin_2 + 1):
			piece = chess_board.board[x+j][y]
			if piece == 0:
				moves.append([x+j,y])
			elif piece.color != self.color:
				moves.append([x+j,y])
				break
			else:
				break

		for k in range(1, pin_3 + 1):
			piece = chess_board.board[x][y-k]
			if piece == 0:
				moves.append([x,y-k])
			elif piece.color != self.color:
				moves.append([x,y-k])
				break
			else:
				break

		for p in range(1, pin_4 + 1):
			piece = chess_board.board[x][y+p]
			if piece == 0:
				moves.append([x,y+p])
			elif piece.color != self.color:
				moves.append([x,y+p])
				break
			else:
				break

		self.orthogonal = moves		

	def check_diagonal(self, chess_board):
		x = self.x
		y = self.y

		pin_1 = min(abs(0-x),abs(0-y))
		pin_2 = min(abs(0-x),abs(7-y))
		pin_3 = min(abs(7-x),abs(0-y))
		pin_4 = min(abs(7-x),abs(7-y))

		moves = []

		for i in range(1,pin_1+1):
			piece = chess_board.board[x-i][y-i]
			if piece == 0:
				moves.append([x-i,y-i])
			elif piece.color != self.color:
				moves.append([x-i,y-i])
				break
			else:
				break
				
		for i in range(1,pin_2+1):
			piece = chess_board.board[x-i][y+i]
			if piece == 0:
				moves.append([x-i,y+i])
			elif piece.color != self.color:
				moves.append([x-i,y+i])
				break
			else:
				break

		for i in range(1,pin_3+1):
			piece = chess_board.board[x+i][y-i]
			if piece == 0:
				moves.append([x+i,y-i])
			elif piece.color != self.color:
				moves.append([x+i,y-i])
				break
			else:
				break

		for i in range(1,pin_4+1):
			piece = chess_board.board[x+i][y+i]
			if piece == 0:
				moves.append([x+i,y+i])
			elif piece.color != self.color:
				moves.append([x+i,y+i])
				break
			else:
				break

		self.diagonal = moves

	def check_L_shaped(self, chess_board):
		x = self.x
		y = self.y
		moves = []

		if x - 2 >= 0 and y - 1 >= 0:
			piece = chess_board.board[x-2][y-1]
			if piece == 0 or piece.color != self.color:
				moves.append([x-2,y-1])
		
		if x - 1 >= 0 and y - 2 >= 0:
			piece = chess_board.board[x-1][y-2]
			if piece == 0 or piece.color != self.color:
				moves.append([x-1,y-2])

		if x - 2 >= 0 and y + 1 <= 7:
			piece = chess_board.board[x-2][y+1]
			if piece == 0 or piece.color != self.color:
				moves.append([x-2,y+1])

		if x - 1 >= 0 and y + 2 <= 7:
			piece = chess_board.board[x-1][y+2]
			if piece == 0 or piece.color != self.color:
				moves.append([x-1,y+2])

		if x + 2 <= 7 and y - 1 >= 0:
			piece = chess_board.board[x+2][y-1]
			if piece == 0 or piece.color != self.color:
				moves.append([x+2,y-1])
		
		if x + 1 <= 7 and y - 2 >= 0:
			piece = chess_board.board[x+1][y-2]
			if piece == 0 or piece.color != self.color:
				moves.append([x+1,y-2])

		if x + 2 <= 7 and y + 1 <= 7:
			piece = chess_board.board[x+2][y+1]
			if piece == 0 or piece.color != self.color:
				moves.append([x+2,y+1])

		if x + 1 <= 7 and y + 2 <= 7:
			piece = chess_board.board[x+1][y+2]
			if piece == 0 or piece.color != self.color:
				moves.append([x+1,y+2])


		self.L_shaped = moves

	def move(self,chess_board, dest):
		self.check_surrounding(chess_board)
		moves, x, y = self.moves, self.x, self.y
		coordinate, dest_x, dest_y = dest, dest[0], dest[1]
		name = chess_board.board[x][y]

		if coordinate in moves:
			chess_board.board[x][y] = 0
			piece = chess_board.board[dest_x][dest_y]
			if piece == 0:
				self.movement(dest_x,dest_y,name,chess_board)
			elif piece != 0:
				piece.remove_from_board(chess_board)
				self.movement(dest_x,dest_y,name,chess_board)
			else:
				print('Invalid Movement')

		self.orthogonal = self.diagonal = self.L_shaped = self.moves = None

	def remove_from_board(self, chess_board):
		chess_board.board[self.x][self.y] = 0
		self.x = None
		self.y = None
		self.state = None

	def movement(self, x, y, name, chess_board):
		self.x = x
		self.y = y
		self.set_current([x,y])
		chess_board.board[x][y] = name 

		if self.moved ==None:
			self.moved = True


class pawn(piece):
	def check_surrounding(self, chess_board):
		x = self.x
		y = self.y
		moves = []


		if self.color == 'white':
			if x-1>=0:
				piece = chess_board.board[x-1][y]
				if piece == 0:
					moves.append([x-1,y])

			if x-2>=0 and self.moved==None:
				piece = chess_board.board[x-2][y]
				if piece == 0:
					moves.append([x-2,y])

			if x-1>=0 and y-1>=0:
				piece = chess_board.board[x-1][y-1]
				if piece!=0:
					if piece.color !=self.color:
						moves.append([x-1,y-1])

			if x-1>=0 and y+1<=7:
				piece = chess_board.board[x-1][y+1]
				if piece!=0:
					if piece.color!=self.color:
						moves.append([x-1,y+1])
				
			self.moves = moves

		elif self.color == 'black':
			if x+1<=7:
				piece = chess_board.board[x+1][y]
				if piece == 0:
					moves.append([x+1,y])

			if x+2<=7 and self.moved==None:
				piece = chess_board.board[x+2][y]
				if piece == 0:
					moves.append([x+2,y])

			if x+1<=7 and y+1<=7:
				piece = chess_board.board[x+1][y+1]
				if piece!=0:
					if piece.color !=self.color:
						moves.append([x+1,y+1])

			if x+1<=7 and y-1>=0:
				piece = chess_board.board[x+1][y-1]
				if piece!=0:
					if piece.color!=self.color:
						moves.append([x+1,y-1])
				
			self.moves = moves			


class rook(piece):
	def check_surrounding(self, chess_board):
		self.check_orthogonal(chess_board)
		self.compile()

class bishop(piece):
	def check_surrounding(self, chess_board):
		self.check_diagonal(chess_board)
		self.compile()

class knight(piece):
	def check_surrounding(self, chess_board):
		self.check_L_shaped(chess_board)
		self.compile()

class queen(piece):
	def check_surrounding(self, chess_board):
		self.check_orthogonal(chess_board)
		self.check_diagonal(chess_board)
		self.compile()

class king(piece):
	def __init__(self, color, x, y):
		self.in_check = False
		super().__init__(color, x, y)

	def check_surrounding(self, chess_board):
		x = self.x
		y = self.y
		moves = []

		if x-1>=0:
			piece = chess_board.board[x-1][y]
			if piece == 0 or piece.color != self.color:
				moves.append([x-1,y])
		
		if x+1<=7:
			piece = chess_board.board[x+1][y]
			if piece == 0 or piece.color!=self.color:
				moves.append([x+1,y])

		if y-1>=0:
			piece = chess_board.board[x][y-1]
			if piece== 0 or piece.color!=self.color:
				moves.append([x,y-1])

		if y+1<=7:
			piece = chess_board.board[x][y+1]
			if piece== 0 or piece.color!=self.color:
				moves.append([x,y+1])

		if x-1>=0 and y-1>=0:
			piece = chess_board.board[x-1][y-1]
			if piece== 0 or piece.color!=self.color:
				moves.append([x-1,y-1])

		if x-1>=0 and y+1<=7:
			piece = chess_board.board[x-1][y+1]
			if piece== 0 or piece.color!=self.color:
				moves.append([x-1,y+1])

		if x+1<=7 and y-1>=0:
			piece = chess_board.board[x+1][y-1]
			if piece== 0 or piece.color!=self.color:
				moves.append([x+1,y-1])

		if x+1<=7 and y+1<=7:
			piece = chess_board.board[x+1][y+1]
			if piece== 0 or piece.color!=self.color:
				moves.append([x+1,y+1])

		self.moves = moves

	def generate_point(self, chess_board):
		self.check_orthogonal(chess_board)
		self.check_diagonal(chess_board)
		self.check_L_shaped(chess_board)
		orthogonal, diagonal, L_shaped = self.orthogonal, self.diagonal, self.L_shaped
		moves = orthogonal,diagonal,L_shaped
		self.risks = [x for x in moves if x != None]

	def check_detection(self, chess_board):
		self.generate_point(chess_board)
		curr_x = self.x
		curr_y = self.y
		risks = self.risks
		king_space = [curr_x, curr_y]
		threats = []

		for risk in risks:
			x = risk[0]
			y = risk[1]
			point = chess_board.board[x][y]

			if point != 0:
				if point.color!=self.color:
					threats.append(point)

		for threat in threats:
			threat.check_surrounding()
			if king_space in threat.moves:
				self.in_check = True
				break
			else:
				continue

#initialize all pieces

black_pawn_1 = pawn('black', 1, 0)
black_pawn_2 = pawn('black', 1, 1)
black_pawn_3 = pawn('black', 1, 2)
black_pawn_4 = pawn('black', 1, 3)
black_pawn_5 = pawn('black', 1, 4)
black_pawn_6 = pawn('black', 1, 5)
black_pawn_7 = pawn('black', 1, 6)
black_pawn_8 = pawn('black', 1, 7)
black_rook_1 = rook('black', 0, 0)
black_rook_2 = rook('black', 0, 7)
black_knight_1 = knight('black', 0, 1)
black_knight_2 = knight('black', 0, 6)
black_bishop_1 = bishop('black', 0, 2)
black_bishop_2 = bishop('black', 0, 5)
black_queen = queen('black', 0, 3)
black_king = king('black', 0, 4)

white_pawn_1 = pawn('white', 6, 0)
white_pawn_2 = pawn('white', 6, 1)
white_pawn_3 = pawn('white', 6, 2)
white_pawn_4 = pawn('white', 6, 3)
white_pawn_5 = pawn('white', 6, 4)
white_pawn_6 = pawn('white', 6, 5)
white_pawn_7 = pawn('white', 6, 6)
white_pawn_8 = pawn('white', 6, 7)
white_rook_1 = rook('white', 7, 0)
white_rook_2 = rook('white', 7, 7)
white_knight_1 = knight('white', 7, 1)
white_knight_2 = knight('white', 7, 6)
white_bishop_1 = bishop('white', 7 , 2)
white_bishop_2 = bishop('white', 7 , 5)
white_queen = queen('white', 7, 3)
white_king = king('white', 7, 4)


all_pieces = [white_pawn_1, white_pawn_2, white_pawn_3, white_pawn_4, white_pawn_5, white_pawn_6, white_pawn_7, white_pawn_8,
white_rook_1, white_knight_1, white_bishop_1, white_queen, white_king, white_bishop_2, white_knight_2, white_rook_2,
black_pawn_1, black_pawn_2, black_pawn_3, black_pawn_4, black_pawn_5, black_pawn_6, black_pawn_7, black_pawn_8,
black_rook_1, black_knight_1, black_bishop_1, black_queen, black_king, black_bishop_2, black_knight_2, black_rook_2]


if __name__ == '__main__':
	chess_board = board.board()
	chess_board.fill_board(all_pieces)
	white_knight_1.move(chess_board, [5,2])
	white_knight_1.check_surrounding(chess_board)
	print(white_knight_1.moves)
	piece = chess_board.board[6][4]
	print(piece.color != white_knight_1.color)

