# It is also called as partition exchange sort
# Developed by Tony Hoare in 1959 and published in 1961 
# It can be 2 or 3 times faster than the merge sort and heap sort


# comparison sort
# in_place algorithm
# Unstable algorithm
# Recursive algorithm


# Quick sort is devide and conquer type algorithm
# 1) Devide
        # Devide the list in to sublists
        # Devide the list by using pivot element(dividing element)
        # We can choose the pivot element any of the element in the list
                # first number / last numeber / random number / median of three values(first, mid, last)
        # most of the cases the first and last element is selected as the pivot element
        # but in the case of sorted list/ reverse sorted list these are the bad choice
        # The selection of pivot element is based on the type of input

# after selecting the pivot value  we want find out the exact position of the pivot value where it should be 
# for that we need two variables
# Then start combine with the pivot value 
# for that we need to follow few rules
        #1) left <= right
        #2) list[left] <= pivot
        #3) list[right] >= pivot
# This is for ascending order
# after the checking those condition and the right and left is crossing each other that should be the position of pivot value

# If you take first element as pivot
        # the pivot value is left

# if you take last element as pivot 
        # the pivot value is right

# if you took the pivot element as random, we have to swap the pivot value to either last or first

# if you select the pivot value as median
        # find the mid positon 
        # sort the elments(first, mid, last)

# in this the condition  for descending which we following is different
        #1) left <= right
        #2) list[left] >= pivot
        #3) list[right] <= pivot

# 2) Conquer
        # find out the solution for sublist recursively

# 3) combine

def pivot_place(list1,first,last):
    pivot = list1[first]
    left = first+1
    right = last
    while True:
        while left <= right and list1[left] <= pivot:
            left  += 1
        while left <= right and list1[right] >= pivot:
            right -= 1
        if right < left:
             break
        else:
            list1[left], list1[right] = list1[right] , list1[left]
    list1[first], list1[right] = list1[right], list1[first]
    return right

def quicksort(list1,first,last):
    if first < last:
        p = pivot_place(list1,first,last)
        quicksort(list1,first,p-1)
        quicksort(list1,p+1,last)

list1 = [56,26,93,17,31,44]
n = len(list1)
quicksort(list1,0,n-1)
print(list1)