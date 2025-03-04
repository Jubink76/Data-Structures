#some time it reffered as sinking sort
# it sort a number of elements in the list by comparing the each pair of adjascent items
# swap them if they are wrong order

# Ascending order
# 1) Starting at the first index,compare the current element to next element
# 2) If the current element is greater than the next element swap
# 3) If it is not greater move to next 
# 4) repaeat

list1 = [10,15,4,28,0]
# for i in range(len(list1)-1,0,-1):
#     for j in range(i):
#         if list1[j] > list1[j+1]:
#             list1[j],list1[j+1] = list1[j+1],list1[j]

# print(list1)

for i in range(len(list1)-1,0,-1):
    for j in range(i):
        if list1[j] < list1[j+1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]

print(list1)
