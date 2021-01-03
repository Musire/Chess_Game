#Gneerate the Board
class board():
	def __init__(self):
		self.board = [[0 for i in range(8)] for j in range(8)]


	def fill_board(self, arr):
		for piece in arr:
			self.board[piece.x][piece.y] = piece
		

	def print_board(self):
		for row in self.board:
			print(row)

if __name__ == '__main__':
	apple = 0