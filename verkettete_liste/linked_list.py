import random

class LinkedList():
    def __init__(self):
        self.first_element = None
        
    def __iter__(self):
        return LinkedListIterator(self.first_element)
    
    def __next__(self):
        self.current = self.first_element
        if not self.current:
           raise StopIteration
        elif self.current.get_next_element() is None:
            raise StopIteration
        else:
           item = self.current.content
           self.current = self.current.get_next_element()
           return item
       
    def __len__(self):
        length = 0
        element = self.get_first_element()
        while element is not None:
            length += 1
            element = element.get_next_element()
        return length
    
    def __getitem__(self, index):
        return self.get_element_by_index(index)
    
    def __str__(self):
        print_val = self.get_first_element()
        to_print = "["
        first = True
        while print_val is not None:
            if first:
                to_print = to_print + str(print_val)
                first = False         
            else:
                to_print = to_print + ", " + str(print_val)       
            print_val = print_val.get_next_element()
        to_print = to_print + "]"
        return to_print
     
    def append(self, element):
        new_element = Node(element)
        if self.first_element is not None:
            last_element = self.get_last_element()
            last_element.set_next_element(new_element)
        else:
            self.first_element = new_element
    
    def insert(self, index, content):
        new_element = Node(content)
        if index != 0 and not index > len(self)-1 and not index == len(self)-1:
            new_element.set_next_element(self[index])
            self[index-1].set_next_element(new_element)
        elif index == 0:
            new_element.set_next_element(self[index])
            self.set_first_element(new_element)
        elif index > len(self)-1:
            self.append(content)
        elif index == len(self)-1:
            new_element.set_next_element(self[index])
            self[index-1].set_next_element(new_element)
            
    def get_first_element(self):
        return self.first_element
    
    def set_first_element(self, element):
        self.first_element = element
    
    def print_first_element(self):
        if self.first_element is None:
            raise IndexError("No first element")
        return self.get_first_element().content
    
    def get_last_element(self):
        return self[len(self)-1]
    
    def print_last_element(self):
        if self.get_last_element() is None:
            raise IndexError("List is empty")
        return self.get_last_element().content
    
    def print_list(self):
        print_val = self.get_first_element()
        while print_val is not None:
            print(print_val.content)
            print_val = print_val.get_next_element()
    
    def sort(self):
        self.insertion_sort()#could be changed to bubble_sort()
    
    def bubble_sort(self):
        n = len(self)
        swapped = False
        for i in range(n-1):
            for j in range(0, n-i-1):
                if self[j].content > self[j+1].content:
                    swapped = True
                    self[j].content, self[j+1].content = self[j+1].content, self[j].content
                                       
            if not swapped:
                print("sorted")
                return
            
    def insertion_sort(self):
        sorted = None
        current = self.first_element
        while (current != None):
            next = current.get_next_element()
            sorted = self.sorted_insert(sorted, current)
            current = next
        self.first_element = sorted
        
    def sorted_insert(self, head_ref, new_element):
        current = None
        if(head_ref == None or (head_ref).content >= new_element.content):
            new_element.set_next_element(head_ref)
            head_ref = new_element
        else:
            current = head_ref
            while (current.get_next_element() != None and current.get_next_element().content < new_element.content):
                current = current.get_next_element()
            new_element.set_next_element(current.get_next_element())
            current.set_next_element(new_element)
        return head_ref
    
    def get_element_by_index(self, index):
        n = len(self)
        element = self.get_first_element()
        if index > n-1 or index < 0 or n == 0:
            raise IndexError("Please use a valid index")
        for i in range(index):
            element = element.get_next_element()
        return element
    
    def print_element_by_index(self, index):
        return self[index].content 
    
    def pop(self, index):
        if index != 0 and index != len(self)-1 and not index > len(self)-1:
            self[index-1].set_next_element(self[index].get_next_element())
        elif index == 0:
            self.set_first_element(self[index+1])
        elif index == len(self)-1:
            self[index-1].next_element = None
        elif index > len(self)-1:
            raise IndexError("Please use a valid index")
        print("Removed element at index: " + str(index))
        
    def reverse(self):
        if not len(self) < 1:
            prev = None
            current = self.get_first_element()
            while(current is not None):
                next = current.get_next_element()
                current.set_next_element(prev)
                prev = current
                current = next
            self.first_element = prev 
    
    def clear(self):
        self.set_first_element(None)
    
    def shuffle(self):
        indices = list(range(len(self)))
        random.shuffle(indices)
        new_linked_list = LinkedList()
        for index in indices:
            new_linked_list.append(self[index].content)
        self.first_element = new_linked_list.first_element
        
    def index(self, value):
        for i in range(len(self)):
            if self[i].content == value:
                #print("Value %s found at index %d" % (value, i))
                return i
        return None
    
    def contains(self, value):
        response = self.index(value)
        if response is None:
            #print("List does not contain: %s" % value)
            return False
        else:
            #print("List contains value %s" % value)
            return True
    
    def remove(self, value):
        response = self.index(value)
        if response is None:
            #print("List does not contain: %s" % value)
            return False
        else:
            #print("List contains value %s" % value)
            self.pop(response)
            return True
    
    def remove_all(self, value):
        # version 1
        new_list = LinkedList()
        for i in range(len(self)):
            if self[i].content != value:
                new_list.append(self[i].content)
        self.first_element = new_list.first_element
        #print(new_list)
        
        # version 2
        #prev_node = self.first_element
        #now_node = self.first_element
        #while(now_node != None):
        #    if(now_node.content == value):
        #        prev_node.set_next_element(now_node.get_next_element())
        #        now_node = now_node.get_next_element()
        #        continue
        #    else:
        #        prev_node = now_node
        #        now_node = now_node.get_next_element()
        
    
    def count(self, value):
        count = 0
        for i in range(len(self)):
            if self[i].content == value:
                count += 1
        return count
    
      
class LinkedListIterator:
    def __init__(self, head):
        self.current = head
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            item = self.current
            self.current = self.current.get_next_element()
            return item 
                
class Node():
    
    def __init__(self, content = None):
        self.content = content
        self.next_element = None

    def __lt__(self, other): 
        return self.content < other.content
    
    def __str__(self):
        return str(self.content)
    
    def get_next_element(self):
        return self.next_element
    
    def set_next_element(self, new_element):
        self.next_element = new_element