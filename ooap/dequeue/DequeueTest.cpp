#include <catch.hpp>

#include "Dequeue.h"

using namespace queues;

TEST_CASE("queue")
{
    Queue<int> queue;
    CHECK(queue.size() == 0);

    queue.put_tail(8);
    CHECK(queue.size() == 1);
    CHECK(queue.front() == 8);

    CHECK(queue.getFrontStatus() == FrontStatus::Ok);

    queue.remove_front();
    CHECK(queue.getRemoveFrontStatus() == RemoveFrontStatus::Ok);
    CHECK(queue.size() == 0);

    queue.remove_front();
    CHECK(queue.getRemoveFrontStatus() == RemoveFrontStatus::EmptyQueue);
    queue.front();
    CHECK(queue.getFrontStatus() == FrontStatus::EmptyQueue);
}

TEST_CASE("dequeue")
{
    Dequeue<int> dequeue;
    CHECK(dequeue.size() == 0);

    dequeue.put_front(-1);
    dequeue.put_front(-2);
    dequeue.put_tail(1);
    dequeue.put_tail(2);
    dequeue.put_tail(3);
    CHECK(dequeue.size() == 5);

    CHECK(dequeue.front() == -2);
    dequeue.remove_front();
    CHECK(dequeue.front() == -1);
    dequeue.remove_front();

    CHECK(dequeue.tail() == 3);
    dequeue.remove_tail();
    CHECK(dequeue.getRemoveTailStatus() == RemoveTailStatus::Ok);
    CHECK(dequeue.getTailStatus() == TailStatus::Ok);

    CHECK(dequeue.tail() == 2);
    dequeue.remove_tail();

    CHECK(dequeue.tail() == 1);
    dequeue.remove_tail();
    CHECK(dequeue.getRemoveTailStatus() == RemoveTailStatus::Ok);
    CHECK(dequeue.getTailStatus() == TailStatus::Ok);
    CHECK(dequeue.size() == 0);

    dequeue.remove_front();
    CHECK(dequeue.getRemoveFrontStatus() == RemoveFrontStatus::EmptyQueue);
    dequeue.remove_tail();
    CHECK(dequeue.getRemoveTailStatus() == RemoveTailStatus::EmptyDequeue);
}
