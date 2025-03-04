stack = []

def push():
    element = int(input("Enter the element:"))
    stack.append(element)
    print(stack)
def pop():
    if not stack:
        print("Stack is empty nothing to delete")
    e = stack.pop()
    print(f'Poped element is {e}')
    print(stack)

while True:
    choice = int(input("Select any of the operatin , 1.push, 2. pop, 3.break"))
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        break
    else:
        print("choose correct choice ")
