from queue import Queue
q = Queue()
# int this we can assign the maximum sizee of thee queue at first
# by using Queue(maxsize=3)
# Queue.full is used for checking the Queue is full or not
# syntax of put methodd --> put(item,block=True-default,timeout=n)
# if block is true and timeout is None it is add element until the free slot is available
# There is also a syntax instead of that --> put_nowait(item)

# also similar we have get() or get_nowait()
q.put(10)
q.put(20)
q.put(30)
print(q.get())