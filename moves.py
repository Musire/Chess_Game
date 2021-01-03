class move():
	def __init__(self):
		self.move_queue = []
		self.turn_queue = []

	
	@property
	def current_turn(self):

		size = len(self.turn_queue)
		if size == 0:
			return 'white'
		elif size >0:
			if self.turn_queue[size-1] == 'black':
				return 'white'
			else:
				return 'black'


if __name__ == '__main__':
	central_move = move()
	print(central_move.current_turn)
	central_move.turn_queue.append('white')
	print(central_move.current_turn)