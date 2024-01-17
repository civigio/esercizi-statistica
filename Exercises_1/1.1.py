def divisibility(a):
	k=0
	if (a % 2 == 0):
		print('Divisible by 2')
	else:
		k+=1
	if (a % 3 == 0):
		print('Divisible by 3')
	else:
		k+=1
	if (a % 5 == 0):
		print('Divisible by 5')
	else:
		k+=1
	if (a % 7 == 0):
		print('Divisible by 7')
	else:
		k+=1
	if (k==4):
		print("Number isn't divisible by 2, 3, 5, 7")
		
def divisibility_between_two(a, b):
	if (a % b == 0):
		print('First number is divisible by the second')
	else:
		print('First number is not divisible by the second')
	if (b % a == 0):
		print('Second number is divisible by the first')
	else:
		print('Second number is not divisible by the first')
		
def main():
	a = int(input('Insert first integer: '))
	b = int(input('Insert second integer: '))
	divisibility_between_two(a, b)
	print('\nAbout the first number: ')
	divisibility(a)
	print('\nAbout the second number: ')
	divisibility(b)
	
	
if __name__ == "__main__":
	main()
