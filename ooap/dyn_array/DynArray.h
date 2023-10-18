#include <algorithm>

namespace dyn_array {

enum class AppendStatus {
    NotCalled,
    Ok,
    IncorrectIndex
};
using ReplaceStatus = AppendStatus;
using InsertStatus = AppendStatus;
using RemoveStatus = AppendStatus;
using GetStatus = AppendStatus;

template <class T>
class AbstractDynArray {
public:
    // КОНСТРУКТОР:
    // постусловие: создаёт новый пустой массив
    // virtual AbstractDynArray();

    // КОМАНДЫ:

    //постусловие: в конец массива добавлено заданное значение
    virtual void append(T value) = 0;

    //предусловие:  0<i<size
    //постусловие1: по заданному индексу распологается заданное значение
    virtual void replace(T value, unsigned int i) = 0;

    //предусловие:  0<i<size
    //постусловие1: по заданному индексу распологается заданное значение
    //постусловие2: элементы после заданного индекса, если такие имеются, сдвигаются "вправо"
    virtual void insert(T value, unsigned int i) = 0;

    //предусловие:  0<i<size
    //постусловие1: по заданному индексу распологается заданное значение
    //постусловие2: элементы после заданного индекса, если такие имеются, сдвигаются "влево"
    virtual void remove(unsigned int i) = 0;

    // ЗАПРОСЫ:
    //предусловие:  0<i<size
    virtual T get(unsigned int i) const = 0;

    virtual unsigned int size() const = 0;

    //ЗАПРОСЫ-СТАТУСЫ:

    virtual AppendStatus getAppendStatus() const = 0;
    virtual ReplaceStatus getReplaceStatus() const = 0;
    virtual InsertStatus getInsertStatus() const = 0;
    virtual RemoveStatus getRemoveStatus() const = 0;
    virtual GetStatus getGetStatus() const = 0;
};

template <class T>
class DynArray : public AbstractDynArray<T> {
public:
    DynArray()
        : capacity_(kMinimalCapacity)
        , storage_(new T[kMinimalCapacity])
    {
    }
    ~DynArray()
    {
        delete[] storage_;
    }
    void append(T value) override
    {
        mayBeReallocate();

        storage_[size_] = value;
        ++size_;
    }
    void replace(T value, unsigned int i) override
    {
        if (i >= size_) {
            replaceStatus_ = ReplaceStatus::IncorrectIndex;
            return;
        }
        storage_[i] = value;
        replaceStatus_ = ReplaceStatus::Ok;
    }
    void insert(T value, unsigned int i) override
    {
        if (i >= size_) {
            insertStatus_ = InsertStatus::IncorrectIndex;
            return;
        }

        mayBeReallocate();

        std::copy(storage_ + i, storage_ + size_, storage_ + i + 1);
        storage_[i] = value;
        ++size_;

        insertStatus_ = InsertStatus::Ok;
    }
    void remove(unsigned int i) override
    {
        if (i >= size_) {
            removeStatus_ = RemoveStatus::IncorrectIndex;
            return;
        }

        std::copy_backward(storage_ + i + 1, storage_ + size_, storage_ + i);
        --size_;

        mayBeDeallocate();
        removeStatus_ = RemoveStatus::Ok;
    }
    T get(unsigned int i) const override
    {
        if (i >= size_) {
            getStatus_ = GetStatus::IncorrectIndex;
            return T {};
        }
        getStatus_ = GetStatus::Ok;
        return storage_[i];
    }
    unsigned int size() const override
    {
        return size_;
    }

    AppendStatus getAppendStatus() const override
    {
        return appendStatus_;
    }
    ReplaceStatus getReplaceStatus() const override
    {
        return replaceStatus_;
    }
    InsertStatus getInsertStatus() const override
    {
        return insertStatus_;
    }
    RemoveStatus getRemoveStatus() const override
    {
        return removeStatus_;
    }
    GetStatus getGetStatus() const override
    {
        return getStatus_;
    }

private:
    void mayBeReallocate()
    {
        if (size_ == capacity_)
            reallocate_(capacity_ * kReallocMultiplier);
    }
    void mayBeDeallocate()
    {
        if (size_ < capacity_ * kDeallocThreshold)
            reallocate_(capacity_ / kDeallocDivider);
    }
    void reallocate_(unsigned int newCapacity)
    {
        T* newStorage = new T[newCapacity];
        std::copy(storage_, storage_ + size_, newStorage);
        delete[] storage_;
        storage_ = newStorage;
        capacity_ = newCapacity;
    }

private:
    const unsigned int kMinimalCapacity = 16;
    const double kReallocMultiplier = 2;
    const double kDeallocThreshold = 0.5;
    const double kDeallocDivider = 1.5;

private:
    unsigned int size_ = 0;
    unsigned int capacity_ = 0;
    T* storage_ = nullptr;

    AppendStatus appendStatus_ = AppendStatus::NotCalled;
    ReplaceStatus replaceStatus_ = ReplaceStatus::NotCalled;
    InsertStatus insertStatus_ = InsertStatus::NotCalled;
    RemoveStatus removeStatus_ = RemoveStatus::NotCalled;
    mutable GetStatus getStatus_ = GetStatus::NotCalled;
};

} // end of namespace dyn_array
