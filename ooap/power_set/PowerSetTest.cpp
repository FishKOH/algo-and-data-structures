#include <catch.hpp>

#include "PowerSet.h"

using namespace power_set;

template <class T>
PowerSet<T> createPowerSet(std::initializer_list<T> values)
{
    PowerSet<T> powerSet;
    for (auto value : values)
        powerSet.put(value);
    return powerSet;
}

template <class T>
bool isEqual(const PowerSet<T>& powerSet, std::initializer_list<T> values)
{
    return std::all_of(values.begin(), values.end(), [&powerSet](T value) {
        return powerSet.has(value);
    });
}

TEST_CASE("PowerSet::intersection")
{
    SECTION("non intersected")
    {
        PowerSet<int> a = createPowerSet({ 1, 2, 3 });
        PowerSet<int> b = createPowerSet({ 4, 5, 6 });
        auto c = a.makeIntersection(b);
        CHECK(isEqual(c, {}));
    }
    SECTION("b_in_a")
    {
        PowerSet<int> a = createPowerSet({ 1, 2, 3, 4 });
        PowerSet<int> b = createPowerSet({ 3, 4 });
        auto c = a.makeIntersection(b);
        CHECK(isEqual(c, { 3, 4 }));
    }
    SECTION("a_in_b")
    {
        PowerSet<int> a = createPowerSet({ 1, 2 });
        PowerSet<int> b = createPowerSet({ 1, 2, 3, 4 });
        auto c = a.makeIntersection(b);
        CHECK(isEqual(c, { 1, 2 }));
    }
    SECTION("partly_intersection")
    {
        PowerSet<int> a = createPowerSet({ 1, 2, 3, 4 });
        PowerSet<int> b = createPowerSet({ 3, 4, 5, 6 });
        auto c = a.makeIntersection(b);
        CHECK(isEqual(c, { 3, 4 }));
    }
    SECTION("a_is_b")
    {
        PowerSet<int> a = createPowerSet({ 1, 2, 3 });
        PowerSet<int> b = createPowerSet({ 1, 2, 3 });
        auto c = a.makeIntersection(b);
        CHECK(isEqual(c, { 1, 2, 3 }));
    }
}

TEST_CASE("PowerSet::difference")
{
    SECTION("non intersected")
    {
        PowerSet<int> a = createPowerSet({ 1, 2, 3 });
        PowerSet<int> b = createPowerSet({ 4, 5, 6 });
        auto c = a.makeDifference(b);
        CHECK(isEqual(c, { 1, 2, 3 }));
    }
    SECTION("b_in_a")
    {
        PowerSet<int> a = createPowerSet({ 1, 2, 3, 4 });
        PowerSet<int> b = createPowerSet({ 3, 4 });
        auto c = a.makeDifference(b);
        CHECK(isEqual(c, { 1, 2 }));
    }
    SECTION("a_in_b")
    {
        PowerSet<int> a = createPowerSet({ 1, 2 });
        PowerSet<int> b = createPowerSet({ 1, 2, 3, 4 });
        auto c = a.makeDifference(b);
        CHECK(isEqual(c, {}));
    }
    SECTION("partly_intersection")
    {
        PowerSet<int> a = createPowerSet({ 1, 2, 3, 4 });
        PowerSet<int> b = createPowerSet({ 3, 4, 5, 6 });
        auto c = a.makeDifference(b);
        CHECK(isEqual(c, { 1, 2 }));
    }
    SECTION("a_is_b")
    {
        PowerSet<int> a = createPowerSet({ 1, 2, 3 });
        PowerSet<int> b = createPowerSet({ 1, 2, 3 });
        auto c = a.makeDifference(b);
        CHECK(isEqual(c, {}));
    }
}

TEST_CASE("PowerSet::union")
{
    SECTION("non intersected")
    {
        PowerSet<int> a = createPowerSet({ 1, 2, 3 });
        PowerSet<int> b = createPowerSet({ 4, 5, 6 });
        auto c = a.makeUnion(b);
        CHECK(isEqual(c, { 1, 2, 3, 4, 5, 6 }));
    }
    SECTION("b_in_a")
    {
        PowerSet<int> a = createPowerSet({ 1, 2, 3, 4 });
        PowerSet<int> b = createPowerSet({ 3, 4 });
        auto c = a.makeUnion(b);
        CHECK(isEqual(c, { 1, 2, 3, 4 }));
    }
    SECTION("a_in_b")
    {
        PowerSet<int> a = createPowerSet({ 1, 2 });
        PowerSet<int> b = createPowerSet({ 1, 2, 3, 4 });
        auto c = a.makeUnion(b);
        CHECK(isEqual(c, { 1, 2, 3, 4 }));
    }
    SECTION("partly_intersection")
    {
        PowerSet<int> a = createPowerSet({ 1, 2, 3, 4 });
        PowerSet<int> b = createPowerSet({ 3, 4, 5, 6 });
        auto c = a.makeUnion(b);
        CHECK(isEqual(c, { 1, 2, 3, 4, 5, 6 }));
    }
    SECTION("a_is_b")
    {
        PowerSet<int> a = createPowerSet({ 1, 2, 3 });
        PowerSet<int> b = createPowerSet({ 1, 2, 3 });
        auto c = a.makeUnion(b);
        CHECK(isEqual(c, { 1, 2, 3 }));
    }
}

TEST_CASE("PowerSet::isSubset")
{
    SECTION("non intersected")
    {
        PowerSet<int> a = createPowerSet({ 1, 2, 3 });
        PowerSet<int> b = createPowerSet({ 4, 5, 6 });
        CHECK_FALSE(a.isSubset(b));
    }
    SECTION("b_in_a")
    {
        PowerSet<int> a = createPowerSet({ 1, 2, 3, 4 });
        PowerSet<int> b = createPowerSet({ 3, 4 });
        CHECK(a.isSubset(b));
    }
    SECTION("a_in_b")
    {
        PowerSet<int> a = createPowerSet({ 1, 2 });
        PowerSet<int> b = createPowerSet({ 1, 2, 3, 4 });
        CHECK_FALSE(a.isSubset(b));
    }
    SECTION("partly_intersection")
    {
        PowerSet<int> a = createPowerSet({ 1, 2, 3, 4 });
        PowerSet<int> b = createPowerSet({ 3, 4, 5, 6 });
        CHECK_FALSE(a.isSubset(b));
    }
    SECTION("a_is_b")
    {
        PowerSet<int> a = createPowerSet({ 1, 2, 3 });
        PowerSet<int> b = createPowerSet({ 1, 2, 3 });
        CHECK(a.isSubset(b));
    }
    /*
 * class TestPowerSetIsSubset(unittest.TestCase):

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
 */
}
