import random
import time
from linked_list import LinkedList
from double_linked_list import DoubleLinkedList
from array_list import ArrayList

def print_list_querys(list):
    print("-----------------------------")
    print("First Element: " + str(list.print_first_element()))
    print("Last Element: " + str(list.print_last_element()))
    print("List Length: " + str(len(list)))
    print("Element at index ("+ str(0) +"): " + str(list[0]))
    print("-----------------------------")

def main_linked_list():
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
    print("\npop")
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
    my_list.insert(8, 5)
    print(my_list)
    print_list_querys(my_list)
    
    # count number of elements with value of 5
    print("\ncount")
    print(my_list.count(5))
    print(my_list)
    print_list_querys(my_list)
    
    # get index of 5
    print("\nget index")
    print(my_list.index(5))
    print(my_list)
    print_list_querys(my_list)
    
    # remove first element that is 5
    print("\nremove")
    my_list.remove(5)
    print(my_list)
    print_list_querys(my_list)
    
    # remove all elements that are 5
    my_list.insert(8, 5)
    my_list.insert(8, 5)
    print(my_list)
    print("\nremove all")
    #my_list.remove_all(5)
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
    
def main_dll():
    my_list = DoubleLinkedList()
    count = 1000
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
    print("\npop")
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
    my_list.insert(8, 5)
    print(my_list)
    print_list_querys(my_list)
    
    # count number of elements with value of 5
    print("\ncount")
    print(my_list.count(5))
    print(my_list)
    print_list_querys(my_list)
    
    # get index of 5
    print("\nget index")
    print(my_list.index(5))
    print(my_list)
    print_list_querys(my_list)
    
    # remove first element that is 5
    print("\nremove")
    my_list.remove(5)
    print(my_list)
    print_list_querys(my_list)
    
    # remove all elements that are 5
    my_list.insert(8, 5)
    my_list.insert(8, 5)
    print(my_list)
    print("\nremove all")
    my_list.remove_all(5)
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

def main_al():
    my_array = ArrayList()
    
    for i in range(50):
        my_array.append(random.randint(0, 100))
    
    print(len(my_array))
    print(my_array)
    print(my_array[10])
    
if __name__ == "__main__":
    
    #main_ll()
    
    print("############################################################")
    
    #main_dll()
    
    print("############################################################")
    
    main_al()