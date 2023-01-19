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
        
    def append(self, element):
        if self.first_element is not None:
            last_element = self.get_last_element()
            last_element.set_next_element(element)
        else:
            self.first_element = element
            
    def get_first_element(self):
        return self.first_element
    
    def print_first_element(self):
        return self.get_first_element().content
    
    def get_last_element(self):
        return self[len(self)-1]
    
    def print_last_element(self):
        return self.get_last_element().content
    
    def print_list(self):
        print_val = self.get_first_element()
        while print_val is not None:
            print(print_val.content)
            print_val = print_val.get_next_element()
    
    def sort(self):
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
    
    def get_element_by_index(self, index):
        n = len(self)
        element = self.get_first_element()
        if index > n-1 or index < 0:
            raise IndexError("Please use a valid index")
        for i in range(index):
            element = element.get_next_element()
        return element
    
    def print_element_by_index(self, index):
        return self.get_element_by_index(index).content    
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
                
class ListElement():
    
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

def main():
    my_list = LinkedList()
    count = 10
    for i in range(count):
        my_list.append(ListElement(random.randint(0, 100)))
    my_list.print_list()
    print("-----------------------------")
    print("First Element: " + str(my_list.print_first_element()))
    print("Last Element: " + str(my_list.print_last_element()))
    print("List Length: " + str(len(my_list)))
    print("Element at index: " + str(my_list.print_element_by_index(1)))
    print("-----------------------------")
    #list2 = my_list
    my_list.sort()
    my_list.print_list()
    print("-----------------------------")
    print("First Element: " + str(my_list.print_first_element()))
    print("Last Element: " + str(my_list.print_last_element()))
    print("List Length: " + str(len(my_list)))
    print("Element at index: " + str(my_list.print_element_by_index(1)))
    print("-----------------------------")
    #list2.print_list()
    #print("-----------------------------")
    #sorted(list2)
    #list2.print_list()
    
    
if __name__ == "__main__":
    main()