import array

class ArrayList():              
    def __init__(self):
        self.arr = [None] * 10
    
    def __len__(self):
        length = 0
        for i in self.arr:
            if i == None:
                break
            else:
                length += 1
        return length
    
    def __str__(self):
        info = "["
        for i in self.arr:
            if i != None:
                info += (str(i) + ",")
        #info = info[:-1] if len(info) > 1 else info + "]"

        return info + "]"
    
    def __getitem__(self, index):
        if index < 0:
            raise IndexError("Invalid Index")
        if index >= len(self.arr):
            raise IndexError("Invalid Index")
        al_index = 0
        for i in self.arr: 
            if al_index == index:
                return i
            al_index += 1
    
    def append(self, data):
        def append_wrapper():
            if len(self.arr) == 0:
                self.arr[0] = data
            for i in range(len(self.arr)+1):
                try:
                    if self.arr[i] == None:
                        self.arr[i] = data
                        return True
                except IndexError:
                    pass
            return False
        res = append_wrapper()
        if res == False:
            self.arr = self.arr + ([None]*10)
            self.append(data)
        return
    
    def pop(self, index):
        def pop_wrapper():
            popped_entry = self.arr[index]
            self.arr.remove(index)
            if len(self) <= self.arr/2:
                return False, popped_entry
            return True, popped_entry
        res, entry = pop_wrapper()
        if res == False:
            self.size /= 2
        return entry
    
    def remove(self, value):
        def remove_wrapper():
            for i in range(len(self)-1):
                if self.arr[i] == value:
                    self.arr.remove(i)
                    if len(self) <= self.size/2:
                        return False
                    return True
        res = remove_wrapper()
        if res == False:
            self.size /= 2


if __name__ == "__main__":
    
    my_array = ArrayList()
    
    for i in range(50):
        my_array.append(i)
    
    print(len(my_array))
    print(my_array)