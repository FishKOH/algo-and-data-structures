#include <catch.hpp>

#include "NativeDict.h"

using namespace native_dict;

TEST_CASE("NativeDict::init")
{
    NativeDict<std::string> nativeDict(17);
    CHECK(nativeDict.has("same string") == false);
    nativeDict.get("same string");
    CHECK(nativeDict.getGetStatus() == GetStatus::HasNotKey);
    nativeDict.remove("same string");
    CHECK(nativeDict.getRemoveStatus() == RemoveStatus::HasNotKey);
}

TEST_CASE("NativeDict::put")
{
    NativeDict<int> nativeDict(17);
    nativeDict.put("A", 10);
    CHECK(nativeDict.getPutStatus() == PutStatus::Ok_PutNewKey);
    CHECK(nativeDict.has("A") == true);
    CHECK(nativeDict.get("A") == 10);
    CHECK(nativeDict.getGetStatus() == GetStatus::Ok);

    nativeDict.put("B", 11);
    CHECK(nativeDict.has("B") == true);
    CHECK(nativeDict.get("B") == 11);
    CHECK(nativeDict.getGetStatus() == GetStatus::Ok);

    nativeDict.put("FishKOH", 42);
    CHECK(nativeDict.has("FishKOH") == true);
    CHECK(nativeDict.get("FishKOH") == 42);
    CHECK(nativeDict.getGetStatus() == GetStatus::Ok);

    nativeDict.put("B", 8);
    CHECK(nativeDict.has("B") == true);
    CHECK(nativeDict.get("B") == 8);
    CHECK(nativeDict.getPutStatus() == PutStatus::Ok_UpdateExistKey);
}

TEST_CASE("NativeDict::remove")
{
    NativeDict<int> nativeDict(17);
    nativeDict.put("A", 10);
    nativeDict.remove("A");
    CHECK(nativeDict.getRemoveStatus() == RemoveStatus::Ok);
    CHECK(nativeDict.has("A") == false);
}
