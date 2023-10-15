#include <catch.hpp>

#include "LinkedList.h"

using namespace linked_list;

TEST_CASE("linked list")
{
    LinkedList<int> list;
    CHECK(list.size() == 0);
    list.head();
    CHECK(list.get_head_status() == HeadStatus::EmptyList);
    list.tail();
    CHECK(list.get_tail_status() == TailStatus::EmptyList);
    list.right();
    CHECK(list.get_right_status() == RightStatus::EmptyList);
    list.put_right(8);
    CHECK(list.get_put_right_status() == PutRightStatus::EmptyList);
    list.put_left(8);
    CHECK(list.get_put_left_status() == PutLeftStatus::EmptyList);
    list.remove();
    CHECK(list.get_remove_status() == RemoveStatus::EmptyList);
    list.replace(8);
    CHECK(list.get_replace_status() == ReplaceStatus::EmptyList);
    list.find(8);
    CHECK(list.get_find_status() == FindStatus::EmptyList);
    list.get();
    CHECK(list.get_get_status() == GetStatus::EmptyList);
    CHECK(list.is_head() == false);
    CHECK(list.is_tail() == false);
    CHECK(list.is_value() == false);

    list.add_tail(42);
    CHECK(list.size() == 1);
    CHECK(list.get() == 42);
    CHECK(list.is_head());
    CHECK(list.is_tail());
    CHECK(list.is_value());

    list.put_right(8);
    list.put_left(1);
    CHECK(list.size() == 3);
    list.head();
    CHECK(list.is_head());
    CHECK(list.get() == 42);
    list.right();
    CHECK(list.get() == 1);
    list.right();
    CHECK(list.get() == 8);
    CHECK(list.is_tail());

    list.replace(13);
    CHECK(list.get() == 13);
    CHECK(list.is_tail());

    list.remove();
    CHECK(list.size() == 2);
    CHECK(list.get() == 1);
    CHECK(list.is_tail());

    list.add_tail(42);
    list.head();
    list.find(42);
    CHECK(list.is_tail());
    list.find(42);
    CHECK(list.get_find_status() == FindStatus::NotFound);

    list.remove_all(42);
    CHECK(list.size() == 1);
    CHECK(list.get() == 1);
    CHECK(list.is_head());
    CHECK(list.is_tail());
    CHECK(list.is_value());
}

TEST_CASE("2ll")
{
    TwoWayList<int> list;
    CHECK(list.size() == 0);

    list.add_tail(1);
    list.add_tail(2);
    list.add_tail(3);

    list.right();
    list.right();
    list.right();
    list.left();
    list.left();
    list.left();
    CHECK(list.size() == 3);
    CHECK(list.is_head());
    CHECK(list.is_tail() == false);
    CHECK(list.is_value());
}
