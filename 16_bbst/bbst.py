class BSTNode:
    
    def __init__(self, key, parent):
        self.NodeKey = key # ключ узла
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок
        self.Level = 0 # уровень узла
    
class BalancedBST:
    
    def __init__(self):
        self.Root = None # корень дерева

    def GenerateTree(self, a):
        def __genTree(root_node, subarray, lvl):
            if len(subarray) == 0:
                return None
            
            mid = len(subarray)//2
            node = BSTNode(subarray[mid], root_node)
            node.Level = lvl
            node.LeftChild = __genTree(node, subarray[:mid], lvl+1)
            node.RightChild = __genTree(node, subarray[mid+1:], lvl+1)
            return node
        
        self.Root = __genTree(None, sorted(a), 0)
    
    def depth(self, root_node):
        if root_node is None:
            return 0
        return max(self.depth(root_node.LeftChild), self.depth(root_node.RightChild)) + 1
    
    def IsBalanced(self, root_node):
        if root_node is None:
            return True
        
        return (
            self.IsBalanced(root_node.LeftChild) and 
            self.IsBalanced(root_node.RightChild) and 
            abs(self.depth(root_node.LeftChild) - 
                self.depth(root_node.RightChild)) < 2)
