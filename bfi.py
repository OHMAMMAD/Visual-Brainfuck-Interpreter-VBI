

import sys
import time
from typing import Optional
file_name = sys.argv[1]

f = open(file_name, 'r')
code = f.read()
f.close()
lenCode = len(code)

arr = []
for i in range(2 ** 13):
	arr.append(0)
pointer = 0

def find_closing(inp, loc):
	outputLoc = 0
	if inp[loc] != '[':
		print('ERROR WHILE FINDING BRACKET')
		return

	i = loc
	lenInp = len(inp)
	bracketsInWay = -1
	while i < lenInp:
		
		if inp[i] == '[':
			bracketsInWay += 1
		elif inp[i] == ']':
			if bracketsInWay == 0:
				return i
			elif bracketsInWay > 0:
				bracketsInWay -= 1

		i += 1
	print('mis matching brackets')
	exit() 


openBracks = []
closeBracks = []

for i in range(lenCode):
	if code[i] == '[':
		openBracks.append(i)
		closeBracks.append(find_closing(code, i))

stack = []
step = 0
cmIndex = 0
brackIndex = -1
while cmIndex < lenCode:
	pointArr = arr[pointer]
	cmStr = code[cmIndex]

	# remmember to update pointArr

	if cmStr == 'q':
		exit()

	if cmStr == '+':
		if arr[pointer] == 255:
			arr[pointer] = -1
		arr[pointer] += 1
	elif cmStr == '-':
		if arr[pointer] == 0:
			arr[pointer] = 256
		arr[pointer] -= 1
	elif cmStr == '>' and pointer != (lenCode - 1):
		pointer += 1
		#arr[pointer] = arr[pointer]
	elif cmStr == '<' and pointer != 0:
		pointer -= 1
		#arr[pointer] = arr[pointer]
	elif cmStr == ',':
		ui = input(': ')
		if ui == '':
			arr[pointer] = 10
		else:
			arr[pointer] = ord(ui[0])
		#arr[pointer] = arr[pointer]
	elif cmStr == '.':
		print(chr(arr[pointer]), end='')
	elif cmStr == '[':
		if arr[pointer] == 0:
			cmIndex = find_closing(code, cmIndex)
		else:
			stack.append(cmIndex)
	elif cmStr == ']':
		if arr[pointer] > 0:
			cmIndex = stack[-1]
		else:
			stack = stack[0:-1]
	#arr[pointer] = pointArr

	#print(f'command: \"{cmStr}\"    step: {step}     index: {cmIndex}')
	#print(' ' + pointer * '   ' + '^')
	#print()
	cmIndex += 1
	step += 1

