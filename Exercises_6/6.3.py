def factorial(number):
    if number == 0: return 1
    else: return number*factorial(number-1)

    return

def main():
    value = int(input('Insert a number: '))
    print(factorial(value))

    return

if __name__ == '__main__':
    main()