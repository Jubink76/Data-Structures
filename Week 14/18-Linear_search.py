
def linear_search(list1,target):
    for i in range(len(list1)):
        if target == list1[i]:
            print("target found")
            break
    else:
        print("given target is not present in the given list")
list1 = [2,5,6,3,8]
key = int(input("entere the key"))
linear_search(list1,key)
