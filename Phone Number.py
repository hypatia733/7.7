def Numberize(phonenumber):
	if phonenumber[3] != '-' or phonenumber[7] != '-' or len(phonenumber) != 12:
		print("The number is in an incorrect format. Enter as: XXX-XXX-XXXX")
		return None
	rawArray = []
	i = 0
	while i < len(phonenumber):
		rawArray.append(phonenumber[i])
		i += 1
	rawArray.remove('-')
	rawArray.remove('-') 
	# ^ Do it twice for both '-'s - theres probably a more eloquent way but... this works
	upperArray = makeUpper(rawArray)
	finalArray = []
	for i in upperArray:
		x = lettersToNumbers(i)
		finalArray.append(x)
	finalArray.insert(3, '-')
	finalArray.insert(7, '-')
	for i in finalArray:
		 print(i, end='')


def makeUpper(array):
	upperArray = []
	for i in array:
		if i.isalpha:
			if i.islower:
				upperArray.append(i.upper())
			else:
				upperArray.append(i)
		else:
			upperArray.append(i)
	return upperArray
	
	
def lettersToNumbers(str):
	if str.isalpha:
		if str == 'A' or str == 'B' or str == 'C':
			str = '2'
		elif str == 'D' or str == 'E' or str == 'F':
			str = '3'
		elif str == 'G' or str == 'H' or str == 'I':
			str = '4'
		elif str == 'J' or str == 'K' or str == 'L':
			str = '5'
		elif str == 'M' or str == 'N' or str == 'O':
			str = '6'
		elif str == 'P' or str == 'Q' or str == 'R' or str == 'S':
			str = '7'
		elif str == 'T' or str == 'U' or str == 'V':
			str = '8'
		elif str == 'W' or str == 'X' or str == 'Y' or str == 'Z':
			str = '9'
	return str

input = str(input("Enter number in format: XXX-XXX-XXXX\n"))

Numberize(input)

