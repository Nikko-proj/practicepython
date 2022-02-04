def lessthanten(lst):
    for i in lst:
        if i < 5:
            print(i)
            
def lessthantenlist(lst):
    '''Return a list of all numbers less than 5'''
    temp = []
    for i in lst:
        if i < 5:
            temp.append(i)
    return temp
            
def main():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    lessthanten(a)
    print(lessthantenlist(a))
    
if __name__ == '__main__':
    main()