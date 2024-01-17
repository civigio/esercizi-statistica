import math

def minimum_point(f, xMin, xMax, precision = 0.0001):
    r = ((math.sqrt(5)-1)*0.5)
    
    while ((xMax - xMin)>precision):
        over = xMin + r*(xMax - xMin)
        under = xMax - r*(xMax - xMin)
        if (f(under)>f(over)): xMin = under
        else: xMax = over

    return ((xMax + xMin)*0.5)

def main():
    print(minimum_point((lambda x: x**2 +7.3*x +4), -10, 10))
    return

if __name__ == '__main__':
    main()