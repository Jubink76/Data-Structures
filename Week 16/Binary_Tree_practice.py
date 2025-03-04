class Node():
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def in_order(root):
    if root:
        in_order(root.left)
        print(root.key,end=" ")
        in_order(root.right)

def find_depth(root):
    if not root:
        return 0
    left_depth = find_depth(root.left)
    right_depth = find_depth(root.right)
    return max(left_depth,right_depth) + 1

def count_node(root):
    if not root:
        return 0
    return 1 + count_node(root.left) + count_node(root.right)

def find_max(root):
    if not root:
        return 0
    left_max = find_max(root.left)
    right_max = find_max(root.right)
    return max(root.key,left_max,right_max)

def find_min(root):
    if not root:
        return float('inf')
    left_min = find_min(root.left)
    right_min = find_min(root.right)
    return min(root.key, left_min, right_min)

def find_sum(root):
    if not root:
        return 0
    left_sum = find_sum(root.left)
    right_sum = find_sum(root.right)
    return (root.key + left_sum + right_sum)

def count_leaf(root):
    if not root:
        return 0
    if root.left is None and root.right is None:
        return 1 
    return count_leaf(root.left) + count_leaf(root.right)

def full_node_count(root):
    if not root:
        return 0
    count = full_node_count(root.left) + full_node_count(root.right)
    if root.left is not None and root.right is not None:
        count += 1
    return count

def count_half(root):
    if not root:
        return 0
    count = count_half(root.left) + count_half(root.right)
    if (root.left and not root.right) or (root.right and not root.left):
        count += 1
    return count 

def lca(root,p,q):
    if root is None or root.key == p or root.key == q:
        return root
    left = lca(root.left,p,q)
    right = lca(root.right,p,q)
    if left and right:
        return root
    return left if left else right

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(5)
root.left.right = Node(7)
in_order(root)
print("Depthe of the tree is :",find_depth(root))
print("Count of nodes in the tree:",count_node(root))
print("Max of tree:",find_max(root))
print("Min of tree:",find_min(root))
print("sum of tree:",find_sum(root))
print("Count of leaf node:",count_leaf(root))
print("no of full nodes:",full_node_count(root))
print("no of halfnodes:",count_half(root))
print("lca of two nodes",lca(root,5,2).key)