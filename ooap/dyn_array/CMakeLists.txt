cmake_minimum_required(VERSION 3.5)

project(ooap LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(SOURCES )
set(HEADERS DynArray.h)

set(LIBRARY_NAME dyn_array)
add_library(${LIBRARY_NAME} ${SOURCES} ${HEADERS} )
set_target_properties(${LIBRARY_NAME} PROPERTIES LINKER_LANGUAGE CXX)

#tests
add_executable(${LIBRARY_NAME}_test "main.cpp"
    "DynArrayTest.cpp")
add_test(NAME ${LIBRARY_NAME}_test COMMAND ${LIBRARY_NAME}_test)
set_target_properties(${LIBRARY_NAME}_test PROPERTIES LINKER_LANGUAGE CXX)

target_link_libraries(${LIBRARY_NAME}_test PRIVATE
    ${LIBRARY_NAME}
    )

target_include_directories(${LIBRARY_NAME}_test PRIVATE "/home/nsv/workspace/ssr/stdssr/test/libs/Catch/single_include")

if(TARGET check)
    add_dependencies(check ${LIBRARY_NAME}_test)
else()
    add_custom_target(check COMMAND ${CMAKE_CTEST_COMMAND}
                      DEPENDS ${LIBRARY_NAME}_test )
endif ()
