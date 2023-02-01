import random
import time
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
    time1 = time.time()
    
    
    for i in range(count):
        my_list.append(random.randint(0, 100))

    print(my_list)
    print_list_querys(my_list)
    
    # sorting list
    print("\nsort")
    my_list.sort()
    print(my_list)
    print_list_querys(my_list)
    
    # pop first element
    print("\nremove")
    my_list.pop(0)
    print(my_list)
    print_list_querys(my_list)
    
    # reversing list
    print("\nreverse")
    my_list.reverse()
    print(my_list)
    print_list_querys(my_list)
    
    # shuffle the list
    print("\nshuffle")
    my_list.shuffle()
    print(my_list)
    print_list_querys(my_list)
    
    # inserting value 10 at index 5
    print("\ninsert")
    my_list.insert(8, 10)
    print(my_list)
    print_list_querys(my_list)
    
    # check if list contains 5
    print("\ncontains")
    print(my_list.contains(5))
    print(my_list)
    print_list_querys(my_list)
    
    # clearing the list#
    print("\nclear")
    my_list.clear()
    print(my_list)
    #print_list_querys(my_list)
    
    print("\nTime: " + str(time.time()*1000 - time1*1000) + " ms")
    
    
if __name__ == "__main__":
    main()