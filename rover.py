class Rover:
	def BFS(self,Lx,Ly,Z,Tc,Tx,Ty,Map):
		print('\nLander Location',Lx,Ly)
		print('\nElevation Threshold',Z)
		print('\nNo of Targets',Tc)
		print('\nTarget Location',Tx,Ty)
		print('\nMap',Map)
		Queue = [[Lx+1,Ly+1]]
		#print('\nQueue Initiated...',Queue)
		Visited= []
		Parents = dict()
		while Queue!=[]:
			node = Queue.pop(0)
			#print('\n Popped Node',node)
			if node[0]==Tx+1 and node[1]==Ty+1:
				key = str(Tx+1)+str(Ty+1)
				lsite=str(Lx+1)+str(Ly+1)
				return self.getPath(key,lsite,Parents)
			else:
				children = self.getchildren(node[0],node[1])
				for child in children:
					child_z = Map[child[0]][child[1]]
					node_z = Map[node[0]][node[1]]
					# print('\nZ',child_z-node_z)
					if child_z-node_z <= Z:
						if child not in Visited:
							# print('\n Child Not Visited',child)
							if child not in Queue:
								#print('child Not in Queue',Queue)
								Queue.append(child)
							Parents[str(child[0])+str(child[1])]=str(node[0])+str(node[1])
				if node not in Visited:
					Visited.append(node)
				# print('\n Visited List', Visited)
				# print('\n Queue',Queue)
				# print('\n Parents',Parents)

		return 'False'

	def getchildren(self,x,y):
		children = []
		children.append([x-1,y-1])
		children.append([x-1,y])
		children.append([x,y-1])
		children.append([x+1,y+1])
		children.append([x+1,y])
		children.append([x,y+1])
		children.append([x-1,y+1])
		children.append([x+1,y-1])
		return children

	def getPath(self,key,lsite,Parents):
		Path = ''
		while key!=lsite:
			Path+=str(int(key[0])-1)+','+str(int(key[1])-1)+' '
			key = Parents[key]
		Path+=str(int(key[0])-1)+','+str(int(key[1])-1)
		#print('Path',Path[::-1])
		return Path[::-1]


	def USC():
		pass
	def A_star():
		pass


if __name__== "__main__":
	# First 6 lines are fixed
	'''

	1 --> Algo
	2 --> Column and row
	3 --> Landing Site Location
	4 --> Threshold Eleveation
	5 --> No of Target Sites
	6 --> Target Site Location
	7 onwards --> Map of the area
'''
	filepath = 'input.txt'
	data = []
	with open(filepath) as fp:
		line = fp.readline()
		while line:
			data.append(line.strip())
			line = fp.readline()
	####################################################		
	print('Readind Data ....')
	Algo = data[0]
	Column = int(data[1][0])
	Row = int(data[1][2])
	Lx = int(data[2][2])
	Ly = int(data[2][0])
	Z = int(data[3][0])
	Tc = int(data[4][0])
	Targets = []
	Map = [[float('inf') for i in range(0,Column+2)] for i in range(0,Row+2)]
	for i in range(5,5+Tc):
		Tx = int(data[i][2])
		Ty = int(data[i][0])
		Targets.append([Tx,Ty])
	print('\n Algo',Algo)
	print('\nTargets',Targets)
	####################################################
	for i in range(5+Tc,5+Tc+Row):
		s = data[i].split(' ')
		for j in range(0,Column):
			Map[i-4-Tc][j+1]=int(s[j])
	####################################################
	rover = Rover()
	if Algo=='BFS':
		for i in range(0,len(Targets)):
			Tx = Targets[i][0]
			Ty = Targets[i][1]
			path = rover.BFS(Lx=Lx,Ly=Ly,Z=Z,Tc=Tc,Tx=Tx,Ty=Ty,Map=Map)
			f = open('output.txt',"a")
			f.write(path+'\n')
			f.close()
	# elif Algo=='USC':
	# 	USC()
	# elif Algo=='A*':
	# 	A_star()
