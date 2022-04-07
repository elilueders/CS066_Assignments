
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class UnorderedList:
# add(item) adds a new item to the list. It needs the item and returns nothing. Assume the item is not already in the list.
# size() returns the number of items in the list. It needs no parameters and returns an integer.
# index(item) returns the position of item in the list. It needs the item and returns the index. Assume the item is in the list.
# insert(pos,item) adds a new item to the list at position pos. It needs the item and returns nothing. Assume the item is not already in the list and there are enough existing items to have position pos.
# pop() removes and returns the last item in the list. It needs nothing and returns an item. Assume the list has at least one item.

# List() creates a new list that is empty. It needs no parameters and returns an empty list.
    def __init__(self):
        self.head = None
        
# isEmpty() tests to see whether the list is empty. It needs no parameters and returns a boolean value.
    def isEmpty(self):
        return self.head == None
    
# append(item) adds a new item to the end of the list making it the last item in the collection. It needs the item and returns nothing. Assume the item is not already in the list.
    #this method is really a prepend - it puts the new node at the beginning
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
            
    def __repr__(self):
        list_representation = ""
        current = self.head #start with the Node at the head
        while current: #this will keep going until current equals None
            list_representation += str(current.getData())+" -> "
            current = current.getNext() #move on to the next Node in the list
        list_representation += "None" #the last one in the list points to None
        return list_representation
    
    def __getitem__(self,index):
        
        if index < 0:
            raise Exception("list index "+str(index)+" is out of range")
        
        current = self.head
        item_counter = 0
        
        while current and item_counter < index:
            
            current = current.getNext()
            item_counter += 1
            
        if current == None:
            raise Exception("list index "+str(index)+" is out of range")
            
        return current.getData()

# search(item) searches for the item in the list. It needs the item and returns a boolean value.
    def __contains__(self, item):
        current = self.head
        found = False

        while current and not found:

            if item == current.getData():
                found = True
            else: 
                current = current.getNext()

        return found

# pop(pos) removes and returns the item at position pos. It needs the position and returns the item. Assume the item is in the list
    def pop(self,index):
        
        if index < 0:
            raise Exception("list index "+str(index)+" out of range")
        
        current = self.head
        previous = None
        item_counter = 0
        
        while current and item_counter < index:
            previous = current
            current = current.getNext()
            item_counter += 1
            
        if current == None:
            raise Exception("list index "+str(index)+" out of range")
            
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
            
        return current.getData()

# remove(item) removes the item from the list. It needs the item and modifies the list. Assume the item is present in the list.
            
my_list = UnorderedList()

my_list.add(31)
my_list.add(77)
my_list.add(17)
my_list.add(93)
my_list.add(26)
my_list.add(54)
print(my_list)

print( 17 in my_list ) #should print True
print( 34 in my_list ) #should print False
