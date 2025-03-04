# Factorial calculation

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(5))

# fibonacci series


def fab(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fab(n-1) + fab(n-2)
    
print(fab(6))

# sum of first n natural numbers

def result(n):
    if n == 0:
        return 0
    return n + result(n-1)

print(result(5))

# Reverse a string using recursion
def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]    
print(reverse_string("hello"))



