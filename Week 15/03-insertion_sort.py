# It is a simple sorting algorithm 
# It builds the final sorted list one item at a time

# Steps of insertion algorithm

# 1) Consider the first element is sorted and rest is unsorted
# 2) Take the first element in the unsorted part and compared it to the sorted part
# 3) If U1(unsorted part element 1) < s1 (sorted part element 1) in the currect index, else leave it as it is
# 4) take next element in the un sorted part and compare to sorted part 
# 5) repeat these steps until getting the sorted array 

list1 = [2,4,3,5,1]
for i in range(1,len(list1)):
    current_val = list1[i]
    pos = i
    while current_val < list1[pos-1] and pos > 0:
        list1[pos] = list1[pos-1]
        pos = pos-1
        list1[pos] = current_val

print(list1)


# list1 = [64, 34, 25, 12, 22, 11, 90]
# for i in range(1,len(list1)):
#     key = list1[i]
#     j = i-1

#     while j >=0 and key < list1[j]:
#         list1[j+1] = list1[j]
#         j -= 1
#         list1[j+1] = key
# print(list1)