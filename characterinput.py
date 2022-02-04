# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that
# they will turn 100 years old.

class person:
    
    year = 2022
    
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age
    
    def nameage(self):
        ''' Asks name and age '''
        self.name = str(input('Enter your name: '))
        self.age = int(input('Enter your age: '))
        
    def onehundred(self):
        ''' Returns year the person will turn 100 '''
        return (self.year - self.age) + 100
        
    
def main():
#     Kirby = person()
#     Kirby.nameage()
#     print('{} is {} years old.'.format(Kirby.name,Kirby.age))
#     print('{} will turn 100 in the year {}'.format(Kirby.name,Kirby.onehundred()))
    
    names = [{'Duke':13},{'Kirby':3},{'Toldo':4},{'Nikko':26},{'Courtney':24}]
    lst = []
    for i in names:
        for j in i:
            print(j,type(j),i[j],type(i[j]),sep=" ")
            lst.append(person(j,i[j]))
            
    for a_person in lst:
        print('{} will turn 100 in the year {}'.format(a_person.name,a_person.onehundred()))
            
    
if __name__ == '__main__':
    main()