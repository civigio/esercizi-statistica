import math

def recursive_minimum_point(f, xMin, xMax, precision = 0.0001):
    r = ((math.sqrt(5)-1)*0.5)

    if ((xMax - xMin)<precision): return ((xMax + xMin)*0.5)
    
    over = xMin + r*(xMax - xMin)
    under = xMax - r*(xMax - xMin)
    
    if (f(under)>f(over)): return recursive_minimum_point(f, under, xMax)
    else: return recursive_minimum_point(f, xMin, over)

def main():
    print(recursive_minimum_point((lambda x: x**2 +7.3*x +4), -10, 10))
    return

if __name__ == '__main__':
    main()