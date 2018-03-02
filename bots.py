import random

## Parent bot class
class Bot(object):
	def __init__(self,loc,pathfinder,visibility,
		efficiency,battery_max,storage_max):

		self.loc = loc
		self.pathfinder = pathfinder
		self.visibility = visibility
		self.battery = battery_max
		self.battery_max = battery_max
		self.efficiency = efficiency
		self.storage_max = storage_max
		self.storage = [0]*5


class Miner(Bot):
	def __init__(self,speed_boost,drill_depth):
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



