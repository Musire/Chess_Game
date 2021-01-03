import pieces

class player():
	def __init__(self, color):
		self.color = color

white_player = player('white')
black_player = player('black')


if __name__ == '__main__':
	print(white_player.color)
	print(black_player.color)