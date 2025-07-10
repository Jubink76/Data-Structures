class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
        
class Linked_list:
    def __init__(self):
        self.head = None
    
    def insert_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        curr = self.head
        while curr.ref:
            curr = curr.ref
        curr.ref = new_node
    def display(self):
        if self.head is None:
            print("list is empty")
            return
        curr = self.head
        while curr:
            print(curr.data,end="-->")
            curr = curr.ref
            
# merge_two_sorted_list            
def merge_lists(l1, l2):
    dummy = Node(-1)
    tail = dummy
    
    while l1 and l2:
        if l1.data <= l2.data:
            tail.ref = l1
            l1 = l1.ref
        else:
            tail.ref = l2
            l2 = l2.ref
        tail = tail.ref
    if l1:
        tail.ref = l1
    elif l2:
        tail.ref = l2
    return dummy.ref

#merge_dupliacte from sorted list
def remove_duplicate(head):
    if head is None:
        print("list is empty")
        return
    curr = head
    while curr and curr.ref:
        if curr.data == curr.ref.data:
            curr.ref = curr.ref.ref
        else:
            curr =curr.ref
    return head

# remove duplicate from unsorted_list

def remove_dup_unsorted(head):
    if head is None:
        return None
    seen = set()
    curr = head
    prev = None
    
    while curr:
        if curr.data in seen:
            prev.ref = curr.ref
        else:
            seen.add(curr.data)
            prev = curr
        curr = curr.ref
    return head
    
# to find the nth node from end
def find_nth_from_end(head,n):
    fast = slow = head
    for _ in range(n):
        if not fast:
            return None
        fast = fast.ref
    while fast:
        slow = slow.ref
        fast = fast.ref
    return slow.data if slow else None
    
# rotate a linkedlist by k position
def rotate_list(head,k):
    if not head or k == 0:
        return head
        
    # count lenght and new tail
    length = 1
    tail = head
    while tail.ref:
        tail = tail.ref
        length += 1
    # make circular
    tail.ref = head
    # find new tail and new head
    k = k % length
    steps_to_new_tail = length - k
    new_tail = head
    for _ in range(steps_to_new_tail - 1):
        new_tail = new_tail.ref
    new_head = new_tail.ref
    
    #break the circle
    new_tail.ref = None
    return new_head
    
def swap_pairs(head):
    dummy = Node(0)
    dummy.ref = head
    curr = dummy
    
    while curr.ref and curr.ref.ref:
        first = curr.ref
        second = curr.ref.ref
        
        first.ref = second.ref
        second.ref = first
        curr.ref = second
        curr = first
    
    return dummy.ref
    
L1 =  Linked_list()
list1 = [1,3,5]
for i in list1:
    L1.insert_end(i)
L1.display()
print()
L2 = Linked_list()
list2 = [2,4,6]
for i in list2:
    L2.insert_end(i)
L2.display()
merged_head = merge_lists(L1.head,L2.head)
# Display merged list
print("Merged:")
def display_list(head):
    curr = head
    while curr:
        print(curr.data, end="-->")
        curr = curr.ref
    print("None")

display_list(merged_head)

L3 = Linked_list()
list3 = [1,3,3,4,4,4,5,7,9,9]
for i in list3:
    L3.insert_end(i)
L3.display()
print()
dup_les_list = remove_duplicate(L3.head)
display_list(dup_les_list)

L4 = Linked_list()
list4 = [3,5,2,3,5,6,2]
for i in list4:
    L4.insert_end(i)
duples_list = remove_dup_unsorted(L4.head)
display_list(duples_list)

result = find_nth_from_end(L4.head,2)
print(result)
    
    
# Rebuild L1 for rotation test
L5 = Linked_list()
for val in [1, 2, 3, 4, 5]:
    L5.insert_end(val)
print("Original for rotation:")
L5.display()

rotated = rotate_list(L5.head, 2)
print("After rotating by 2:")
display_list(rotated)

# -----------------------------
# Rebuild another list for swap test
L6 = Linked_list()
for val in [10, 20, 30, 40, 50, 60]:
    L6.insert_end(val)
print("Original for swap:")
L6.display()

swapped = swap_pairs(L6.head)
print("After swapping in pairs:")
display_list(swapped)
    
    
    
    
    
    