from queue import LifoQueue
stack = LifoQueue() 
# in this stack we can define a limit of perticular stack by LifoQueue(3)
# if limit exceeded it will raise error
# but it wont show the error it will wait for the input
stack.put(10)
# here we can define time out parameter to show thee error 
# that is stack.put(10,timeout=1) here 1 represent the 1 sec time
stack.get(10)
stack.get(10,timeout= 1)
