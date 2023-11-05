#include <cassert>
#include <functional>
#include <numeric>

template <class T>
class AbstractBloomFilter {
public:
    // КОНСТРУКТОР:
    // постусловие: создаёт новый пустой фильтр Блюма
    // virtual AbstractBloomFilter(unsigned int maxSize);

    // КОМАНДЫ:

    //постусловие: в фильтр Блюма добавлено заданное значение
    virtual void put(T value) = 0;

    // ЗАПРОСЫ:
    virtual bool has(T value) const = 0;
};

class BitArray {
public:
    BitArray(unsigned int maxSize)
    {
        assert(maxSize <= 32);
    }
    void set(unsigned int index)
    {
        bits_ |= (1 << index);
    }
    void reset(unsigned int index)
    {
        bits_ &= (mask_ - (1 << index));
    }

    bool get(unsigned int index) const
    {
        return (bits_ & (1 << index)) >> index;
    }

private:
    unsigned int bits_ = 0;
    const unsigned int mask_ = (1ull << 32) - 1;
};

template <class T>
std::function<unsigned int(T)>
makeHashFun(unsigned int p, unsigned int maxSize)
{
    auto hashFun = [maxSize](T value) {
        return std::hash<T> {}(value) % maxSize;
    };
    return hashFun;
}

template <>
std::function<unsigned int(std::string)>
makeHashFun<std::string>(unsigned int p, unsigned int maxSize)
{
    auto hashFun = [p, maxSize](std::string value) {
        return std::reduce(value.begin(), value.end(), 0,
            [p, maxSize](unsigned int hash, char c) {
                return (hash * p + static_cast<unsigned int>(c)) % maxSize;
            });
    };
    return hashFun;
}

template <class T>
class BloomFilter : public AbstractBloomFilter<T> {
public:
    BloomFilter(unsigned int maxSize)
        : size_(maxSize)
        , bitArray_(size_)
    {
        hashFun1_ = makeHashFun<T>(17, size_);
        hashFun2_ = makeHashFun<T>(223, size_);
    }

    void put(T value) override
    {
        bitArray_.set(hashFun1_(value));
        bitArray_.set(hashFun2_(value));
    }

    bool has(T value) const override
    {
        return bitArray_.get(hashFun1_(value)) and bitArray_.get(hashFun2_(value));
    }

private:
    unsigned int size_ = 0;
    BitArray bitArray_;

    std::function<unsigned int(T)> hashFun1_;
    std::function<unsigned int(T)> hashFun2_;
};
