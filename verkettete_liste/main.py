import random

class linked_list():
    def __init__(self):
        self.first_element = None
        
    def append(self, element):
        if self.first_element is not None:
            last_element = self.get_last_element()
            last_element.next_element = element
        else:
            self.first_element = element
            
    def get_first_element(self):
        return self.first_element
    
    def print_first_element(self):
        return self.get_first_element().content
    
    def get_last_element(self):
        last_element = self.get_first_element()
        while last_element.next_element is not None:
            last_element = last_element.next_element
        return last_element
    
    def print_last_element(self):
        return self.get_last_element().content
    
    def print_list(self):
        print_val = self.get_first_element()
        while print_val is not None:
            print(print_val.content)
            print_val = print_val.next_element
    
    def get_length_list(self):
        length = 0
        element = self.get_first_element()
        while element is not None:
            length += 1
            element = element.next_element
        return length
    
    def sort(self):
        n = self.get_length_list()
        swapped = False
        for i in range(n-1):
            for j in range(0, n-i-1):
                if self.get_element_by_index(j).content > self.get_element_by_index(j+1).content:
                    swapped = True
                    self.get_element_by_index(j).content, self.get_element_by_index(j+1).content = self.get_element_by_index(j+1).content, self.get_element_by_index(j).content
                                       
            if not swapped:
                print("sorted")
                return        
            
    def get_element_by_index(self, index):
        n = self.get_length_list()
        element = self.get_first_element()
        if index > n-1 or index < 0:
            print("Error: Index not in list")
            return list_element()
        for i in range(index):
            element = element.next_element
        return element
    
    def print_element_by_index(self, index):
        return self.get_element_by_index(index).content
            
            
class list_element():
    
    def __init__(self, content = None):
        self.content = content
        self.next_element = None


def main():
    my_list = linked_list()
    my_list.append(list_element(random.randint(0, 100)))
    my_list.append(list_element(random.randint(0, 100)))
    my_list.append(list_element(random.randint(0, 100)))
    my_list.append(list_element(random.randint(0, 100)))
    my_list.append(list_element(random.randint(0, 100)))
    my_list.print_list()
    print("-----------------------------")
    print("First Element: " + str(my_list.print_first_element()))
    print("Last Element: " + str(my_list.print_last_element()))
    print("List Length: " + str(my_list.get_length_list()))
    print("Element at index: " + str(my_list.print_element_by_index(1)))
    print("-----------------------------")
    my_list.sort()
    my_list.print_list()
    print("-----------------------------")
    print("First Element: " + str(my_list.print_first_element()))
    print("Last Element: " + str(my_list.print_last_element()))
    print("List Length: " + str(my_list.get_length_list()))
    print("Element at index: " + str(my_list.print_element_by_index(1)))
    print("-----------------------------")
    
    
if __name__ == "__main__":
    main()