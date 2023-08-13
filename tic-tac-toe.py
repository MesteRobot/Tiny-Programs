def tic_tac_toe(inputs):
	winArray = ['012', '048', '036', '147', '258', '246', '345', '678']
	os = ''
	xs = ''
	for i in range(0,3,1):
		for j in range(0,3,1):
			if inputs[i][j] == 'X':
				xs += str(i*3+j)
			elif inputs[i][j] == 'O':
				os += str(i*3+j)
	for i in range(0,len(winArray),1):
		if containsByChars(winArray[i], os):
			return "Player 2 wins"
		elif containsByChars(winArray[i], xs):
			return "Player 1 wins"
	return "It's a Tie"
				
def containsByChars (first, seccond):
	for i in range(0, len(first),1):
		if not first[i] in seccond:
			return False
	return True


print(tic_tac_toe([
  ["X", "O", "O"],
  ["O", "X", "O"],
  ["O", "#", "X"]
]))
# ➞ "Player 1 wins"


print(tic_tac_toe([
  ["X", "O", "O"],
  ["O", "X", "O"],
  ["X", "#", "O"]
]))
# ➞ "Player 2 wins"


print(tic_tac_toe([
  ["X", "X", "O"],
  ["O", "X", "O"],
  ["X", "O", "#"]
]))
# ➞ "It's a Tie"
