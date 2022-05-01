
from distutils.log import error


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

    def __init__(self):
        self.head = None
        self.length = 0
        
    def isEmpty(self):
        return self.head == None
        
    def size(self):
        return self.length

    #this method is really a prepend - it puts the new node at the beginning
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        self.length += 1
            
    def __repr__(self):
        list_representation = ""
        current = self.head #start with the Node at the head
        while current: #this will keep going until current equals None
            list_representation += str(current.getData())+" -> "
            current = current.getNext() #move on to the next Node in the list
        list_representation += "None" #the last one in the list points to None
        return list_representation

    def __contains__(self,item):
        return self.search(item)
        
    def search(self,item):
        return self.__search_node(item,self.head)
    
    def __search_node(self,item,currnode):
        #if we're at the end of the list return False - it isn't here
        if currnode == None:
            return False
        #we found the item - return True
        elif currnode.getData() == item:
            return True
        #search the rest of the list
        else:
            return self.__search_node(item,currnode.getNext())

    def index(self, item):
        self.idx = 0
        return self.__index_node(item,self.head)
    
    def __index_node(self,item,currnode):
        if currnode == None:
            raise Exception("item "+str(item)+" is not in the list")
        if currnode.getData() == item:
            return self.idx
        else:
            self.idx += 1
            return self.__index_node(item,currnode.getNext())


"""my_list = UnorderedList()

my_list.add(31)
my_list.add(77)
my_list.add(17)
my_list.add(93)
my_list.add(26)
my_list.add(54)

print( my_list.index(31) )
print( my_list.index(77) )
print( my_list.index(17) )
print( my_list.index(93) )
print( my_list.index(26) )
print( my_list.index(22) )"""