class BSTNode:
    def __init__(self,initdata):
        self.data = initdata
        self.less = None
        self.more = None
    
    def getData(self):
        return self.data

    def getLess(self):
        return self.less
    
    def getMore(self):
        return self.more

    def setData(self,newdata):
        self.data = newdata

    def setLess(self,newless):
        self.less = newless

    def setMore(self,newmore):
        self.less = newmore

    def add(self,new_val):
        if new_val < self.data:
            if self.less == None:
                newnode = BSTNode(new_val)
                self.less = newnode
            else:
                self.less.add(new_val)
        else:
            if self.more == None:
                newnode = BSTNode(new_val)
                self.more = newnode
            else:
                self.more.add(new_val)

                


#we could create a new node like this
mynode = BSTNode(42)
mynode.add(77)
print(mynode.getMore().getData())
print(mynode.getData())
