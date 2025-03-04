Queue = []

def enqueue():
    element = int(input("Enter the elemenet:"))
    Queue.append(element)
    print(f"Added element is {element}")

def dequeue():
    if not Queue:
        print("Queue is empty")
    else:
        e = Queue.pop(0)
        print(f'removed element is {e}')
def display():
    print(Queue)

while True:
    choice = int(input("Enter any of the choices 1- add ,2 - remove, 3-display,4-quite"))
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("choose any of the corrected choice")

