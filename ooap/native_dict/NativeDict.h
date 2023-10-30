#include <functional>
#include <optional>
#include <string>

namespace native_dict {

enum class PutStatus {
    NotCalled,
    Ok_PutNewKey,
    Ok_UpdateExistKey,
    HasNotEmptySlot
};

enum class GetStatus {
    NotCalled,
    Ok,
    HasNotKey
};

using RemoveStatus = GetStatus;

template <class T>
class AbstractNativeDict {
public:
    // КОНСТРУКТОР:
    // постусловие: создаёт новый пустой словарь
    // virtual AbstractNativeDict(unsigned int maxSize);

    // КОМАНДЫ:

    // предусловие: словарь не полон/есть место под заданные ключ-значение
    // постусловие: если в словаре отсутствует заданный ключ,
    // то в словарь добавлен заданный ключ и соответсвующее ему
    // заданное значение,
    // иначе перезаписывается значение по существующему заданному ключу
    virtual void put(const std::string& key, T value) = 0;

    // предусловие: в словаре имеется заданный ключ
    // постусловие: из словаря удалён ключ и соответсвующее ему значение
    virtual void remove(const std::string& key) = 0;

    // ЗАПРОСЫ:

    // предусловие: в словаре имеется заданный ключ
    virtual T get(const std::string& key) const = 0;

    virtual bool has(const std::string& key) const = 0;

    //ЗАПРОСЫ-СТАТУСЫ:

    virtual PutStatus getPutStatus() const = 0;
    virtual RemoveStatus getRemoveStatus() const = 0;
    virtual GetStatus getGetStatus() const = 0;
};

template <class T>
class NativeDict : public AbstractNativeDict<T> {
public:
    NativeDict(unsigned int maxSize)
        : size_(maxSize)
        , keys_(new std::optional<std::string>[size_])
        , values_(new std::optional<T>[size_])
    {
        hashFun_ = [size = size_](std::string key) {
            return std::hash<std::string> {}(key) % size;
        };
    }

    void put(const std::string& key, T value) override
    {
        auto existIndex = find_(key);
        if (existIndex.has_value()) {
            putStatus_ = PutStatus::Ok_UpdateExistKey;
            values_[existIndex.value()] = value;
            return;
        }

        auto newIndex = seekSlot_(key);
        if (not newIndex.has_value()) {
            putStatus_ = PutStatus::HasNotEmptySlot;
            return;
        }

        keys_[newIndex.value()] = key;
        values_[newIndex.value()] = value;
        putStatus_ = PutStatus::Ok_PutNewKey;
    }

    void remove(const std::string& key) override
    {
        auto index = find_(key);

        if (not index.has_value()) {
            removeStatus_ = RemoveStatus::HasNotKey;
            return;
        }
        keys_[index.value()].reset();
        values_[index.value()].reset();
        removeStatus_ = RemoveStatus::Ok;
    }

    T get(const std::string& key) const override
    {
        auto index = find_(key);

        if (not index.has_value()) {
            getStatus_ = GetStatus::HasNotKey;
            return T {};
        }
        getStatus_ = GetStatus::Ok;
        return values_[index.value()].value();
    }

    bool has(const std::string& key) const override
    {
        return find_(key).has_value();
    }

    PutStatus getPutStatus() const override
    {
        return putStatus_;
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
    std::optional<unsigned int> seekSlot_(const std::string& key) const
    {
        unsigned int index = hashFun_(key);

        for (unsigned int i = 0; i < size_; ++i) {
            if (not keys_[index].has_value())
                return index;
            index = (index + step_) % size_;
        }
        return std::nullopt;
    }

    std::optional<unsigned int> find_(const std::string& key) const
    {
        unsigned int index = hashFun_(key);

        for (unsigned int i = 0; i < size_; ++i) {
            if (not keys_[index].has_value())
                return std::nullopt;
            if (keys_[index].value() == key)
                return index;
            index = (index + step_) % size_;
        }
        return std::nullopt;
    }

private:
    unsigned int size_ = 0;
    unsigned int step_ = 1;
    std::optional<std::string>* keys_ = nullptr;
    std::optional<T>* values_ = nullptr;

    std::function<unsigned int(std::string)> hashFun_;

    PutStatus putStatus_ = PutStatus::NotCalled;
    RemoveStatus removeStatus_ = RemoveStatus::NotCalled;
    mutable GetStatus getStatus_ = GetStatus::NotCalled;
};

} // end of namespace dyn_array
