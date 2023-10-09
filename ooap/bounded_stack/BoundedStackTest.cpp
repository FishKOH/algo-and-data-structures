#include <catch.hpp>

#include "BoundedStack.h"

TEST_CASE("construct")
{
    auto bStack = BoundedStack<int>(3u);
    CHECK(bStack.size() == 0);
}

TEST_CASE("push")
{
    auto bStack = BoundedStack<int>(3u);
    CHECK(bStack.getPushStatus() == BoundedStack<int>::PushStatus::NotCalled);
    bStack.push(8);
    CHECK(bStack.getPushStatus() == BoundedStack<int>::PushStatus::Ok);
    bStack.push(8);
    bStack.push(8);
    CHECK(bStack.getPushStatus() == BoundedStack<int>::PushStatus::Ok);
    bStack.push(8);
    CHECK(bStack.getPushStatus() == BoundedStack<int>::PushStatus::OverflowStack);
}

TEST_CASE("pop")
{
    auto bStack = BoundedStack<int>(3u);
    CHECK(bStack.getPopStatus() == BoundedStack<int>::PopStatus::NotCalled);
    bStack.pop();
    CHECK(bStack.getPopStatus() == BoundedStack<int>::PopStatus::EmptyStack);
    bStack.push(8);
    bStack.pop();
    CHECK(bStack.getPopStatus() == BoundedStack<int>::PopStatus::Ok);
}

TEST_CASE("peek")
{
    auto bStack = BoundedStack<int>(3u);
    CHECK(bStack.getPeekStatus() == BoundedStack<int>::PeekStatus::NotCalled);
    bStack.peek();
    CHECK(bStack.getPeekStatus() == BoundedStack<int>::PeekStatus::EmptyStack);
    bStack.push(8);
    CHECK(bStack.peek() == 8);
    CHECK(bStack.getPeekStatus() == BoundedStack<int>::PeekStatus::Ok);
}
