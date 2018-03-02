
import numpy as np

class Maps:

	def __init__(self,N,depth):
		self.terrain = np.ones([N,N,depth])
		self.mask = np.zeros([N,N],depth)
		self.units = np.zeros([N,N])
		self.buildings = np.zeros([N,N])

	def print_map(self,filt,level):
		pass
