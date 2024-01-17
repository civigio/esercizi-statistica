import math

def solutions(a, b, c):
	delta = b*b-4*a*c
	if(delta<0):
		print('There are no solutions')
	elif(delta==0):
		solution = (-b)/(2*a)
		print('x1 = x2 = ', solution)
	else:
		solution1 = ((-b)+math.sqrt(delta))/(2*a)
		solution2 = ((-b)-math.sqrt(delta))/(2*a)
		print('x1 = ', solution1)
		print('x2 s= ', solution2)


def main():
	print('Function type ax^2+bx+c=0')
	a = int(input('Insert a: '))
	b = int(input('Insert b: '))
	c = int(input('Insert c: '))
	solutions(a, b, c)
	

if __name__ == "__main__":
	main()
