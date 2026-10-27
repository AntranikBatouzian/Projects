class Node:
    
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node
    
    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data


class linkedlist:

    def __init__(self, root = None):
        self.root = root
        self.length = 0

    def iterate(self):
        curr_node = self.root
        while curr_node:
            yield curr_node.get_data()
            curr_node = curr_node.get_next()
    
    def get_length(self):
        return self.length

    def add(self, data):
        new_node = Node(data, next_node = self.root)
        self.root = new_node
        self.length+=1

    def remove(self, data):
        curr_node = self.root
        prev_node = None
        while curr_node:
            if curr_node.get_data() == data:
                if prev_node:
                    prev_node.set_next(curr_node.get_next())
                else:
                    self.root = curr_node.get_next()
                self.length-=1    
                return True
            else:
                prev_node = curr_node
                curr_node = curr_node.get_next()
        return False
    
    def replace(self, old_data, new_data):
        curr_node = self.root
        while curr_node:
            if curr_node.get_data() == old_data:
                curr_node.set_data(new_data)
                return True
            else:
                curr_node = curr_node.get_next()
        return False

    def find(self, data):
        curr_node = self.root
        while curr_node:
            if curr_node.get_data() == data:
                return data
            else:
                curr_node = curr_node.get_next()
        return None
    

my_list = linkedlist()
my_list.add('john')
my_list.add('kate')
my_list.add('bob')
my_list.add('kevin')
print(' '.join([i for i in my_list.iterate()]))
print(my_list.get_length())
my_list.remove('bob')
print(' '.join([i for i in my_list.iterate()]))
print(my_list.get_length())
my_list.replace('kate','greg')
print(' '.join([i for i in my_list.iterate()]))
print(my_list.get_length())



    