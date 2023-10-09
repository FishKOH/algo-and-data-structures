cmake_minimum_required(VERSION 3.5)

project(ooap LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(SOURCES )
set(HEADERS bounded_stack/BoundedStack.h)

add_library(bounded_stack ${SOURCES} ${HEADERS} )
set_target_properties(bounded_stack PROPERTIES LINKER_LANGUAGE CXX)

#tests
add_executable(bounded_stack_test "main.cpp"
    "bounded_stack/BoundedStackTest.cpp")
add_test(NAME bounded_stack_test COMMAND bounded_stack_test)
set_target_properties(bounded_stack_test PROPERTIES LINKER_LANGUAGE CXX)


target_link_libraries(bounded_stack_test PRIVATE
    bounded_stack
    )

if(TARGET check)
    add_dependencies(check bounded_stack_test)
else()
    add_custom_target(check COMMAND ${CMAKE_CTEST_COMMAND}
                      DEPENDS bounded_stack_test )
endif ()
