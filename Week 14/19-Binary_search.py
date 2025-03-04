def BinarySearch(list1,target):
    low = 0
    high = len(list1)-1
    found = False
    while low <= high and not found:
        mid = (low + high) // 2
        if target == list1[mid]:
            found = True
        elif target >= list1[mid]:
            low = mid + 1
        else:
            low = mid - 1
    if found == True:
        print("target found")
    else:
        print("target not found")

list1 = [1,3,6,4,9,8,5]
list1.sort()
print(list1)
target = int(input("Enter a number:"))
BinarySearch(list1,target)
