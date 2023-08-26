class SimpleTreeNode:
	
    def __init__(self, val, parent = None):
        self.NodeValue = val # значение в узле
        self.Parent = parent # родитель или None для корня
        self.Children = [] # список дочерних узлов
	
class SimpleTree:

    def __init__(self, root):
        self.Root = root # корень, может быть None
	
    def AddChild(self, ParentNode, NewChild):
        NewChild.Parent = ParentNode
        ParentNode.Children.append(NewChild)
  
    def DeleteNode(self, NodeToDelete):
        NodeToDelete.Parent.Children.remove(NodeToDelete)
        NodeToDelete.Parent = None

    # traversal tree and call f(node) for every node
    def _dfs(self, f):
        # non-recursive version dfs
        if self.Root is None:
            return
        
        nodes_stack = [self.Root]
        while len(nodes_stack) > 0:
            curr_node = nodes_stack.pop()
            f(curr_node)
            nodes_stack.extend(curr_node.Children)
    
    def GetAllNodes(self):
        all_nodes = []
        self._dfs(lambda node : all_nodes.append(node))
        return all_nodes

    def FindNodesByValue(self, val):
        finded_nodes = []
        def _append_equal(node):
            nonlocal finded_nodes
            if node.NodeValue == val: 
                finded_nodes.append(node)
        
        self._dfs(_append_equal)
        return finded_nodes
   
    def MoveNode(self, OriginalNode, NewParent):
        self.DeleteNode(OriginalNode)
        self.AddChild(NewParent, OriginalNode)
   
    def Count(self):
        nodes_count = 0
        def _count(node):
            nonlocal nodes_count
            nodes_count += 1
        
        self._dfs(_count)
        return nodes_count

    def LeafCount(self):
        leafs_count = 0
        def _leaf_count(node):
            nonlocal leafs_count
            if len(node.Children) == 0: 
                leafs_count += 1
        
        self._dfs(_leaf_count)
        return leafs_count
    
    def AssignTreeLevel(self, init_lvl = 0):
        def _set_tree_lvl(node):
            nonlocal init_lvl
            node.NodeValue = node.Parent.NodeValue + 1 if node.Parent else init_lvl
        self._dfs(_set_tree_lvl)
    
    def __AssignTreeLevelRecursive(self, node, init_lvl):
        node.NodeValue = init_lvl
        for child_node in node.Children:
            self.__AssignTreeLevelRecursive(child_node, init_lvl+1)
    
    def AssignTreeLevelRecursive(self, init_lvl = 0):
        if self.Root is None: 
            return
        
        self.__AssignTreeLevelRecursive(self.Root, init_lvl)
    
    def EvenTrees(self):
        
        def __possible_cuts(node): # [p_node, node,..], nodes_count
            if len(node.Children) == 0:
                return [], 1
            
            nodes_count = 0
            cuts = []
            children_cuts = []
            for child in node.Children:
                child_cuts, child_nodes_count =__possible_cuts(child)
                children_cuts.extend(child_cuts)
                nodes_count += child_nodes_count
                if child_nodes_count % 2 == 0:
                    cuts.extend([node, child])
            cuts.extend(children_cuts)
            return cuts, nodes_count + 1
        
        if self.Root is None:
            return []
        
        possible_cuts, count = __possible_cuts(self.Root)
        return possible_cuts if count % 2 == 0 else []
