import math

def recursive_bisection(f, xMin, xMax, precision = 0.0001):

    xAve = ((xMin + xMax)*0.5)
    if ((xMax - xMin)<precision): return xAve
    if ((f(xMin) * f(xAve)) >0): return recursive_bisection(f, xAve, xMax)
    else: return recursive_bisection(f, xMin, xAve)

def main():
    value = recursive_bisection((lambda x: math.cos(x)), 0, 4)
    print(value)

    return


if __name__ == '__main__':
    main()