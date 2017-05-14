cmake_minimum_required(VERSION 3.0 FATAL_ERROR)

project(git_info_test)

set(git_info_REMOTE_PATTERN "NOhs/git_info.git")
add_subdirectory(git_info)

create_git_info_file(test/git_info.hpp cpp)
create_git_info_file(test/git_info.py python)

enable_testing()

add_executable(test_compile test/test_compile.cpp)

add_test(
    NAME              test_cpp_compile 
    COMMAND           $<TARGET_FILE:test_compile>
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/test)

add_test(
    NAME              test_python_works
    COMMAND           ${PYTHON_EXECUTABLE} test_git_info.py
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/test)

add_test(
    NAME              test_python_cpp_output_equal
    COMMAND           ${CMAKE_COMMAND} -E compare_files python_git.out cpp_git.out
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/test)


if(NOT ${IS_GIT_REPOSITORY})
    message(FATAL_ERROR "Not in a git repository!")
endif(NOT ${IS_GIT_REPOSITORY})

unset(git_info_REMOTE_PATTERN)