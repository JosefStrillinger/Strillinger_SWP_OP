import random
from linked_list import LinkedList

def print_list_querys(list):
    print("-----------------------------")
    print("First Element: " + str(list.print_first_element()))
    print("Last Element: " + str(list.print_last_element()))
    print("List Length: " + str(len(list)))
    print("Element at index ("+ str(1) +"): " + str(list[1]))
    print("-----------------------------")

def main():
    my_list = LinkedList()
    count = 10
    
    for i in range(count):
        my_list.append(random.randint(0, 100))

    print(my_list)
    print_list_querys(my_list)
    
    # sorting list
    my_list.sort()
    print(my_list)
    print_list_querys(my_list)
    
    # removing first element
    my_list.remove(0)
    print(my_list)
    print_list_querys(my_list)
    
    # reversing list
    my_list.reverse()
    print(my_list)
    print_list_querys(my_list)
    
    # shuffle the list
    my_list.shuffle()
    print(my_list)
    print_list_querys(my_list)
    
    # inserting value 10 at index 5
    print("insert")
    my_list.insert(8, 10)
    print(my_list)
    print_list_querys(my_list)
    
    # clearing the list
    my_list.clear()
    print(my_list)
    #print_list_querys(my_list)
    
if __name__ == "__main__":
    main()