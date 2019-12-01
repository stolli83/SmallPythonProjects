def collatz(numb):
 if numb % 2: #ungrade
    return 3 * numb +1
 else: #grade
    return numb // 2

while True:
	print('Enter number: ')
	try:
		number = int(input())
		break
	except ValueError:
			print('Error: Invalid argument')
			print('Please try again')
			continue


while number != 1:
 print(str(collatz(number)))
 number = collatz(number)

