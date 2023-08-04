import unittest

from power_set import PowerSet

def create_power_set(values):
    power_set = PowerSet()
    for v in values:
        power_set.put(v)
    return power_set
        
def isequal(power_set, values):
    return power_set.size() == len(values) and all(power_set.get(v) for v in values)

class TestPowerSet(unittest.TestCase):

    def test_init(self):
        power_set = PowerSet()
        self.assertEqual(power_set.size(), 0)
    
    def test_put_n_get(self):
        power_set = PowerSet()
        for v in [1, '2', 3.14]:
            power_set.put(v)
        
        self.assertTrue(power_set.get(1))
        self.assertTrue(power_set.get('2'))
        self.assertTrue(power_set.get(3.14))
        self.assertEqual(power_set.size(), 3)
        
        power_set.put(1)
        power_set.put(3.14)
        self.assertEqual(power_set.size(), 3)
    
    def test_remove(self):
        power_set = PowerSet()
        self.assertFalse(power_set.remove(1))
        
        for v in [1, '2', 3.14, -100]:
            power_set.put(v)
        self.assertEqual(power_set.size(), 4)
        
        self.assertTrue(power_set.remove(1))
        self.assertTrue(power_set.remove(-100))
        
        self.assertFalse(power_set.remove(1))
        self.assertFalse(power_set.remove(42))
        
        self.assertEqual(power_set.size(), 2)

class TestPowerSetIntersection(unittest.TestCase):

    def test_non_intersected(self):
        a = create_power_set([1,2,3])
        b = create_power_set([4,5,6])
        c = a.intersection(b)
        self.assertTrue(isequal(c, []))

    def test_b_in_a(self):
        a = create_power_set([1,2,3,4])
        b = create_power_set([3,4])
        c = a.intersection(b)
        self.assertTrue(isequal(c, [3,4]))

    def test_a_in_b(self):
        a = create_power_set([1,2])
        b = create_power_set([1,2,3,4])
        c = a.intersection(b)
        self.assertTrue(isequal(c, [1,2]))
    
    def test_partly_intersection(self):
        a = create_power_set([1,2,3,4])
        b = create_power_set([3,4,5,6])
        c = a.intersection(b)
        self.assertTrue(isequal(c, [3,4]))

    def test_a_is_b(self):
        a = create_power_set([1,2,3])
        b = create_power_set([1,2,3])
        c = a.intersection(b)
        self.assertTrue(isequal(c, [1,2,3]))

class TestPowerSetUnion(unittest.TestCase):

    def test_non_intersected(self):
        a = create_power_set([1,2,3])
        b = create_power_set([4,5,6])
        c = a.union(b)
        self.assertTrue(isequal(c, [1,2,3,4,5,6]))

    def test_b_in_a(self):
        a = create_power_set([1,2,3,4])
        b = create_power_set([3,4])
        c = a.union(b)
        self.assertTrue(isequal(c, [1,2,3,4]))

    def test_a_in_b(self):
        a = create_power_set([1,2])
        b = create_power_set([1,2,3,4])
        c = a.union(b)
        self.assertTrue(isequal(c, [1,2,3,4]))
    
    def test_partly_intersection(self):
        a = create_power_set([1,2,3,4])
        b = create_power_set([3,4,5,6])
        c = a.union(b)
        self.assertTrue(isequal(c, [1,2,3,4,5,6]))

    def test_a_is_b(self):
        a = create_power_set([1,2,3])
        b = create_power_set([1,2,3])
        c = a.union(b)
        self.assertTrue(isequal(c, [1,2,3]))
    
    def test_union_with_empty(self):
        power_set = PowerSet()
        for i in range(10):
            power_set.put(i)
        
        other_power_set = PowerSet()
        
        union_set = power_set.union(other_power_set)
        self.assertEqual(union_set.size(), 10)
        for i in range(10):
            with self.subTest(i=i):
                self.assertTrue(union_set.get(i))

class TestPowerSetDifference(unittest.TestCase):

    def test_non_intersected(self):
        a = create_power_set([1,2,3])
        b = create_power_set([4,5,6])
        c = a.difference(b)
        self.assertTrue(isequal(c, [1,2,3]))

    def test_b_in_a(self):
        a = create_power_set([1,2,3,4])
        b = create_power_set([3,4])
        c = a.difference(b)
        self.assertTrue(isequal(c, [1,2]))

    def test_a_in_b(self):
        a = create_power_set([1,2])
        b = create_power_set([1,2,3,4])
        c = a.difference(b)
        self.assertTrue(isequal(c, []))
    
    def test_partly_intersection(self):
        a = create_power_set([1,2,3,4])
        b = create_power_set([3,4,5,6])
        c = a.difference(b)
        self.assertTrue(isequal(c, [1,2]))

    def test_a_is_b(self):
        a = create_power_set([1,2,3])
        b = create_power_set([1,2,3])
        c = a.difference(b)
        self.assertTrue(isequal(c, []))

class TestPowerSetIsSubset(unittest.TestCase):

    def test_non_intersected(self):
        a = create_power_set([1,2,3])
        b = create_power_set([4,5,6])
        self.assertFalse(a.issubset(b))

    def test_b_in_a(self):
        a = create_power_set([1,2,3,4])
        b = create_power_set([3,4])
        self.assertTrue(a.issubset(b))
    
    def test_a_in_b(self):
        a = create_power_set([1,2])
        b = create_power_set([1,2,3,4])
        self.assertFalse(a.issubset(b))
    
    def test_partly_intersection(self):
        a = create_power_set([1,2,3,4])
        b = create_power_set([3,4,5,6])
        self.assertFalse(a.issubset(b))

    def test_a_is_b(self):
        a = create_power_set([1,2,3])
        b = create_power_set([1,2,3])
        self.assertTrue(a.issubset(b))

class TestPowerSetEfficiency(unittest.TestCase):

    def setUp(self):
        self.set = PowerSet()
        for i in range(20000):
            self.set.put(i)

        self.other_set = PowerSet()
        for i in range(13000, 23000):
            self.other_set.put(i)


    def test_efficiency_put(self):
        self.set.put(1)
        self.set.put(100)
        self.set.put(100000)
    
    def test_efficiency_get(self):
        self.set.get(5)
        self.set.get(500)
        self.set.get(50000)
    
    def test_efficiency_remove(self):
        self.set.remove(7)
        self.set.remove(700)
        self.set.remove(70000)
    
    def test_efficiency_relations(self):
        self.assertEqual(self.set.intersection(self.other_set).size(), 7000)
        self.assertEqual(self.set.union(self.other_set).size(), 23000)
        self.assertEqual(self.set.difference(self.other_set).size(), 13000)
        self.assertFalse(self.set.issubset(self.other_set))

