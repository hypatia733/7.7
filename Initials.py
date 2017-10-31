# Accept string, return initials


def Initials(string):
	initialsarray = []
	splitstring = string.split(' ')
	for i in splitstring:
		if i[0].islower():
			initialsarray.append(i[0].upper())
		else:
			initialsarray.append(i[0])
	finalarray = []
	for i in initialsarray:
		temparray = []
		temparray.append(i)
		temparray.append('.')
		tempstring = str(temparray[0] + temparray[1])
		finalarray.append(tempstring)
	for i in range(0, len(finalarray)):
		print(finalarray[i], end='')
	return None

input = input("Enter names to initial:\n")

Initials(input)
