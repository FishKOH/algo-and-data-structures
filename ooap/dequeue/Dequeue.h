#include <list>

namespace queues {

enum class RemoveFrontStatus {
    NotCalled,
    Ok,
    EmptyQueue
};
using FrontStatus = RemoveFrontStatus;

template <class T>
class AbstractParentQueue {
public:
    // КОНСТРУКТОР:
    // постусловие: создаёт новую пустую очередь
    // virtual AbstractParentQueue();

    // КОМАНДЫ:

    //постусловие: в конец очереди добавлен элемент
    virtual void put_tail(T value) = 0;

    //предусловие:  очередь не пуста
    //постусловие: элемент из начала очереди удалён
    virtual void remove_front() = 0;

    // ЗАПРОСЫ:

    //возвращает элемент из начала очереди
    //предусловие:  очередь не пуста
    virtual T front() const = 0;

    virtual unsigned int size() const = 0;

    //ЗАПРОСЫ-СТАТУСЫ:

    virtual RemoveFrontStatus getRemoveFrontStatus() const = 0;
    virtual FrontStatus getFrontStatus() const = 0;
};

template <class T>
class AbstractQueue : public AbstractParentQueue<T> {
public:
    // КОНСТРУКТОР:
    // постусловие: создаёт новую пустую очередь
    // virtual AbstractQueue();
};

enum class RemoveTailStatus {
    NotCalled,
    Ok,
    EmptyDequeue
};
using TailStatus = RemoveTailStatus;

template <class T>
class AbstractDequeue : virtual public AbstractParentQueue<T> {
public:
    // КОНСТРУКТОР:
    // постусловие: создаёт новую пустую двустороннюю очередь
    // virtual AbstractDequeue();

    // КОМАНДЫ:

    //постусловие: в начало очереди добавлен элемент
    virtual void put_front(T value) = 0;

    //предусловие:  очередь не пуста
    //постусловие: элемент в конце очереди удалён
    virtual void remove_tail() = 0;

    // ЗАПРОСЫ:

    //возвращает элемент c конца очереди
    //предусловие:  очередь не пуста
    virtual T tail() const = 0;

    //ЗАПРОСЫ-СТАТУСЫ:

    virtual RemoveTailStatus getRemoveTailStatus() const = 0;
    virtual TailStatus getTailStatus() const = 0;
};

template <class T>
class ParentQueue : virtual public AbstractParentQueue<T> {
public:
    ParentQueue() = default;

    void put_tail(T value) override
    {
        storage_.push_back(value);
    }
    void remove_front() override
    {
        if (storage_.empty()) {
            RemoveFrontStatus_ = RemoveFrontStatus::EmptyQueue;
            return;
        }
        storage_.pop_front();
        RemoveFrontStatus_ = RemoveFrontStatus::Ok;
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
    RemoveFrontStatus getRemoveFrontStatus() const override
    {
        return RemoveFrontStatus_;
    }
    FrontStatus getFrontStatus() const override
    {
        return frontStatus_;
    }

    unsigned int size() const override
    {
        return storage_.size();
    }

protected:
    std::list<T> storage_;

private:
    RemoveFrontStatus RemoveFrontStatus_ = RemoveFrontStatus::NotCalled;
    mutable FrontStatus frontStatus_ = FrontStatus::NotCalled;
};

template <class T>
class Queue : public ParentQueue<T> {
public:
    Queue() = default;
};

template <class T>
class Dequeue : public ParentQueue<T>, public AbstractDequeue<T> {
public:
    Dequeue() = default;

    void put_front(T value) override
    {
        ParentQueue<T>::storage_.push_front(value);
    }

    void remove_tail() override
    {
        if (ParentQueue<T>::storage_.empty()) {
            removeTailStatus_ = RemoveTailStatus::EmptyDequeue;
            return;
        }
        removeTailStatus_ = RemoveTailStatus::Ok;
        ParentQueue<T>::storage_.pop_back();
    }
    T tail() const override
    {
        if (ParentQueue<T>::storage_.empty()) {
            tailStatus_ = TailStatus::EmptyDequeue;
            return T();
        }
        tailStatus_ = TailStatus::Ok;
        return ParentQueue<T>::storage_.back();
    }
    RemoveTailStatus getRemoveTailStatus() const override
    {
        return removeTailStatus_;
    }
    TailStatus getTailStatus() const override
    {
        return tailStatus_;
    }

private:
    RemoveTailStatus removeTailStatus_ = RemoveTailStatus::NotCalled;
    mutable TailStatus tailStatus_ = TailStatus::NotCalled;
};

} // end of namespace dyn_array
