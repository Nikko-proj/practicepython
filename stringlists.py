# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

def is_palindrome(word):
    try:
        return True if word == word[::-1] else False
    except TypeError as e:
        return 'Enter a valid string' 
    
def main():
    words = ['racecar','world','civic','radar']
    for word in words:
        print('{} is a palindrome: {}'.format(word,is_palindrome(word)))
    print(is_palindrome(55))
    
if __name__ == '__main__':
    main()