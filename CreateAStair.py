def stair(steps):
	if steps==0 :
		return('___')
	stair = ''
	for i in range(steps):
			stair += ('  ')
	stair += ('_\n')
	for i in range(steps):
		for j in range(steps-1):
			stair += ('  ')
		stair += ('_|')
		steps -= 1
		if steps >= 1:
			stair += '\n'
	return stair


stair(1)
stair(5)
stair(3)
stair(6)
