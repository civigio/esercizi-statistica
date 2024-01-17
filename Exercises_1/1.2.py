import math

def pythagorean(a, b):
	c = math.sqrt(a*a + b*b)
	return c
	
def type_triangle(a, b, c):
	k = max(a, b, c)
	if (k==a):
		v = pythagorean(b, c)
	elif (k==b):
		v = pythagorean(a, c)
	else:
		v = pythagorean(a, b)
		
	if(k>v):
		print('Triangle is octusangle')
	elif(k==v):
		print('Triangle is rectangle')
	else:
		print('Triangle is acutangle')
	
def main():
	a = int(input('Side a:'))
	b = int(input('Side b:'))
	c = int(input('Side c:'))
	type_triangle(a, b, c)
	
if __name__ == "__main__":
	main()
