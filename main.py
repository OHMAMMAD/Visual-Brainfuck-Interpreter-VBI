

import time
import sys


def removeSpace(text):
	text = text.split(' ')
	output = ''
	for i in text:
		output += i
	return output

def removeExtraCharecters(text):
	output = ''
	for i in text:
		if i in ['[', ']', ',', '.', '+', '-', '>', '<', 'q']:
			output += i
	return output

def joinListElements(theList):
	output = ''
	for i in theList:
		output += i
	return output

def returnWithoutHash(lineOfText):
	output = ''
	for i in lineOfText:
		if i == '#':
			break
		output += i

	return output


def parser(code):
	arrayOfCode = code.split('\n')
	tempArrayOfCode = []

	for line in arrayOfCode:
		if line != '' and line[0] != '#':
			line = removeSpace(line)  # removing spaces in each line

			line = returnWithoutHash(line) # remove everything after "#" sign
			line = removeExtraCharecters(line) # removing every charecter that is not one of the 8 main charecters


			tempArrayOfCode.append(line)   # the last two lines: destroying lines with nothing on them(filtering them by sending the ones with things on them into another list)


	arrayOfCode = tempArrayOfCode
	if display or showCodeFirst:
		print('\n\n' + joinListElements(arrayOfCode) + '\n\n')
	return joinListElements(arrayOfCode)




class Cell:
	def __init__(self):
		self.value = 0

	def addOne(self):
		if self.value + 1 == 256:
			self.value = 0
		else:
			self.value += 1

	def subtractOne(self):
		if self.value == 0:
			self.value = 255
		else:
			self.value -= 1

	def getInput(self, theInput, thePointer):
		if theInput == '':
			self.value = 10
			return
		if len(theInput) == 1:
			self.value = ord(theInput)
			return
		for char in range(len(theInput)):
			cellListArray[thePointer].getInput(theInput[char], thePointer)
			thePointer += 1

		# cells value is now the ascii value of the inputed string

	def getValue(self):
		return self.value

	def printValue(self):
		output = self.getValue()
		if output > 127:
			output -= 127
		print(output)


def makeSTR(theList, bracket):
	output = ''
	for i in theList:
		if bracket:
			output += f'[{i}] '
		else:
			output += f'{i} '

	return output[:-1]

def showVisuals(areaShowingEachSide):
	visualList = []
	pointerList = []
	indexList = []
	visualPointer = pointer + ((pointer - areaShowingEachSide) * -1)

	start = pointer - areaShowingEachSide
	end = pointer + areaShowingEachSide + 1

	if start < 0:
		end += start * -1 # num is negative
		visualPointer -= start * -1 # num is negative
		start = 0

	if end > len(cellListArray) - 1:
		start += len(cellListArray) - end # num is negative
		visualPointer -= len(cellListArray) - end # num is negative
		end = len(cellListArray)

	counter = 0
	for i in range(start, end):
		visualList.append(str(cellListArray[i].getValue()))
		pointerList.append(len(str(cellListArray[i].getValue())) * ' ' + '  ')
		indexList.append(' ' + (len(visualList[counter])) * ' ' + ' ')
		counter += 1


	indexList[0] = str(start + 1) + ((3 - len(str(start + 1))) * ' ') + ' '
	# adds the number of spaces needed, to push the end number enough to the right
	indexList[len(visualList) - 1] = str(end)
	pointerList[visualPointer] = ' ' + len(str(visualList[visualPointer])) * '^'
	print(makeSTR(visualList, True))
	print(makeSTR(pointerList, False))
	print(makeSTR(indexList, False))


def jumpToEndOfBracket(firstBracketPos):
	#NOTE: PLEASE READ THE COMMENTS FROM THE "jumpToStartOfBracket"
	# FUNCTION THESE TWO ARE THE SAME
	if code == '':
			print('Empty String')
			return
	firstBracketPos += 1
	openBrackets = 0

	for i in range(len(code) - firstBracketPos):
		I = code[i + firstBracketPos]
		#code starts
		if I == ']':
			if openBrackets == 0:
				return i + 1
			openBrackets -= 1
		if I == '[':
			openBrackets += 1

def jumpToStartOfBracket(endBracketPos):
	if code == '':
			print('Empty String')
			return
	openBrackets = 0
	endBracketPos += 1

	for i in range(len(code) - 1 - (len(code) - endBracketPos), -1, -1):
		# line abov will close the area that we are searching in,
		# and makes it so that the search starts from the bracket and
		# not from before it, if we didnt had this, we would start from
		# other brackets so our anwser whould change
		I = code[i - 1]
		#code starts
		if I == '[':
			if openBrackets == 0:
				return endBracketPos - i
				# doing this extra subtraction so we get how far away
				# the other bracket is, not its position
			openBrackets -= 1
		if I == ']':
			openBrackets += 1


pointer = 0
step = 0
cellListArray = [Cell()]


code = ''

amountOfCells = 2 ** 11
userFileName = sys.argv[1]
areaEachSide = 5
display = False
showCodeFirst = False
isDelay = False
onlyParse = False
commandLineCoding = False
for i in range(len(sys.argv)):

	if sys.argv[i] == '-v':
		display = True
		if i + 1 != len(sys.argv):

			if (sys.argv[i + 1])[0] != '-':
				areaEachSide = int(sys.argv[i + 1])

	if sys.argv[i] == '-d':
		print('delay on')
		isDelay = True
		delay = float(sys.argv[i + 1])
		print(delay)

	if sys.argv[i] == '-a':
		amountOfCells = int(sys.argv[i + 1 ])

	if sys.argv[i] == '-p':
		onlyParse = True
		showCodeFirst = True

	if sys.argv[i] == '-i':
		commandLineCoding = True
		code = sys.argv[1]

for i in range(amountOfCells):
	cellListArray.append(Cell())

if not commandLineCoding:
	file = open(userFileName, 'r')
	code = file.read()
	file.close()
	
code = parser(code)


if display:
	showVisuals(areaEachSide)

command = 0
while command < len(code):
	commandSTR = code[command]
	step += 1
	#print(f'the command is: {commandSTR} and is in pos: {command}')
	if onlyParse:

		break
	if commandSTR == '>':
		if pointer + 1 == len(cellListArray):
			pointer = -1
		pointer += 1
	if commandSTR == '<':
		if pointer == 0:
			pointer = len(cellListArray)
		pointer -= 1
	if commandSTR == '+':
		cellListArray[pointer].addOne()
	if commandSTR == '-':
		cellListArray[pointer].subtractOne()
	if commandSTR == '.':
		#print(f'\nCommand: [{commandSTR}], Step: {step}')
		print(chr(cellListArray[pointer].getValue()), end='')
		if display:
			print()
		# prints the ascii of the selected cell
	if commandSTR == ',':
		#print(f'\nCommand: [{commandSTR}], Step: {step}')
		cellListArray[pointer].getInput(input(': '), pointer)
	if commandSTR == '[':
		if cellListArray[pointer].getValue() == 0:
			command += jumpToEndOfBracket(command)
	if commandSTR == ']':
		if cellListArray[pointer].getValue() != 0:
			command -= jumpToStartOfBracket(command) + 1
	if commandSTR == 'q':
		break

	command += 1
	if display:
		if commandSTR not in [',', '.']:
			print()
			print(f'Command: [{commandSTR}], Step: {step}')
			showVisuals(areaEachSide)
	if isDelay:
		time.sleep(delay)


