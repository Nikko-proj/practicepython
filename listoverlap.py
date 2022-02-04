# Write a program that returns a list that contains only the elements
# that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

from random import randrange as rd

def overlap(a,b):
    temp = []
    for i in a:
        for j in b:
            if i == j:
                temp.append(i)
    return temp

def main():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    print(overlap(a,b))
    
    
if __name__ == '__main__':
    main()