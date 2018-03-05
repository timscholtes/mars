import random
import copy
## Parent bot class
class Bot(object):
	def __init__(self,loc=[0,0],visibility=10,
		efficiency=10,battery_max=10,storage_max=10,speed=10,pathfinder=None):

		self.loc = loc
		self.pathfinder = pathfinder
		self.visibility = visibility
		self.battery = battery_max
		self.battery_max = battery_max
		self.efficiency = efficiency
		self.storage_max = storage_max
		self.speed = speed
		self.storage = [0]*5


	def base_pathfinder(self,b):
		new_loc = copy.deepcopy(self.loc)
		while new_loc != b:
			if new_loc[0] != b[0]:
				if new_loc[0] < b[0]:
					new_loc[0] += 1
				else:
					new_loc[0] -= 1
			elif new_loc[1] != b[1]:
				if new_loc[1] < b[1]:
					new_loc[1] += 1
				else:
					new_loc[1] -= 1
			yield (new_loc,self.speed)
		return StopIteration
		





	
	def move(self,new_loc):
		self.loc = new_loc


class Miner(Bot):
	def __init__(self,speed_boost=5,drill_depth=5):
		super(Miner, self).__init__()
		self.speed = random.randint(2,5) + speed_boost
		self.drill_depth = drill_depth
		self.storage_max += 10

	def mine(self,mineral):
		if sum(self.storage) < self.storage_max:
			self.storage[mineral] += 1

	def empty(self):
		self.storage = [0]*5


class Scout(Bot):
	def __init__(self,speed_boost):
		super(Scout, self).__init__()
		self.speed = random.randint(5,8) + speed_boost

class Drone_Scout(Bot):
	def __init__(self,speed_boost):
		super(Drone_Scout, self).__init__()
		self.speed = random.randint(8,10) + speed_boost

class Builder(Bot):
	def __init__(self,speed_boost):
		super(Builder, self).__init__()
		self.speed = random.randint(2,5) + speed_boost

class Transporter(Bot):
	def __init__(self,speed_boost):
		super(Transporter, self).__init__()
		self.speed = random.randint(4,7) + speed_boost



