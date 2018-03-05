import maps
import bots
import collections

class Game:

	def __init__(self,N,depth):
		
		self.bots = {}
		self.buildings = {}
		self.maps = maps.Maps(N,depth)
		self.schedule = collections.defaultdict(collections.deque)
		self.score = 0
		self.resources = [100]*5
		self.year = 2025.0
		self.season = (self.year % 1) * 4
		self.t_per_season = 100

		
	def add_action(self,bot_id,action):
		self.schedule[bot_id].appendleft(action)

	def execute_turn(self,verbose=0):
		"""
		Scheduling is important! Trying to avoid race conditions.
		Each element in the schedule is a generator (a super-task)
		this super-task creates sub tasks that get assigned onto a heap
		the heap is indexed by time that it can be completed, as I want to include
		delays to make some actions take longer.

		The control flow is to :
		1. take the intial actions from all active super-tasks
		2. heapify, with time schedule as the min-key
		3. while heap and t < 100:
			a. extract-min from the heap.
			b. do the task
				i. this task may end with adding a new task to the heap.
					eg. move a-b may end with req to move b-c next.
				ii. if the super task has ended, then pop it and 
					enqueue the new generator, get next from this
			c. t += 1
		"""

	def uncover(self,i,j,vis_range):
		self.maps.mask[i-vis_range:i+vis_range,
		j-vis_range:j+vis_range] = 1


if __name__ == '__main__':
	game = Game(20,3)
	game.bots = {
	'm1':bots.Miner(),
	'm2':bots.Miner(),
	'm3':bots.Miner()}



	game.add_action('m1',game.bots['m1'].base_pathfinder([10,10]))
	game.add_action('m2',game.bots['m2'].base_pathfinder([-10,-10]))
	print(game.schedule['m1'])
	print(game.schedule['m3'])

	for k in range(30):
		print(next(game.schedule['m1'][len(game.schedule['m1'])-1]))






