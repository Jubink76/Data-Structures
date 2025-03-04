# 1) split the unsorted list
# 2) Devide the unsorted list until it is contain single element
# 3) Compare the divided based on the condintion( min / max )
# 4) Merge them

num = int(input("Enter the number of elements:"))
list1 = [int(input("Enter the list elements:") for x in range(num))]
def merge_sort(list1):
    if len(list1) > 1:
        mid = len(list1) // 2
        left_list = list1[:mid]
        right_list = list1[mid:]
        merge_sort(left_list)
        merge_sort(right_list)
        i = 0
        j = 0
        k = 0

        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list1[k] = left_list[i]
                i = i+1
                k = k+1
            else:
                list1[k] = right_list[j]
                j = j+1
                k = k+1
        while i < len(left_list):
            list1[k] = left_list[i]
            i = i+1
            k = k+1
        while j < len(right_list):
            list1[k] = right_list[j]
            j = j+1
            k = k+1

merge_sort(list1)
print(list1)

