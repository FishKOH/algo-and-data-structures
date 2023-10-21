#include <catch.hpp>

#include "Queue.h"

using namespace queue;

TEST_CASE("queue")
{
    Queue<int> queue;
    CHECK(queue.size() == 0);

    queue.queue(8);
    CHECK(queue.size() == 1);
    CHECK(queue.front() == 8);

    CHECK(queue.getFrontStatus() == FrontStatus::Ok);

    queue.dequeue();
    CHECK(queue.getDequeueStatus() == DequeueStatus::Ok);
    CHECK(queue.size() == 0);

    queue.dequeue();
    CHECK(queue.getDequeueStatus() == DequeueStatus::EmptyQueue);
    queue.front();
    CHECK(queue.getFrontStatus() == FrontStatus::EmptyQueue);
}
