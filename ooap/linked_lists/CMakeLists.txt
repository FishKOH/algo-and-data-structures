cmake_minimum_required(VERSION 3.5)

project(ooap LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(SOURCES )
set(HEADERS LinkedList.h)

add_library(linked_lists ${SOURCES} ${HEADERS} )
set_target_properties(linked_lists PROPERTIES LINKER_LANGUAGE CXX)

#tests
add_executable(linked_lists_test "main.cpp"
    "LinkedListTest.cpp")
add_test(NAME linked_lists_test COMMAND linked_lists_test)
set_target_properties(linked_lists_test PROPERTIES LINKER_LANGUAGE CXX)

target_link_libraries(linked_lists_test PRIVATE
    linked_lists
    )

if(TARGET check)
    add_dependencies(check linked_lists_test)
else()
    add_custom_target(check COMMAND ${CMAKE_CTEST_COMMAND}
                      DEPENDS linked_lists_test )
endif ()
