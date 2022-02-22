from pythonds.basic import Queue

the_queue = Queue()

print(the_queue.isEmpty())

the_queue.enqueue("A")
the_queue.enqueue("B")
print(the_queue.size())

the_queue.enqueue("C")
print(the_queue.dequeue())
the_queue.enqueue("D")
the_queue.enqueue("E")
print(the_queue.isEmpty())
print(the_queue.size())
print(the_queue.dequeue())
the_queue.dequeue()
the_queue.dequeue()
the_queue.enqueue("F")
print(the_queue.size())

for x in the_queue:
    print(x)

