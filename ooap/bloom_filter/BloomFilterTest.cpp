#include <catch.hpp>

#include "BloomFilter.h"

std::array<std::string, 10> testStrings = {
    "0123456789",
    "1234567890",
    "2345678901",
    "3456789012",
    "4567890123",
    "5678901234",
    "6789012345",
    "7890123456",
    "8901234567",
    "9012345678"
};

TEST_CASE("BloomFilter::one element")
{
    BloomFilter<std::string> bloomFilter(32);
    CHECK_FALSE(bloomFilter.has("FishKOH"));
    CHECK_FALSE(bloomFilter.has(testStrings[0]));

    bloomFilter.put(testStrings[0]);
    CHECK(bloomFilter.has(testStrings[0]));
}

TEST_CASE("BloomFilter::full")
{
    BloomFilter<std::string> bloomFilter(32);
    for (auto s : testStrings)
        bloomFilter.put(s);

    for (auto s : testStrings)
        CHECK(bloomFilter.has(s));
}
