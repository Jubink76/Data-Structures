# In place comparison 

# In this first find the min/ max element in the perticular list
# stores in the first position, That would become the sorted sub array
# then considering the remaining unsorted subarray
# repeat the steps

# In Ascending order 
# using 2 looop
list1 = [64, 34, 25, 12, 22, 11, 90]
for i in range(len(list1)):
    min_idx = i
    for j in range(i+1,len(list1)):
        if list1[j] < list1[min_idx]:
            min_idx = j
    list1[i],list1[min_idx] = list1[min_idx], list1[i]
print(list1)


# # using 1 loop

for i in range(len(list1)):
    min_val = min(list1[i:])
    min_idx = list1.index(min_val,i)
    if list1[i] != list1[min_idx]:
        list1[i],list1[min_idx] = list1[min_idx],list1[i]
print(list1)

# In Descending order

for i in range(len(list1)):
    max_pos = i
    for j in range(i+1,len(list1)):
        if list1[j] > list1[max_pos]:
            max_pos = j
    if list1[i] != list1[max_pos]:
        list1[i], list1[max_pos] = list1[max_pos], list1[i]
print(list1)



for i in range(len(list1)):
    max_val = max(list1[i:])
    max_idx = list1.index(max_val,i)
    if list1[i] != list1[max_idx]:
        list1[i], list1[max_idx]= list1[max_idx],list1[i]

print(list1)
