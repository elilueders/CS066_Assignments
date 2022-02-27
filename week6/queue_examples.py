# 11,8,5,9
# 4
# 11
# 8
# 5
# 9

from pythonds.basic import Queue

my_q = Queue()
my_q.enqueue(4)
my_q.enqueue(7)
my_q.enqueue(11)
my_q.dequeue()
my_q.enqueue(8)
my_q.dequeue()
my_q.enqueue(5)
my_q.enqueue(9)

print("Size:",my_q.size())

while not my_q.isEmpty():
    print(my_q.dequeue())