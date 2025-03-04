#1) Direct recursion
def direct_recursion(n):
    if n == 0:
        return 
    print(n)
    direct_recursion(n-1)

direct_recursion(5)

#2) Indirect recursion

def func1(n):
    if n > 0:
        print(n,end=" ")
        func2(n-1)

def func2(n):
    if n > 0:
        print(n ,end=" ")
        func1(n-1)

func1(5)


#Tail recursion 

def tail_recursion(n):
    if n == 0:
        return 
    print(n,end=" ")
    tail_recursion(n-1)

tail_recursion(5)

#Non tail recursion

def non_tail(n):
    if n == 0:
        return
    non_tail(n-1)
    print(n,end=" ")

non_tail(5)