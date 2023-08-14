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

    def _dfs(self, f):
        # non-recursive version dfs
        if self.Root is None:
            return
        
        node_stack = [self.Root]
        while len(node_stack) > 0:
            curr_node = node_stack.pop()
            f(curr_node)
            for node in curr_node.Children:
                node_stack.append(node)
    
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
