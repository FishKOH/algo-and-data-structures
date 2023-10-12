#include <list>

template <class T>
class BoundedStack {
public:
    enum class PeekStatus {
        NotCalled,
        Ok,
        EmptyStack
    };
    enum class PopStatus {
        NotCalled,
        Ok,
        EmptyStack
    };
    enum class PushStatus {
        NotCalled,
        Ok,
        OverflowStack
    };

public:
    //постусловие: создан новый пустой стек
    BoundedStack(unsigned int maxSize = 32)
        : maxSize_(maxSize)
    {
        clear();
    }

    //предусловие: размер стека меньше максимального размера
    //постусловие: в стек добавлено новое значение
    void push(T value)
    {
        if (storage_.size() >= maxSize_) {
            pushStatus_ = PushStatus::OverflowStack;
        } else {
            pushStatus_ = PushStatus::Ok;
            storage_.push_back(value);
        }
    }

    //предусловие: стек не пустой
    //постусловие: из стека удалён верхний элемент
    void pop()
    {
        if (storage_.empty()) {
            popStatus_ = PopStatus::EmptyStack;
        }
        else {
            popStatus_ = PopStatus::Ok;
            storage_.pop_back();
        }
    }

    //постусловие: из стека удалены все элементы
    void clear()
    {
        storage_.clear();
        peekStatus_ = PeekStatus::NotCalled;
        popStatus_  = PopStatus::NotCalled;
        pushStatus_ = PushStatus::NotCalled;
    }

    //предусловие: стек не пустой
    T peek()
    {
        if (storage_.empty()) {
            peekStatus_ = PeekStatus::EmptyStack;
            return T{};
        }
        peekStatus_ = PeekStatus::Ok;
        return storage_.back();
    }

    int size() const
    {
        return storage_.size();
    }

    PeekStatus getPeekStatus() const
    {
        return peekStatus_;
    }

    PopStatus getPopStatus() const
    {
        return popStatus_;
    }

    PushStatus getPushStatus() const
    {
        return pushStatus_;
    }

private:
    std::list<T> storage_;
    unsigned int maxSize_;
    PeekStatus peekStatus_;
    PopStatus  popStatus_;
    PushStatus pushStatus_;
};
