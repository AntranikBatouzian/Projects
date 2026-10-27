class node:
  
    def __init__(self, data, prev_node = None, next_node = None):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_prev(self):
        return self.prev_node
    
    def set_prev(self, new_prev):
        self.prev_node = new_prev

    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next):
        self.next_node = new_next


class linkedlist:

    def __init__(self, root = None, end = None):
        self.root = root
        self.end = end
        self.length = 0

    def iterate(self):
        curr_node = self.root
        while curr_node:
            yield curr_node.get_data()
            curr_node = curr_node.get_next()

    def riterate(self):
        curr_node = self.end
        while curr_node:
            yield curr_node.get_data()
            curr_node = curr_node.get_prev()

    def get_length(self):
        return self.length

    def add(self, data):
        new_node = node(data, None, self.root)
        if self.root:
            curr_node = self.root
            curr_node.set_prev(new_node)
        else:
            self.end = new_node
        self.root = new_node
        self.length+=1

    def append(self, data):
        new_node = node(data, self.end, None)
        if self.end:
            curr_node = self.end
            curr_node.set_next(new_node)
        else:
            self.root = new_node
        self.end = new_node
        self.length+=1
  
    def front_remove(self, data):
        curr_node = self.root
        while curr_node:
            if curr_node.get_data() == data:
                prev_node = curr_node.get_prev()
                ahead_node = curr_node.get_next()
                if prev_node and ahead_node:
                    prev_node.set_next(ahead_node)
                    ahead_node.set_next(prev_node)
                elif prev_node:
                    self.end = prev_node
                elif ahead_node:
                    self.root = ahead_node
                else:
                    self.root, self.end = None, None
                return True
            else:
                curr_node = curr_node.get_next()
        return False

    def end_remove(self, data):
        curr_node = self.root
        while curr_node:
            if curr_node.get_data() == data:
                prev_node = curr_node.get_prev()
                ahead_node = curr_node.get_next()
                if prev_node and ahead_node:
                    prev_node.set_next(ahead_node)
                    ahead_node.set_next(prev_node)
                elif prev_node:
                    self.end = prev_node
                elif ahead_node:
                    self.root = ahead_node
                else:
                    self.root, self.end = None, None
                return True
            else:
                curr_node = curr_node.get_prev()
        return False

    def front_replace(self, to_be_replaced, new_data):
        curr_node = self.root
        while curr_node:
            if curr_node.get_data() == to_be_replaced:
                curr_node.set_data(new_data)
                return True
            else:
                curr_node = curr_node.get_next()
        return False

    def end_replace(self, to_be_replaced, new_data):
        curr_node = self.end
        while curr_node:
            if curr_node.get_data() == to_be_replaced:
                curr_node.set_data(new_data)
                return True
            else:
                curr_node = curr_node.get_prev()
        return False
    
    def front_find(self, data):
        curr_node = self.root
        while curr_node:
            if curr_node.get_data() == data:
                return data
            else:
                curr_node = curr_node.get_next()
        return False
    
    def end_find(self, data):
        curr_node = self.end
        while curr_node:
            if curr_node.get_data() == data:
                return data
            else:
                curr_node = curr_node.get_prev()
        return False


mylist = linkedlist()
mylist.add(1)
mylist.front_remove(1)
print(mylist.get_length())
mylist.add(2)
mylist.add(3)
print(' '.join([str(i) for i in mylist.iterate()]))
print(mylist.get_length())
mylist.append(0)
mylist.append(-1)
mylist.add(4)
print(' '.join([str(i) for i in mylist.iterate()]))
print(mylist.get_length())
mylist.end_remove(0)
print(' '.join([str(i) for i in mylist.iterate()]))
print(mylist.get_length())
mylist.front_replace(2, 1)
mylist.end_replace(-1, 0)
print(' '.join([str(i) for i in mylist.iterate()]))
print(mylist.get_length())
print(mylist.front_find(4))
print(mylist.end_find(1))
print(mylist.front_find(6))
print(mylist.end_find(7))