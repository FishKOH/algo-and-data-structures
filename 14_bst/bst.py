class BSTNode:
    
    def __init__(self, key, val, parent):
        self.NodeKey = key # ключ узла
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок


class BSTFind: # промежуточный результат поиска

    def __init__(self):
        self.Node = None # None если 
        # в дереве вообще нету узлов

        self.NodeHasKey = False # True если узел найден
        self.ToLeft = False # True, если родительскому узлу надо 
        # добавить новый узел левым потомком

class BST:

    def __init__(self, node : BSTNode):
        self.Root = node # корень дерева, или None
        if self.Root is not None:
            self.Root.Parent = None

    def FindNodeByKey(self, key) -> BSTFind:
        find_result = BSTFind()
        if self.Root is None:
            return find_result
        
        curr_node = self.Root
        while curr_node is not None:
            if key == curr_node.NodeKey:
                find_result.Node = curr_node
                find_result.NodeHasKey = True
                return find_result
            
            if key < curr_node.NodeKey:
                next_node = curr_node.LeftChild
            else:
                next_node = curr_node.RightChild
            
            if next_node is None:
                find_result.Node = curr_node
                find_result.NodeHasKey = False
                find_result.ToLeft = key < curr_node.NodeKey
                return find_result
            
            curr_node = next_node
        return None 

    def AddKeyValue(self, key, val) -> bool:
        find_result = self.FindNodeByKey(key)
        if find_result.Node is None:
            self.Root = BSTNode(key, val, None)
            return True
        
        if find_result.NodeHasKey:
            return False

        if find_result.ToLeft:
            find_result.Node.LeftChild = BSTNode(key, val, find_result.Node)
        else:
            find_result.Node.RightChild = BSTNode(key, val, find_result.Node)

        return True
  
    def FindMinMax(self, FromNode : BSTNode, FindMax : bool) -> BSTNode:
        def next_node(curr_node, FindMax):
            return curr_node.RightChild if FindMax else curr_node.LeftChild
        
        if FromNode is None:
            return None
        
        curr_node = FromNode
        while next_node(curr_node, FindMax) is not None:
            curr_node = next_node(curr_node, FindMax)
        return curr_node        
    
    # some strange, ignore this
    FinMinMax = FindMinMax
    
    def __reset(self, old_node : BSTNode , new_node : BSTNode):
        parent_node = old_node.Parent
        if new_node is not None:
            new_node.Parent = parent_node
            
        if parent_node is None: # is root
            self.Root = new_node
            return
        
        to_left = old_node.NodeKey < parent_node.NodeKey
        if to_left:
            parent_node.LeftChild = new_node
        else:
            parent_node.RightChild = new_node
    
    def __isolate_node(self, node):
        node.Parent = None
        node.LeftChild = None
        node.RightChild = None
    
    def __delete_node_without_all_children(self, delete_node):
        successor_node = None
        if delete_node.LeftChild is None:
            successor_node = delete_node.RightChild
        if delete_node.RightChild is None:
            successor_node = delete_node.LeftChild        
        #if both is None: successor_node = None
        
        self.__reset(delete_node, successor_node)
        self.__isolate_node(delete_node)
    
    def DeleteNodeByKey(self, key) -> bool:
        find_result = self.FindNodeByKey(key)
        if find_result.Node is None or not find_result.NodeHasKey:
            return False
        
        delete_node = find_result.Node
        
        if delete_node.LeftChild is None or  delete_node.RightChild is None:
            self.__delete_node_without_all_children(delete_node)
            return True
        
        successor_node = self.FindMinMax(FromNode = delete_node.RightChild, FindMax = False)
        self.__reset(successor_node, successor_node.RightChild)
        
        successor_node.LeftChild = delete_node.LeftChild
        successor_node.LeftChild.Parent = successor_node
        
        successor_node.RightChild = delete_node.RightChild
        if successor_node.RightChild is not None:
            successor_node.RightChild.Parent = successor_node
        
        self.__reset(delete_node, successor_node)
        self.__isolate_node(delete_node)
        return True
    
    # traversal tree and call f(node) for every node
    def _dfs(self, f):
        # non-recursive version dfs
        if self.Root is None:
            return
        
        nodes_stack = [self.Root]
        while len(nodes_stack) > 0:
            curr_node = nodes_stack.pop()
            f(curr_node)
            for child in [curr_node.LeftChild, curr_node.RightChild]:
                if child is not None:
                    nodes_stack.append(child)
    
    def Count(self) -> int:
        nodes_count = 0
        def _count(node):
            nonlocal nodes_count
            nodes_count += 1
        
        self._dfs(_count)
        return nodes_count
