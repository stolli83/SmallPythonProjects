#spam = ['apples','bananas','tofu','cats']
spam = ['liebe','lachen','brille','tasse','kerze']

def kommacode(register):
	for i in range(len(register)-2):
		print(register[i], end=', ')
		
	print(register[len(register)-2] + ' and '+ register[-1])
	
kommacode(spam)

