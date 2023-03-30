import array

class ArrayList():              
    def __init__(self):
        self.arr = []
        self.size = 10
    
    def __len__(self):
        l = 0
        for i in self.arr:
            if i == None:
                break
            else:
                l += 1
        return l
    
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
        if index >= self.size:
            raise IndexError("Invalid Index")
        al_index = 0
        for i in self.arr: 
            if al_index == index:
                return i
            al_index += 1
    
    def append(self, data):
        def append_wrapper():
            if len(self.arr) < self.size:
                self.arr.append(data)
                return True
            return False
        res = append_wrapper()
        if res == False:
            self.size *= 2
            self.append(data)
        return
    
    def pop(self, index): # insert checks 
        def pop_wrapper():
            popped_entry = self.arr[index]
            self.arr.remove(index)
            if len(self) <= self.size/2:
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