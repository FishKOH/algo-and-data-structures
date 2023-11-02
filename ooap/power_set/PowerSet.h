#include "../hash_table/HashTable.h"

namespace power_set {

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
class AbstractPowerSet : public hash_table::AbstractHashTable<T> {
public:
    // КОНСТРУКТОР:
    // постусловие: создаёт новое пустое множество
    // virtual AbstractPowerSet(unsigned int maxSize);

    // ЗАПРОСЫ:
    virtual AbstractPowerSet<T>& makeIntersection(const AbstractPowerSet<T>& set2);
    virtual AbstractPowerSet<T>& makeUnion(const AbstractPowerSet<T>& set2);
    virtual AbstractPowerSet<T>& makeDifference(const AbstractPowerSet<T>& set2);
    virtual bool isSubset(const AbstractPowerSet<T>& set2);
};

template <class T>
class PowerSet : public hash_table::HashTable<T> /*, public AbstractPowerSet<T>*/ {
public:
    PowerSet(unsigned int maxSize = 20'000)
        : hash_table::HashTable<T>(maxSize)
    {
    }

    PowerSet<T> makeIntersection(const PowerSet<T>& set2) /*override*/
    {
        PowerSet<T> intersectionSet(this->size());
        for (unsigned int i = 0; i < this->maxSize_; ++i) {
            if (this->storage_[i].has_value() and set2.has(this->storage_[i].value()))
                intersectionSet.put(this->storage_[i].value());
        }
        return intersectionSet;
    }
    PowerSet<T> makeUnion(const PowerSet<T>& set2) /*override*/
    {
        PowerSet<T> unionSet(this->size() + set2.size());
        for (unsigned int i = 0; i < this->maxSize_; ++i) {
            if (this->storage_[i].has_value())
                unionSet.put(this->storage_[i].value());
        }
        for (unsigned int i = 0; i < set2.maxSize_; ++i) {
            if (set2.storage_[i].has_value())
                unionSet.put(set2.storage_[i].value());
        }
        return unionSet;
    }
    PowerSet<T> makeDifference(const PowerSet<T>& set2) /*override*/
    {
        PowerSet<T> diffSet(this->size());
        for (unsigned int i = 0; i < this->maxSize_; ++i) {
            if (this->storage_[i].has_value() and not set2.has(this->storage_[i].value()))
                diffSet.put(this->storage_[i].value());
        }
        return diffSet;
    }
    bool isSubset(const PowerSet<T>& set2) /*override*/
    {
        for (unsigned int i = 0; i < set2.maxSize_; ++i) {
            if (set2.storage_[i].has_value() and not this->has(set2.storage_[i].value()))
                return false;
        }
        return true;
    }
};

} // end of namespace dyn_array
