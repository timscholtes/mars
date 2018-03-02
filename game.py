import maps
import bots


class Game:

	def __init__(self,N,depth):
		
		self.bots = {}
		self.buildings = {}
		self.maps = maps.Maps(N,depth)
		self.schedule = []
		self.score = 0
		self.resources = [100]*5
		self.year = 2025.0
		self.season = (self.year % 1) * 4
		self.t_per_season = 100

		
	def add_actions(self,action_lst):
		self.schedule.append(action_lst)

	def execute_turn(self,verbose=0):
		pass

	def move_bot(self,bot_id,new_loc):
		this_bot = self.bots[bot_id[0]][bot_id[1]].loc
		this_bot.loc = new_loc
		self.uncover(new_loc[0],new_loc[1],this_bot.visibility)

	def uncover(self,i,j,vis_range):
		self.maps.mask[i-vis_range:i+vis_range,
		j-vis_range:j+vis_range] = 1











