import math

def bisection(f, xMin, xMax, precision = 0.0001):

    while ((xMax - xMin) > precision):
        xAve = ((xMin + xMax)*0.5)
        if ((f(xMin) * f(xAve)) >0): xMin = xAve
        else: xMax = xAve

    return xAve

def main():
    value = bisection((lambda x: math.cos(x)), 0, 4)
    print(value)

    return


if __name__ == '__main__':
    main()