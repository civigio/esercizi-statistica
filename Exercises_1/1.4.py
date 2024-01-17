def term(a, b):
	c=a+b
	return(c)
	
def main():
	print('Up to which index do you want to calculate the Fibonacci sequence?')
	index = int(input())
	i = 3
	fibonacci = {}
	if(index>=1):
		fibonacci[1]=1
	if(index>=2):
		fibonacci[2]=1
	for i in range (3, index+1):
		value = fibonacci[i-1] + fibonacci[i-2]
		fibonacci[i] = value
	
	print(fibonacci)
	
if __name__ == "__main__":
	main()
