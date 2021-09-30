

from io import open_code
import sys

def parse(cd):
	out = ''
	for char in range(len(cd)):
		if cd[char] in ['[', '<', '+', ',', '.', '-', '>', ']', 'q']:
			out += cd[char]
	print(out + '\n')
	return out

def show():

	startPoint = pointer - amountEachSide
	endPoint = pointer + amountEachSide + 1
	visPointer = pointer - startPoint

	if pointer < amountEachSide:
		endPoint -= startPoint
		startPoint = 0
		visPointer = pointer
	if pointer >= len(arr) - amountEachSide:
		visPointer += endPoint - len(arr)
		startPoint -= endPoint - len(arr)
		endPoint = len(arr)


	cellArr = []
	spacesAmount = 0

	for i in range(startPoint, endPoint):
		cellArr.append(str(arr[i]))

	for i in range(visPointer):
		spacesAmount += 2 + len(str(cellArr[i]))

	arrStr = "  ".join(cellArr)
	print(f'{arrStr}    p: {pointer}    range: {startPoint}  {endPoint -1} {stack} {cm}    {code[cmIndex][1]}')
	print((spacesAmount) * ' ' + '^')


def get_close_bracket(cd, loc):
	if cd[loc][0] != '[':
		print('ERROR')
		return
	
	bracksCount = 0
	index = loc + 1
	while index < len(cd):
		if cd[index][0] == '[':
			bracksCount -=-1

		if cd[index][0] == ']':
			if bracksCount == 0:
				return index
			else:
				bracksCount -= 1

		index -=-1


def find_other_brack(loc):
	for bracks in range(len(openBracksArr)):
		sp = openBracksArr[bracks].split(':')
		for item in range(len(sp)):
			if int(sp[item]) == loc:
				if item == 1:
					return int(sp[0])
				if item == 0:
					return int(sp[1])

def check_order(cd, order=['>', '+', '<', '-']):
	boolOrd = True
	boolSet = True

	for i in range(len(cd)):
		if cd[i][0] != order[i]:
			boolOrd = False
	if cd[-1][1] != 1 or (cd[0][1] != cd[2][1]):
		# if "-" == 1, and number of ">" and "<" were simular, return True
		boolSet = False
	if boolSet and boolOrd:
		return [True, cd[0][1], cd[1][1]]
	return [False, boolSet]

def is_mult(cd):
	order = ['>', '+', '<', '-']

	if len(cd) != len(order):
		return [False]

	if check_order(cd)[0]:
		return check_order(cd)

	if not check_order(cd)[1]:
		return [False]


	if check_order(cd, ['<', '+', '>', '-'])[0]:
		return [True, cd[0][1] * -1, cd[1][1]]

	if check_order(cd, ['>', '-', '<', '-'])[0]:
		return [True, cd[0][1], cd[1][1] * -1]

	if check_order(cd, ['<', '-', '>', '-'])[0]:
		return [True, cd[0][1] * -1, cd[1][1] * -1]
	return [False]
	

def find_pattern(cd):
	if cd == [['-', 1]]:
		return [[1, 0]]
	elif is_mult(cd)[0]:
		res = is_mult(cd)
		return [[2, res[1], res[2]]]
	return [['[', 1]] + cd + [[']', 1]]

def opt(cd):
	out = [[0, 0]]
	for command in range(len(cd)):
		if cd[command] != out[-1][0]:
			out.append([cd[command], 1])
		elif  cd[command] == out[-1][0] and (cd[command] == '[' or cd[command] == ']'):
			out.append([cd[command], 1])
		else:
			out[-1][1] += 1
	out.append([0])

	command = 0
	while command < len(out):
		if out[command][0] == '[':
			out[command:get_close_bracket(out, command) + 1] = find_pattern(out[command + 1:get_close_bracket(out, command)])
		command -=- 1

	if out[-1] != [0]:
		out.append(0)

	out = out[1:-1]
	return out

isVisuals = False
amountEachSide = 4
parseOnly = False
for i in range(2, len(sys.argv)):
	if sys.argv[i] == '-v':
		isVisuals = True
		if (i != len(sys.argv)-1) and (sys.argv[i+1][0] != '-'): 
			# if user added amountEachSide
			amountEachSide = int(sys.argv[i+1])
	elif sys.argv[i] == '-p':
		parseOnly = True


# open file
filePath = sys.argv[1]
f = open(filePath, 'r')
code = f.read()
f.close()

# parse and optimize code
code = parse(code)
code = opt(code)
openBracksArr = []


for char in range(len(code)):
	if code[char][0] == '[':
		openBracksArr.append(str(char) + ':' + str(get_close_bracket(code, char)))

# make arr
arrSize = 2 ** 12
arr = []
for i in range(arrSize):
	arr.append(0)

 
# init vars
step = 0
cmIndex = 0
lenCode = len(code)
lenArr = len(arr)
pointer = 0
stack = []
#print('\n', code)
print('Run Time!')
while cmIndex < lenCode:
	cm = code[cmIndex][0]
	pointArr = arr[pointer]

	if cm == 'q':
		break

	if parseOnly:
		break

	if cm == '+':
		pointArr += code[cmIndex][1]
		if pointArr > 255:
			pointArr -= 256
	elif cm == '-':
		pointArr -= code[cmIndex][1]
		if pointArr < 0:
			pointArr += 256
	elif cm == '>':
		pointer += code[cmIndex][1]
		if pointer >= lenArr:
			print('ya cant\' wrap around!')
			break
		pointArr = arr[pointer]
	elif cm == '<':
		pointer -= code[cmIndex][1]
		if pointer < 0:
			print('ya can\'t wrap around!')
			break
		pointArr = arr[pointer]
	elif cm == ',':
		inp = input(': ')
		if inp == '':
			pointArr = 10
		else:
			pointArr = ord(inp[0])
	elif cm == '.':
		print(chr(pointArr), end="")
	elif cm == '[':
		if pointArr > 0:
			stack.append(cmIndex)
		else:
			cmIndex = find_other_brack(cmIndex)
	elif cm == ']':
		if pointArr > 0:
			cmIndex = stack[-1]
		else:
			stack = stack[0:-1]
	elif cm == 1:
		pointArr = 0
	elif cm == 2:
		arr[pointer + code[cmIndex][1]] += pointArr * code[cmIndex][2]
		
		
		if arr[pointer + code[cmIndex][1]] > 255:
			arr[pointer + code[cmIndex][1]] -= 256
		if arr[pointer + code[cmIndex][1]] < 0:
			arr[pointer + code[cmIndex][1]] += 256
		
		
		arr[pointer] = 0
		pointArr = arr[pointer]


	arr[pointer] = pointArr
	#print(f'{arr}   pointer: {pointer}   {stack}    {cm}')
	if isVisuals:
		show()
	step -=- 1
	cmIndex -=- 1

