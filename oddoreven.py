def odd_or_even(num):
    if num % 4 == 0:
        return 'Divisible by 4'
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
    
def main():
    for i in range(1,21):
        print('{} is {}'.format(i,odd_or_even(i)))
        
if __name__ == '__main__':
    main()