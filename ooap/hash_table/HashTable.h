#include <algorithm>

namespace hash_table {

enum class PutStatus {
    NotCalled,
    Ok,
    HasNotEmptySlot
};

enum class RemoveStatus {
    NotCalled,
    Ok,
    HasNotValue
};

template <class T>
class AbstractHashTable {
public:
    // КОНСТРУКТОР:
    // постусловие: создаёт новую пустую хэш-таблицу
    // virtual AbstractHashTable(unsigned int maxSize);

    // КОМАНДЫ:

    //предусловие: таблица не полна/есть место под данный элемент
    //постусловие: в хэш-таблицу добавлено заданное значение
    virtual void put(T value) = 0;

    //предусловие:  заданное значение имеется в хэш-таблице
    //постусловие: из хэш-таблицу удалено заданное значение
    virtual void remove(T value) = 0;

    // ЗАПРОСЫ:
    virtual bool has(T value) const = 0;

    //ЗАПРОСЫ-СТАТУСЫ:

    virtual PutStatus getPutStatus() const = 0;
    virtual RemoveStatus getRemoveStatus() const = 0;
};

template <class T>
class HashTable : public AbstractHashTable<T> {
public:
    HashTable(unsigned int maxSize)
        : size_(maxSize)
        , storage_(new std::optional<T>[size_])
    {
        hashFun_ = [size = size_](T value) {
            return std::hash<T> {}(value) % size;
        };
    }

    void put(T value) override
    {
        auto index = seekSlot_(value);

        if (not index.has_value()) {
            putStatus_ = PutStatus::HasNotEmptySlot;
            return;
        }
        storage_[index.value()] = value;
        putStatus_ = PutStatus::Ok;
    }
    void remove(T value) override
    {
        auto index = find_(value);

        if (not index.has_value()) {
            removeStatus_ = RemoveStatus::HasNotValue;
            return;
        }
        storage_[index.value()].reset();
        removeStatus_ = RemoveStatus::Ok;
    }
    bool has(T value) const override
    {
        return find_(value).has_value();
    }

    PutStatus getPutStatus() const override
    {
        return putStatus_;
    }
    RemoveStatus getRemoveStatus() const override
    {
        return removeStatus_;
    }

private:
    std::optional<unsigned int> seekSlot_(T value) const
    {
        unsigned int index = hashFun_(value);

        for (unsigned int i = 0; i < size_; ++i) {
            if (not storage_[index].has_value())
                return index;
            index = (index + step_) % size_;
        }
        return std::nullopt;
    }

    std::optional<unsigned int> find_(T value) const
    {
        unsigned int index = hashFun_(value);

        for (unsigned int i = 0; i < size_; ++i) {
            if (not storage_[index].has_value())
                return std::nullopt;
            if (storage_[index].value() == value)
                return index;
            index = (index + step_) % size_;
        }
        return std::nullopt;
    }

private:
    unsigned int size_ = 0;
    unsigned int step_ = 1;
    std::optional<T>* storage_ = nullptr;

    std::function<unsigned int(T)> hashFun_;

    PutStatus putStatus_ = PutStatus::NotCalled;
    RemoveStatus removeStatus_ = RemoveStatus::NotCalled;
};

} // end of namespace dyn_array
