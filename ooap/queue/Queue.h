#include <list>

namespace queue {

enum class DequeueStatus {
    NotCalled,
    Ok,
    EmptyQueue
};
using FrontStatus = DequeueStatus;

template <class T>
class AbstractQueue {
public:
    // КОНСТРУКТОР:
    // постусловие: создаёт новый пустой массив
    // virtual AbstractQueue();

    // КОМАНДЫ:

    //постусловие: в конец очереди добавлен элемент
    virtual void queue(T value) = 0;

    //предусловие:  очередь не пуста
    //постусловие: элемент из начала очереди удалён
    virtual void dequeue() = 0;

    // ЗАПРОСЫ:

    //возвращает элемент из начала очереди
    //предусловие:  очередь не пуста
    virtual T front() const = 0;

    virtual unsigned int size() const = 0;

    //ЗАПРОСЫ-СТАТУСЫ:

    virtual DequeueStatus getDequeueStatus() const = 0;
    virtual FrontStatus getFrontStatus() const = 0;
};

template <class T>
class Queue : public AbstractQueue<T> {
public:
    Queue() = default;

    void queue(T value) override
    {
        storage_.push_back(value);
    }
    void dequeue() override
    {
        if (storage_.empty()) {
            dequeueStatus_ = DequeueStatus::EmptyQueue;
            return;
        }
        storage_.pop_front();
        dequeueStatus_ = DequeueStatus::Ok;
    }
    T front() const override
    {
        if (storage_.empty()) {
            frontStatus_ = FrontStatus::EmptyQueue;
            return T();
        }
        frontStatus_ = FrontStatus::Ok;
        return storage_.front();
    }
    DequeueStatus getDequeueStatus() const override
    {
        return dequeueStatus_;
    }
    FrontStatus getFrontStatus() const override
    {
        return frontStatus_;
    }

    unsigned int size() const override
    {
        return storage_.size();
    }

private:
    std::list<T> storage_;

    DequeueStatus dequeueStatus_ = DequeueStatus::NotCalled;
    mutable FrontStatus frontStatus_ = FrontStatus::NotCalled;
};

} // end of namespace dyn_array
