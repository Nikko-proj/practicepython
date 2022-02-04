def divisors():
    '''
    Create a program that asks the user for a number
    and then prints out a list of all the divisors
    of that number.
    '''
    try:
        num = int(input('Enter a whole number: '))
    except ValueError as e:
        print('Please enter a whole number')
    for i in range(1,num+1):
        if num % i == 0:
            print('{} is a divisor of {}'.format(i,num))
        
def main():
    divisors()
    
if __name__ == '__main__':
    main()