#include <catch.hpp>

#include "HashTable.h"

using namespace hash_table;

TEST_CASE("HashTable::simple case")
{
    HashTable<std::string> hashTable(10);
    CHECK(hashTable.has("same string") == false);

    hashTable.put("same string");
    CHECK(hashTable.has("same string") == true);
    CHECK(hashTable.getPutStatus() == PutStatus::Ok);

    hashTable.remove("same string");
    CHECK(hashTable.has("same string") == false);
    CHECK(hashTable.getRemoveStatus() == RemoveStatus::Ok);
}

TEST_CASE("HashTable::complex case")
{
    HashTable<std::string> hashTable(3);
    hashTable.put("string");
    hashTable.put("same string");
    hashTable.put("other string");
    CHECK(hashTable.getPutStatus() == PutStatus::Ok);

    hashTable.put("another string");
    CHECK(hashTable.getPutStatus() == PutStatus::HasNotEmptySlot);

    CHECK(hashTable.has("string"));
    CHECK(hashTable.has("same string"));
    CHECK(hashTable.has("other string"));
    CHECK(hashTable.has("another string") == false);

    hashTable.remove("another string");
    CHECK(hashTable.getRemoveStatus() == RemoveStatus::HasNotValue);
}
