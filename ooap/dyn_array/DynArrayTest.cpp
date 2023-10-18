#include <catch.hpp>

#include "DynArray.h"

using namespace dyn_array;

TEST_CASE("linked dynArray")
{
    DynArray<int> dynArray;
    CHECK(dynArray.size() == 0);

    dynArray.get(4);
    CHECK(dynArray.getGetStatus() == GetStatus::IncorrectIndex);
    dynArray.append(8);
    CHECK(dynArray.size() == 1);
    CHECK(dynArray.get(0) == 8);
    CHECK(dynArray.getGetStatus() == GetStatus::Ok);

    dynArray.replace(42, 0);
    CHECK(dynArray.size() == 1);
    CHECK(dynArray.get(0) == 42);
    CHECK(dynArray.getReplaceStatus() == ReplaceStatus::Ok);

    dynArray.insert(-1, 0);
    CHECK(dynArray.size() == 2);
    CHECK(dynArray.get(0) == -1);
    CHECK(dynArray.get(1) == 42);
    CHECK(dynArray.getReplaceStatus() == ReplaceStatus::Ok);

    dynArray.remove(1);
    CHECK(dynArray.size() == 1);
    CHECK(dynArray.get(0) == -1);
    CHECK(dynArray.getReplaceStatus() == ReplaceStatus::Ok);
}
