class Node():
    ''' Every node has data and points to the next data in the next node'''
    def __init__(self, data, node=None):
        ''' Initializes a node '''
        self.data = data 
        self.next_node = node
        
    def get_next(self):
        '''Returns the next node'''
        return self.next_node
    
    def set_next(self, node):
        '''Sets the next node to the node passed through'''
        self.next_node = node
        
    def get_data(self):
        '''Returns the object's data'''
        return self.data
    
    def set_data(self, data):
        '''Sets the object's data to the data passed in'''
        self.data = data
        
class LinkedList():
    ''' Every linked list starts with a root and size'''
    def __init__(self, root=None):
        self.root = root # points to the head node
        self.size = 0 # keeps track of the size of the linked list
        
    def get_size(self):
        '''Returns the size of the linked list'''
        return self.size
    
    def add(self,data):
        '''
        Create new node with data and current root
        new root equals the new node
        increment the size by 1
        '''
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1
        
    def remove(self, data):
        # Keep track of two nodes
        current_node = self.root # the current node starts at root
        previous_node = None # previous node
        while current_node:
            if current_node.get_data() == data:
                if previous_node:
                    previous_node.set_next(current_node.get_next())
                else:
                    self.root = current_node
                self.size -= 1
                return True # data was found and removed
            else:
                previous_node = current_node
                current_node = current_node.get_next()
        return False # data was not found
    
    def find(self, data):
        current_node = self.root
        while current_node: # python while True
            if current_node.get_data() == data:
                return current_node.get_data()
            else:
                current_node = current_node.get_next()
        return None
    
def main():
    myLink = LinkedList()
    myLink.add(10)
    myLink.add(5)
    myLink.add(6)
    print('size: {}'.format(myLink.get_size()))
    myLink.remove(5)
    print('size: {}'.format(myLink.get_size()))
    print('Finding 6 in linked list: {}'.format(myLink.find(6)))
    print('Removing 11 from linked list: {}'.format(myLink.remove(11)))

if __name__ == '__main__':
    main()
            
        