def term(a, b):
	c=a+b
	return(c)
	
def main():
	print('Up to which index do you want to calculate the Fibonacci sequence?')
	index = int(input())
	i=2
	value = 0
	fibonacci = []
	if(index>=1):
		fibonacci.append(1)
	if(index>=2):
		fibonacci.append(1)
	while i<index:
		value = fibonacci[i-1] + fibonacci[i-2]
		fibonacci.append(value)
		i+=1
	
	print(fibonacci)
	
if __name__ == "__main__":
	main()
