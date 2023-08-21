def GenerateBBSTArray(array):
    def _gbst(abst, abst_index, array, l, r):
        if l >= r:
            return
        
        mid = (l + r) // 2
        abst[abst_index] = array[mid]
        _gbst(abst, abst_index * 2 + 1, array, l, mid)
        _gbst(abst, abst_index * 2 + 2, array, mid+1, r)
    
    def min_size(n):
        size = 1
        while size < n:
            size = (size + 1) * 2 - 1
        return size
    
    
    abst_size = min_size(len(array))
    abst = [None] * abst_size
    _gbst(abst, 0, sorted(array), 0, len(array))
    return abst
